# ttranking/core/views.py
from django.http import HttpResponseServerError, HttpResponseNotFound
from django.shortcuts import render
from django.template import loader

from players.models import Player
from players.serializers import PlayerSerializer

from matches.models import SinglesMatch, DoublesMatch
from matches.serializers import SinglesMatchSerializer, DoublesMatchSerializer

from django.urls import reverse

from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication


class APIRootView(APIView):
    """
    API root view
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        return Response({
            'players': reverse('players:player-list'),
            'singles_matches': reverse('matches:singlesmatch-list'),
            'doubles_matches': reverse('matches:doublesmatch-list'),
            'seasons': reverse('seasons:season-list'),
        })

class HomeView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        ranking = Player.objects.order_by('-ranking', 'matches_played')[:20]

        top = ranking[:3]


        top_winrate = sorted(Player.objects.all().order_by('-matches_played'), key=lambda player: player.winrate, reverse=True)[:6]

        matches_played = SinglesMatch.objects.count() + DoublesMatch.objects.count()

        data = {
            'matchesPlayed': matches_played,
            'topPlayers': PlayerSerializer(top, many=True).data,
            'topByWinrate': PlayerSerializer(top_winrate, many=True).data,
            'ranking': PlayerSerializer(ranking, many=True).data,
        }

        return Response(data)

def bad_request(request, exception):
    return render(request, 'core/400.html', status=400)


def page_not_found(request, exception):
    content = loader.render_to_string('core/404.html', {}, request)
    return HttpResponseNotFound(content)


def server_error(request):
    content = loader.render_to_string('core/500.html', {}, request)
    return HttpResponseServerError(content)