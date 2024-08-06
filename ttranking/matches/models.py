# ttranking/matches/models.py
from django.db import models
from django.core.exceptions import ValidationError
from players.models import Player

WINNING_POINTS = 2
LOSING_POINTS = 1


class SinglesMatch(models.Model):
    date = models.DateTimeField()
    player1 = models.ForeignKey(Player, related_name='singles_matches_as_player1', on_delete=models.CASCADE)
    player2 = models.ForeignKey(Player, related_name='singles_matches_as_player2', on_delete=models.CASCADE)
    player1_score = models.IntegerField(default=0)
    player2_score = models.IntegerField(default=0)
    winner = models.ForeignKey(Player, related_name='singles_matches_won', on_delete=models.CASCADE, null=True,
                               blank=True)

    def update_winner(self):
        if (self.player1_score >= 11 and self.player1_score >= self.player2_score + 2):
            self.winner = self.player1
        elif (self.player2_score >= 11 and self.player2_score >= self.player1_score + 2):
            self.winner = self.player2
        else:
            self.winner = None

    @property
    def winner_display(self):
        if self.winner:
            if self.winner == self.player1:
                return f"{self.player1} won"

            return f"{self.player2} won"

        return f""

    def update_player_points(self):
        self.update_winner()

        if self.pk:  # Check if it's an update
            # Fetch the previous match instance
            previous_match = SinglesMatch.objects.get(pk=self.pk)
            previous_winner = previous_match.winner

            if previous_winner != self.winner:
                # Remove points from the previous winner if they are no longer the winner
                if previous_winner:
                    previous_winner.remove_points(WINNING_POINTS)

                # Add points to the new winner
                if self.winner:
                    self.winner.add_points(WINNING_POINTS)
        else:
            # New match: assign points to the winner
            if self.winner:
                self.winner.add_points(WINNING_POINTS)

    @property
    def score(self) -> str:
        return f"{self.player1_score} - {self.player2_score}"

    def clean(self):
        if self.player1 == self.player2:
            raise ValidationError("Player 1 and Player 2 cannot be the same.")

    def save(self, *args, **kwargs):
        self.update_player_points()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.player1} vs {self.player2} - {self.date}"


class DoublesMatch(models.Model):
    date = models.DateTimeField()
    team1_player1 = models.ForeignKey(Player, related_name='doubles_matches_team1_player1', on_delete=models.CASCADE)
    team1_player2 = models.ForeignKey(Player, related_name='doubles_matches_team1_player2', on_delete=models.CASCADE)
    team2_player1 = models.ForeignKey(Player, related_name='doubles_matches_team2_player1', on_delete=models.CASCADE)
    team2_player2 = models.ForeignKey(Player, related_name='doubles_matches_team2_player2', on_delete=models.CASCADE)
    team1_score = models.IntegerField(default=0)
    team2_score = models.IntegerField(default=0)
    winner_team = models.CharField(max_length=10, blank=True, null=True)

    @property
    def score(self) -> str:
        return f"{self.team1_score} - {self.team2_score}"

    @property
    def winner_display(self):
        if self.winner_team:
            if self.winner_team == "Team 1":
                return f"{self.team1_player1} and {self.team1_player2} won"

            return f"{self.team2_player1} and {self.team2_player2} won"

        return ""

    def update_winner(self):
        if (self.team1_score >= 11 and self.team1_score >= self.team2_score + 2):
            self.winner_team = "Team 1"
        elif (self.team2_score >= 11 and self.team2_score >= self.team1_score + 2):
            self.winner_team = "Team 2"
        else:
            self.winner_team = None

    def update_team_points(self):
        self.update_winner()

        if self.pk:  # Check if it's an update
            # Fetch the previous match instance
            previous_match = DoublesMatch.objects.get(pk=self.pk)
            previous_winner_team = previous_match.winner_team

            if previous_winner_team != self.winner_team:
                # Remove points from the previous winning team if they are no longer the winner
                if previous_winner_team == "Team 1":
                    self.team1_player1.remove_points(WINNING_POINTS)
                    self.team1_player2.remove_points(WINNING_POINTS)
                elif previous_winner_team == "Team 2":
                    self.team2_player1.remove_points(WINNING_POINTS)
                    self.team2_player2.remove_points(WINNING_POINTS)

                # Add points to the new winning team
                if self.winner_team == "Team 1":
                    self.team1_player1.add_points(WINNING_POINTS)
                    self.team1_player2.add_points(WINNING_POINTS)
                elif self.winner_team == "Team 2":
                    self.team2_player1.add_points(WINNING_POINTS)
                    self.team2_player2.add_points(WINNING_POINTS)
        else:
            # New match: assign points to the winning team
            if self.winner_team == "Team 1":
                self.team1_player1.add_points(WINNING_POINTS)
                self.team1_player2.add_points(WINNING_POINTS)
            elif self.winner_team == "Team 2":
                self.team2_player1.add_points(WINNING_POINTS)
                self.team2_player2.add_points(WINNING_POINTS)

    def clean(self):
        if self.team1_player1 == self.team1_player2:
            raise ValidationError("Team 1 players cannot be the same.")
        if self.team2_player1 == self.team2_player2:
            raise ValidationError("Team 2 players cannot be the same.")
        all_players = {self.team1_player1, self.team1_player2, self.team2_player1, self.team2_player2}
        if len(all_players) < 4:
            raise ValidationError("Players cannot be repeated across teams.")

    def save(self, *args, **kwargs):
        self.clean()
        self.update_team_points()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Team 1: {self.team1_player1} & {self.team1_player2} vs Team 2: {self.team2_player1} & {self.team2_player2} - {self.date}"


class MatchStats(models.Model):
    match = models.OneToOneField(SinglesMatch, on_delete=models.CASCADE, null=True, blank=True)
    doubles_match = models.OneToOneField(DoublesMatch, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.match:
            return f"Stats for singles match {self.match}"
        elif self.doubles_match:
            return f"Stats for doubles match {self.doubles_match}"
        return "No match stats"
