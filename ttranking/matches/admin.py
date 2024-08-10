# ttranking/matches/admin.py
from django.contrib import admin
from .models import SinglesMatch, DoublesMatch

@admin.register(SinglesMatch)
class SinglesMatchAdmin(admin.ModelAdmin):
    list_display = ('date', 'player1', 'player2', 'player1_score', 'player2_score', 'winner')
    search_fields = ('player1__name', 'player2__name', 'player1_score', 'player2_score')
    list_filter = ('date', 'winner')

@admin.register(DoublesMatch)
class DoublesMatchAdmin(admin.ModelAdmin):
    list_display = ('date', 'team1_player1', 'team1_player2', 'team2_player1', 'team2_player2', 'team1_score', 'team2_score', 'winner_team')
    search_fields = ('team1_player1__name', 'team1_player2__name', 'team2_player1__name', 'team2_player2__name', 'team1_score', 'team2_score')
    list_filter = ('date', 'winner_team')
