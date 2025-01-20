# admin_panel/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from players.models import Player
from matches.models import SinglesMatch, DoublesMatch
from datetime import timedelta
from django.utils import timezone

class AdminHomeView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        registered_players = Player.objects.count()
        one_week_ago = timezone.now() - timedelta(days=7)
        matches_played_last_week = SinglesMatch.objects.filter(date__gte=one_week_ago).count() + DoublesMatch.objects.filter(date__gte=one_week_ago).count()
        player_activity_trends = []  # Add logic to calculate player activity trends

        data = {
            'registeredPlayers': registered_players,
            'matchesPlayedLastWeek': matches_played_last_week,
            'playerActivityTrends': player_activity_trends,
        }
        return Response(data)