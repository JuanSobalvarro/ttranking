# ttranking/core/views.py
from django.http import HttpResponseServerError, HttpResponseNotFound, Http404
from django.shortcuts import render
from django.template import loader
from players.models import Player
from matches.models import SinglesMatch, DoublesMatch

from django.urls import reverse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class APIRootView(APIView):
    """
    API root view
    """
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        return Response({
            'players': reverse('api:player_list'),
            'singles_matches': reverse('api:single_match_list'),
            'doubles_matches': reverse('api:double_match_list'),
        })


def home(request):
    ranking = Player.objects.all().order_by('-ranking', 'matches_played')[:20]
    top = ranking[:3]

    # calculate top by winrate
    top_winrate = sorted(Player.objects.all().order_by('-matches_played'), key=lambda player: player.winrate, reverse=True)[:6]

    matches_played = SinglesMatch.objects.all().count() + DoublesMatch.objects.all().count()

    return render(request, 'core/home.html', {'top': top, 'ranking': ranking,
                                              'top_by_winrate': top_winrate, 'matches_played': matches_played})


def bad_request(request, exception):
    return render(request, 'core/400.html', status=400)


def page_not_found(request, exception):
    content = loader.render_to_string('core/404.html', {}, request)
    return HttpResponseNotFound(content)


def server_error(request):
    content = loader.render_to_string('core/500.html', {}, request)
    return HttpResponseServerError(content)
