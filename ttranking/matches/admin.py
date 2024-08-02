# ttranking/matches/admin.py
from django.contrib import admin
from .models import Match, MatchStats


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('match_type', 'date', 'player1', 'player2', 'winner')
    list_filter = ('match_type', 'date')
    search_fields = ('player1__name', 'player2__name', 'team1', 'team2')


@admin.register(MatchStats)
class MatchStatsAdmin(admin.ModelAdmin):
    list_display = ('match', 'aces', 'faults')
