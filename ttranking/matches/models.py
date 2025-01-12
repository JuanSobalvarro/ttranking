# ttranking/matches/models.py
from django.db import models
from django.core.exceptions import ValidationError
from players.models import Player
from seasons.models import Season

WINNING_POINTS = 2
LOSING_POINTS = 0


class SinglesMatch(models.Model):
    date = models.DateTimeField()
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='singles_matches')
    player1 = models.ForeignKey(Player, related_name='singles_matches_as_player1', on_delete=models.CASCADE)
    player2 = models.ForeignKey(Player, related_name='singles_matches_as_player2', on_delete=models.CASCADE)
    player1_score = models.IntegerField(default=0)
    player2_score = models.IntegerField(default=0)
    winner = models.ForeignKey(Player, related_name='singles_matches_won', on_delete=models.CASCADE, null=True,
                               blank=True)

    @property
    def players(self):
        return [self.player1, self.player2]

    @property
    def get_season(self) -> Season:
        # Dynamically calculate the season based on the date
        return Season.get_season_for_date(self.date.date())

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
            if self.winner == self.player1:
                return f"{self.player1} won"

            return f"{self.player2} won"

        return f""

    def update_player_points(self):
        self.update_winner()

        if self.pk:  # Check if it's an update
            # Fetch the previous match instance
            previous_match: SinglesMatch = SinglesMatch.objects.get(pk=self.pk)
            previous_winner: Player = previous_match.winner

            if previous_winner != self.winner:
                # Remove points from the previous winner if they are no longer the winner
                if previous_winner:
                    previous_winner.remove_points(WINNING_POINTS)

                # Add points to the new winner
                if self.winner:
                    self.winner.add_points(WINNING_POINTS)

                # print("Previous winner", previous_winner)
                # print("Winner", self.winner)
                # print("Rankings updates: ", previous_winner.ranking, self.winner.ranking)

        else:
            # New match: assign points to the winner
            if self.winner:
                self.winner.add_points(WINNING_POINTS)

    def update_matches_played(self):
        # Handles changes in matches played by the players

        # If we are doing an update we should remove points from the previous players
        if self.pk:
            # Get instance
            instance: SinglesMatch = SinglesMatch.objects.get(pk=self.pk)

            if instance.player1 != self.player1:
                instance.player1.matches_played -= 1
                self.player1.matches_played += 1

            if instance.player2 != self.player2:
                instance.player2.matches_played -= 1
                self.player2.matches_played += 1

            instance.player1.save()
            instance.player2.save()
            self.player1.save()
            self.player2.save()

            return

        # Add the match to the new players
        self.player1.matches_played += 1
        self.player2.matches_played += 1
        self.player1.save()
        self.player2.save()

    @property
    def score(self) -> str:
        return f"{self.player1_score} - {self.player2_score}"

    def clean(self):
        if self.player1 == self.player2:
            raise ValidationError("Player 1 and Player 2 cannot be the same.")

    def save(self, *args, **kwargs):
        self.clean()
        # UPDATE IN THIS ORDER, FIRST MATCHES, THEN PLAYER POINTS. WHY? IDFK
        # Well it looks like it is that when we update the matches played we save the players models
        # so fix this Juan ;p

        self.season = self.get_season

        self.update_matches_played()
        self.update_player_points()

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # revert the winner points
        if self.winner:
            self.winner.remove_points(WINNING_POINTS)

        # Now remove 1 match from the match count of the players
        self.player1.matches_played -= 1;
        self.player2.matches_played -= 1;

        # save players
        self.player1.save()
        self.player2.save()

        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.player1} vs {self.player2} - {self.date}"


class DoublesMatch(models.Model):
    date = models.DateTimeField()
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='doubles_matches')
    team1_player1 = models.ForeignKey(Player, related_name='doubles_matches_team1_player1', on_delete=models.CASCADE)
    team1_player2 = models.ForeignKey(Player, related_name='doubles_matches_team1_player2', on_delete=models.CASCADE)
    team2_player1 = models.ForeignKey(Player, related_name='doubles_matches_team2_player1', on_delete=models.CASCADE)
    team2_player2 = models.ForeignKey(Player, related_name='doubles_matches_team2_player2', on_delete=models.CASCADE)
    team1_score = models.IntegerField(default=0)
    team2_score = models.IntegerField(default=0)
    winner_team = models.CharField(max_length=10, blank=True, null=True)

    @property
    def players(self):
        """
        Gives you a list of the players who played this match
        :return:
        """
        return [self.team1_player1, self.team1_player2, self.team2_player1, self.team2_player2]

    @property
    def get_season(self):
        # Dynamically calculate the season based on the date
        return Season.get_season_for_date(self.date.date())

    @property
    def list_winners(self):
        if self.winner_team == 'Team 1':
            return [self.team1_player1, self.team1_player2]
        elif self.winner_team == 'Team 2':
            return [self.team2_player1, self.team2_player2]
        return []

    @property
    def winners(self):
        """
        Returns the winners of the two teams.
        :return:
        """
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
            previous_winners = previous_match.winners

            for winner in previous_winners:
                winner.remove_points(WINNING_POINTS)

            for winner in self.winners:
                winner.add_points(WINNING_POINTS)

        else:
            # New match: assign points to the winning team
            self.winners[0].add_points(WINNING_POINTS)
            self.winners[1].add_points(WINNING_POINTS)


    def update_matches_played(self):
        # Handles changes in matches played by the players
        new_players: list[Player] = [self.team1_player1, self.team1_player2,
                                     self.team2_player1, self.team2_player2]

        # If we are doing an update we should remove points from the previous players
        if self.pk:
            # Get instance
            instance: DoublesMatch = DoublesMatch.objects.get(pk=self.pk)
            instance_players: list[Player] = [instance.team1_player1, instance.team1_player2,
                                instance.team2_player1, instance.team2_player2]

            for instance_player, new_player in zip(instance_players, new_players):
                if instance_player != new_player:
                    instance_player.matches_played -= 1
                    new_player.matches_played += 1
                    instance_player.save()
                    new_player.save()

            return

        for player in new_players:
            player.matches_played += 1
            player.save()

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
        # revert the winner points
        if self.winners:
            self.winners[0].remove_points(WINNING_POINTS)
            self.winners[1].remove_points(WINNING_POINTS)

        # Now remove 1 match from the match count of the players
        self.team1_player1.matches_played -= 1
        self.team1_player2.matches_played -= 1
        self.team2_player1.matches_played -= 1
        self.team2_player2.matches_played -= 1

        # save players
        self.team1_player1.save()
        self.team1_player2.save()
        self.team2_player1.save()
        self.team2_player2.save()

        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Team 1: {self.team1_player1} & {self.team1_player2} vs Team 2: {self.team2_player1} & {self.team2_player2} - {self.date}"

