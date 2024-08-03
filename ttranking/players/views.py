# ttrankin/players/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Player
from .forms import PlayerForm


def player_list(request):
    players = Player.objects.all().order_by('ranking')
    return render(request, 'players/player_list.html', {'players': players})


def player_detail(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    return render(request, 'players/player_detail.html', {'player': player})


def player_create(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm()
    return render(request, 'players/player_add.html', {'form': form})


def player_edit(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player_list')  # Redirect to the player list or detail view
    else:
        form = PlayerForm(instance=player)

    return render(request, 'players/player_edit.html', {'form': form, 'player': player})


def player_delete(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    if request.method == 'POST':
        player.delete()
        return redirect('player_list')
    return render(request, 'players/player_confirm_delete.html', {'player': player})
