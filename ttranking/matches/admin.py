# ttranking/matches/admin.py
from django.contrib import admin
from .models import SinglesMatch, DoublesMatch, MatchStats

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

@admin.register(MatchStats)
class MatchStatsAdmin(admin.ModelAdmin):
    list_display = ('match', 'doubles_match')
    search_fields = ('match__player1__name', 'doubles_match__team1_player1__name')
    list_filter = ('match', 'doubles_match')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('match', 'doubles_match')

    def has_add_permission(self, request):
        return False  # Disable adding new MatchStats through the admin

    def has_delete_permission(self, request, obj=None):
        return False  # Disable deleting MatchStats through the admin
