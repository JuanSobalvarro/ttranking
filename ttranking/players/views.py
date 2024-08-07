# ttrankin/players/views.py
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from .models import Player

PLAYERS_PER_PAGE = 6


def player_list(request):
    player_list = Player.objects.all().order_by('ranking')
    paginator = Paginator(player_list, PLAYERS_PER_PAGE)  # Show PLAYERS_PER_PAGE players per page

    page = request.GET.get('page', 1)
    try:
        players = paginator.page(page)
    except PageNotAnInteger:
        players = paginator.page(1)
    except EmptyPage:
        players = paginator.page(paginator.num_pages)

    return render(request, 'players/player_list.html', {'players': players})


def player_detail(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    return render(request, 'players/player_detail.html', {'player': player})
