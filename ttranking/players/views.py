# ttrankin/players/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Player
from .forms import PlayerForm


def player_list(request):
    players = Player.objects.all().order_by('ranking')
    return render(request, 'players/player_list.html', {'players': players})


def player_detail(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    return render(request, 'players/player_detail.html', {'player': player})