# ttranking/matches/models.py
from django.db import models
from django.utils.timezone import datetime
from django.core.exceptions import ValidationError
from players.models import Player
from seasons.models import Season

WINNING_POINTS = 2
LOSING_POINTS = 0

class SinglesMatch(models.Model):
    date = models.DateTimeField()
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='singles_matches', blank=True, null=True)
    player1 = models.ForeignKey(Player, related_name='singles_matches_as_player1', on_delete=models.CASCADE)
    player2 = models.ForeignKey(Player, related_name='singles_matches_as_player2', on_delete=models.CASCADE)
    player1_score = models.IntegerField(default=0)
    player2_score = models.IntegerField(default=0)
    winner = models.ForeignKey(Player, related_name='singles_matches_won', on_delete=models.CASCADE, null=True, blank=True)

    @property
    def players(self):
        return [self.player1, self.player2]

    @property
    def get_season(self) -> Season:
        return Season.get_season_for_datetime(self.date)

    def update_winner(self):
        if self.player1_score >= 11 and self.player1_score >= self.player2_score + 2:
            self.winner = self.player1
        elif self.player2_score >= 11 and self.player2_score >= self.player1_score + 2:
            self.winner = self.player2
        else:
            self.winner = None

    @property
    def winner_display(self):
        if self.winner:
            return f"{self.winner} won"
        return ""

    def update_player_points(self):
        self.update_winner()
        if self.pk:
            previous_match = SinglesMatch.objects.get(pk=self.pk)
            previous_winner = previous_match.winner
            if previous_winner != self.winner:
                if previous_winner:
                    previous_winner.remove_points(WINNING_POINTS)
                if self.winner:
                    self.winner.add_points(WINNING_POINTS)
        else:
            if self.winner:
                self.winner.add_points(WINNING_POINTS)

    def update_matches_played(self):
        if self.pk:
            instance = SinglesMatch.objects.get(pk=self.pk)
            if instance.player1 != self.player1:
                instance.player1.matches_played -= 1
                self.player1.matches_played += 1
                instance.player1.save(update_fields=['matches_played'])
                self.player1.save(update_fields=['matches_played'])
            if instance.player2 != self.player2:
                instance.player2.matches_played -= 1
                self.player2.matches_played += 1
                instance.player2.save(update_fields=['matches_played'])
                self.player2.save(update_fields=['matches_played'])
        else:
            self.player1.matches_played += 1
            self.player2.matches_played += 1
            self.player1.save(update_fields=['matches_played'])
            self.player2.save(update_fields=['matches_played'])

    @property
    def score(self) -> str:
        return f"{self.player1_score} - {self.player2_score}"

    def clean(self):
        if self.player1 == self.player2:
            raise ValidationError("Player 1 and Player 2 cannot be the same.")

    def save(self, *args, **kwargs):
        self.clean()
        self.season = self.get_season
        self.update_matches_played()
        self.update_player_points()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.winner:
            self.winner.remove_points(WINNING_POINTS)
        self.player1.matches_played -= 1
        self.player2.matches_played -= 1
        self.player1.save(update_fields=['matches_played'])
        self.player2.save(update_fields=['matches_played'])
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.player1} vs {self.player2} - {self.date}"

class DoublesMatch(models.Model):
    date = models.DateTimeField()
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='doubles_matches', blank=True, null=True)
    team1_player1 = models.ForeignKey(Player, related_name='doubles_matches_team1_player1', on_delete=models.CASCADE)
    team1_player2 = models.ForeignKey(Player, related_name='doubles_matches_team1_player2', on_delete=models.CASCADE)
    team2_player1 = models.ForeignKey(Player, related_name='doubles_matches_team2_player1', on_delete=models.CASCADE)
    team2_player2 = models.ForeignKey(Player, related_name='doubles_matches_team2_player2', on_delete=models.CASCADE)
    team1_score = models.IntegerField(default=0)
    team2_score = models.IntegerField(default=0)
    winner_team = models.CharField(max_length=10, blank=True, null=True)

    @property
    def players(self):
        return [self.team1_player1, self.team1_player2, self.team2_player1, self.team2_player2]

    @property
    def get_season(self):
        return Season.get_season_for_datetime(self.date)

    @property
    def winners(self):
        if self.winner_team == 'Team 1':
            return [self.team1_player1, self.team1_player2]
        elif self.winner_team == 'Team 2':
            return [self.team2_player1, self.team2_player2]
        return []

    @property
    def score(self) -> str:
        return f"{self.team1_score} - {self.team2_score}"

    @property
    def winner_display(self):
        self.update_winner()
        if self.winner_team:
            if self.winner_team == "Team 1":
                return f"{self.team1_player1} and {self.team1_player2} won"
            return f"{self.team2_player1} and {self.team2_player2} won"
        return ""

    def update_winner(self):
        if self.team1_score >= 11 and self.team1_score >= self.team2_score + 2:
            self.winner_team = "Team 1"
        elif self.team2_score >= 11 and self.team2_score >= self.team1_score + 2:
            self.winner_team = "Team 2"
        else:
            self.winner_team = None

    def update_team_points(self):
        self.update_winner()
        if self.pk:
            previous_match = DoublesMatch.objects.get(pk=self.pk)
            previous_winners = previous_match.winners
            for winner in previous_winners:
                winner.remove_points(WINNING_POINTS)
            for winner in self.winners:
                winner.add_points(WINNING_POINTS)
        else:
            for winner in self.winners:
                winner.add_points(WINNING_POINTS)

    def update_matches_played(self):
        print("Updating matches played")
        new_players = [self.team1_player1, self.team1_player2, self.team2_player1, self.team2_player2]
        if self.pk:
            instance = DoublesMatch.objects.get(pk=self.pk)
            instance_players = [instance.team1_player1, instance.team1_player2, instance.team2_player1, instance.team2_player2]
            for instance_player, new_player in zip(instance_players, new_players):
                if instance_player != new_player:
                    instance_player.matches_played -= 1
                    new_player.matches_played += 1
                    instance_player.save(update_fields=['matches_played'])
                    new_player.save(update_fields=['matches_played'])
        else:
            for player in new_players:
                player.matches_played += 1
                player.save(update_fields=['matches_played'])

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
        self.season = self.get_season
        self.update_matches_played()
        self.update_team_points()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        for winner in self.winners:
            winner.remove_points(WINNING_POINTS)
        for player in self.players:
            player.matches_played -= 1
            player.save(update_fields=['matches_played'])
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Team 1: {self.team1_player1} & {self.team1_player2} vs Team 2: {self.team2_player1} & {self.team2_player2} - {self.date}"