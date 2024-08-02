# ttranking/matches/models.py
from django.db import models
from players.models import Player

class SinglesMatch(models.Model):
    date = models.DateTimeField()
    player1 = models.ForeignKey(Player, related_name='singles_matches_as_player1', on_delete=models.CASCADE)
    player2 = models.ForeignKey(Player, related_name='singles_matches_as_player2', on_delete=models.CASCADE)
    score = models.CharField(max_length=20)
    winner = models.ForeignKey(Player, related_name='singles_matches_won', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.player1} vs {self.player2} - {self.date}"


class DoublesMatch(models.Model):
    date = models.DateTimeField()
    team1_player1 = models.ForeignKey(Player, related_name='doubles_matches_team1_player1', on_delete=models.CASCADE)
    team1_player2 = models.ForeignKey(Player, related_name='doubles_matches_team1_player2', on_delete=models.CASCADE)
    team2_player1 = models.ForeignKey(Player, related_name='doubles_matches_team2_player1', on_delete=models.CASCADE)
    team2_player2 = models.ForeignKey(Player, related_name='doubles_matches_team2_player2', on_delete=models.CASCADE)
    score = models.CharField(max_length=20)
    winner_team = models.CharField(max_length=10, choices=[('Team1', 'Team 1'), ('Team2', 'Team 2')], blank=True, null=True)

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
