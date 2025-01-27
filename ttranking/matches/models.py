from django.db import models
from django.db.transaction import commit
from django.utils.timezone import datetime
from django.core.exceptions import ValidationError
from players.models import Player, Ranking
from seasons.models import Season


class SinglesGame(models.Model):
    """
    A singles game is a game between two players.
    Fields: match, player1_score, player2_score, winner
    """
    match = models.ForeignKey('SinglesMatch', related_name='games', on_delete=models.CASCADE)
    player1_score = models.IntegerField(default=0)
    player2_score = models.IntegerField(default=0)
    winner = models.IntegerField(blank=True, null=True)

    def update_match(self):
        match = SinglesMatch.objects.get(pk=self.match.pk)
        match.save()

    def update_winner(self):
        if self.player1_score > self.player2_score:
            self.winner = 1
        elif self.player2_score > self.player1_score:
            self.winner = 2
        else:
            self.winner = None
        # print("Game winner updated: ", self.winner)

    def save(self, *args, **kwargs):
        self.clean()
        self.update_winner()
        super().save(*args, **kwargs)
        self.update_match()

    def clean(self):
        if self.player1_score == self.player2_score:
            raise ValidationError("Scores cannot be equal.")

    def __str__(self):
        return f"Game: {self.player1_score} - {self.player2_score}"

class DoublesGame(models.Model):
    """
    A doubles game is a game between two teams of two players each.
    Fields: match, team1_score, team2_score, winner
    """
    match = models.ForeignKey('DoublesMatch', related_name='games', on_delete=models.CASCADE)
    team1_score = models.IntegerField(default=0)
    team2_score = models.IntegerField(default=0)
    winner = models.IntegerField(blank=True, null=True)

    def update_match(self):
        match = DoublesMatch.objects.get(pk=self.match.pk)
        match.save()

    def update_winner(self):
        if self.team1_score > self.team2_score:
            self.winner = 1
        elif self.team2_score > self.team1_score:
            self.winner = 2
        else:
            self.winner = None
        # print("Game winner updated: ", self.winner)

    def save(self, *args, **kwargs):
        self.clean()
        self.update_winner()
        super().save(*args, **kwargs)
        self.update_match()

    def clean(self):
        if self.team1_score == self.team2_score:
            raise ValidationError("Scores cannot be equal.")

    def __str__(self):
        return f"Game: {self.team1_score} - {self.team2_score}"

class SinglesMatch(models.Model):
    """
    A singles match is a match between two players.
    Fields: date, season, player1, player2, winner
    """
    date = models.DateTimeField(default=datetime.now, blank=True)
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='singles_matches', blank=True, null=True)
    player1 = models.ForeignKey(Player, related_name='singles_matches_as_player1', on_delete=models.CASCADE)
    player2 = models.ForeignKey(Player, related_name='singles_matches_as_player2', on_delete=models.CASCADE)
    winner = models.ForeignKey(Player, related_name='singles_matches_won', on_delete=models.CASCADE, null=True, blank=True)

    @property
    def games_won(self):
        player1_wins = SinglesGame.objects.filter(match=self.id, winner=1).count()
        player2_wins = SinglesGame.objects.filter(match=self.id, winner=2).count()
        return player1_wins, player2_wins

    @property
    def get_season(self):
        return Season.get_season_for_datetime(self.date)

    def update_winner(self):
        player1_wins, player2_wins = self.games_won
        # print("Game wins found: ", player1_wins, player2_wins)
        if player1_wins > player2_wins:
            self.winner = self.player1
        elif player2_wins > player1_wins:
            self.winner = self.player2
        else:
            self.winner = None

        # print("Match winner updated: ", self.winner)

    def update_players(self):
        winning_points = Season.objects.get(pk=self.season.pk).singles_points_for_win
        losing_points = Season.objects.get(pk=self.season.pk).singles_points_for_loss

        player1_ranking = Ranking.objects.get(player=self.player1, season=self.season)
        player2_ranking = Ranking.objects.get(player=self.player2, season=self.season)

        # Check if the match is already created and remove the points from the previous winner and add points to the loser
        if self.pk:
            previous_match = SinglesMatch.objects.select_related('player1', 'player2').get(pk=self.pk)
            prev_player1_ranking = Ranking.objects.get(pk=previous_match.player1.pk)
            prev_player2_ranking = Ranking.objects.get(pk=previous_match.player2.pk)

            # First remove points from winner and add points to loser
            if previous_match.winner == previous_match.player1:
                prev_player1_ranking.remove_points(winning_points)
                prev_player2_ranking.add_points(losing_points)
            elif previous_match.winner == previous_match.player2:
                prev_player2_ranking.remove_points(winning_points)
                prev_player1_ranking.add_points(losing_points)

            # Remove the matches played from the previous players
            prev_player1_ranking.remove_match()
            prev_player2_ranking.remove_match()

        # Then add points to winner and remove points from loser
        # print("Updating points given winner: ", self.winner)
        if self.winner == self.player1:
            player1_ranking.add_points(winning_points)
            player2_ranking.remove_points(losing_points)
        elif self.winner == self.player2:
            player2_ranking.add_points(winning_points)
            player1_ranking.remove_points(losing_points)

        player1_ranking.add_match()
        player2_ranking.add_match()


    def save(self, *args, **kwargs):
        self.clean()

        if not self.season:
            self.season = self.get_season

        self.update_winner()
        self.update_players()
        # print("Saving match with winner: ", self.winner)
        super().save(*args, **kwargs)

    def clean(self):
        if self.player1 == self.player2:
            raise ValidationError("Player 1 and Player 2 cannot be the same.")

    def delete(self, *args, **kwargs):
        winning_points = Season.objects.get(pk=self.season.pk).singles_points_for_win
        losing_points = Season.objects.get(pk=self.season.pk).singles_points_for_loss

        if self.player1 == self.winner:
            self.player1.remove_points(winning_points)
            self.player2.add_points(losing_points)
        elif self.player2 == self.winner:
            self.player2.remove_points(winning_points)
            self.player1.add_points(losing_points)

        self.player1.remove_match()
        self.player2.remove_match()

        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.player1} vs {self.player2} - {self.date}"


class DoublesMatch(models.Model):
    """
    A doubles match is a match between two teams of two players each.
    Fields: date, season, team1_player1, team1_player2, team2_player1, team2_player2, winner_1, winner_2
    """
    date = models.DateTimeField()
    season = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='doubles_matches', blank=True, null=True)
    team1_player1 = models.ForeignKey(Player, related_name='doubles_matches_team1_player1', on_delete=models.CASCADE)
    team1_player2 = models.ForeignKey(Player, related_name='doubles_matches_team1_player2', on_delete=models.CASCADE)
    team2_player1 = models.ForeignKey(Player, related_name='doubles_matches_team2_player1', on_delete=models.CASCADE)
    team2_player2 = models.ForeignKey(Player, related_name='doubles_matches_team2_player2', on_delete=models.CASCADE)
    winner_1 = models.ForeignKey(Player, related_name='doubles_matches_won1', on_delete=models.CASCADE, null=True, blank=True)
    winner_2 = models.ForeignKey(Player, related_name='doubles_matches_won2', on_delete=models.CASCADE, null=True, blank=True)

    @property
    def winners(self):
        return self.winner_1, self.winner_2

    @property
    def get_season(self):
        return Season.get_season_for_datetime(self.date)

    @property
    def games_won(self):
        """
        Returns the number of games won by each team.

        This is achieved by counting the number of games where the team1_score is greater than the team2_score and
        vice versa for the games that have a relation with the match.
        :return:
        """
        team1_wins = DoublesGame.objects.filter(match=self.id, winner=1).count()
        team2_wins = DoublesGame.objects.filter(match=self.id, winner=2).count()
        return team1_wins, team2_wins

    def update_winner(self):
        team1_wins, team2_wins = self.games_won
        if team1_wins > team2_wins:
            self.winner_1 = self.team1_player1
            self.winner_2 = self.team1_player2
        elif team2_wins > team1_wins:
            self.winner_1 = self.team2_player1
            self.winner_2 = self.team2_player2
        else:
            self.winner_1 = None
            self.winner_2 = None

    def update_players(self):
        winning_points = Season.objects.get(pk=self.season.pk).doubles_points_for_win
        losing_points = Season.objects.get(pk=self.season.pk).doubles_points_for_loss

        player1 = Player.objects.get(pk=self.team1_player1.pk)
        player2 = Player.objects.get(pk=self.team1_player2.pk)
        player3 = Player.objects.get(pk=self.team2_player1.pk)
        player4 = Player.objects.get(pk=self.team2_player2.pk)

        # Check if the match is already created
        if self.pk:
            previous_match = DoublesMatch.objects.select_related('team1_player1', 'team1_player2', 'team2_player1', 'team2_player2').get(pk=self.pk)
            prev_player1 = Player.objects.get(pk=previous_match.team1_player1.pk)
            prev_player2 = Player.objects.get(pk=previous_match.team1_player2.pk)
            prev_player3 = Player.objects.get(pk=previous_match.team2_player1.pk)
            prev_player4 = Player.objects.get(pk=previous_match.team2_player2.pk)

            # First remove points from winner and add points to loser
            if previous_match.winner_1 == previous_match.team1_player1 and previous_match.winner_2 == previous_match.team1_player2:
                prev_player1.remove_points(winning_points)
                prev_player2.remove_points(winning_points)
                prev_player3.add_points(losing_points)
                prev_player4.add_points(losing_points)
            elif previous_match.winner_1 == previous_match.team2_player1 and previous_match.winner_2 == previous_match.team2_player2:
                prev_player3.remove_points(winning_points)
                prev_player4.remove_points(winning_points)
                prev_player1.add_points(losing_points)
                prev_player2.add_points(losing_points)

            # Remove the matches played from the previous players
            prev_player1.remove_match()
            prev_player2.remove_match()
            prev_player3.remove_match()
            prev_player4.remove_match()


        # Then add points to winner and remove points from loser
        if self.winner_1 == self.team1_player1 and self.winner_2 == self.team1_player2:
            player1.add_points(winning_points)
            player2.add_points(winning_points)
            player3.remove_points(losing_points)
            player4.remove_points(losing_points)
        elif self.winner_1 == self.team2_player1 and self.winner_2 == self.team2_player2:
            player3.add_points(winning_points)
            player4.add_points(winning_points)
            player1.remove_points(losing_points)
            player2.remove_points(losing_points)

        player1.add_match()
        player2.add_match()
        player3.add_match()
        player4.add_match()


    def save(self, *args, **kwargs):
        self.clean()

        if not self.season:
            self.season = self.get_season

        self.update_winner()
        self.update_players()
        # print("Saving doubles match with winners: ", self.winner_1, self.winner_2)
        super().save(*args, **kwargs)

    def clean(self):
        if self.team1_player1 == self.team1_player2 or self.team2_player1 == self.team2_player2:
            raise ValidationError("Players in the same team cannot be the same.")
        all_players = {self.team1_player1, self.team1_player2, self.team2_player1, self.team2_player2}
        if len(all_players) < 4:
            raise ValidationError("Players cannot be repeated across teams.")

    def delete(self, *args, **kwargs):
        winning_points = Season.objects.get(pk=self.season.pk).doubles_points_for_win
        losing_points = Season.objects.get(pk=self.season.pk).doubles_points_for_loss

        if self.winner_1 == self.team1_player1 and self.winner_2 == self.team1_player2:
            self.team1_player1.remove_points(winning_points)
            self.team1_player2.remove_points(winning_points)
            self.team2_player1.add_points(losing_points)
            self.team2_player2.add_points(losing_points)
        elif self.winner_1 == self.team2_player1 and self.winner_2 == self.team2_player2:
            self.team2_player1.remove_points(winning_points)
            self.team2_player2.remove_points(winning_points)
            self.team1_player1.add_points(losing_points)
            self.team1_player2.add_points(losing_points)

        self.team1_player1.remove_match()
        self.team1_player2.remove_match()
        self.team2_player1.remove_match()
        self.team2_player2.remove_match()

        super().delete(*args, **kwargs)

    def __str__(self):
        return f"Team 1: {self.team1_player1} & {self.team1_player2} vs Team 2: {self.team2_player1} & {self.team2_player2} - {self.date}"
