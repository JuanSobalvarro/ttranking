# ttranking/matches/models.py
from django.db import models
from players.models import Player


class Match(models.Model):
    SINGLES = 'S'
    DOUBLES = 'D'
    MATCH_TYPE_CHOICES = [
        (SINGLES, 'Singles'),
        (DOUBLES, 'Doubles'),
    ]

    match_type = models.CharField(max_length=1, choices=MATCH_TYPE_CHOICES)
    date = models.DateTimeField()
    player1 = models.ForeignKey(Player, related_name='matches_as_player1', on_delete=models.CASCADE)
    player2 = models.ForeignKey(Player, related_name='matches_as_player2', on_delete=models.CASCADE, null=True,
                                blank=True)
    team1 = models.CharField(max_length=100, blank=True)
    team2 = models.CharField(max_length=100, blank=True)
    score = models.CharField(max_length=20)
    winner = models.ForeignKey(Player, related_name='matches_won', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.player1} vs {self.player2} - {self.date}"


class MatchStats(models.Model):
    match = models.OneToOneField(Match, on_delete=models.CASCADE)

    def __str__(self):
        return f"Stats for match {self.match}"
