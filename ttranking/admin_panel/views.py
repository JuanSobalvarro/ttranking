# admin_panel/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.views import View

from .forms import SinglesMatchForm, DoublesMatchForm, PlayerForm

from matches.models import SinglesMatch
from matches.models import DoublesMatch

from players.models import Player


class AdminLoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'admin_panel/login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST or None)
        if form.is_valid():
            user = form.get_user()
            if user.is_staff:
                login(request, user)
                return redirect('/admin-panel/')
        return render(request, 'admin_panel/login.html', {'form': form})


class AdminLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/admin-panel/')

    def post(self, request):
        logout(request)
        return redirect('/admin-panel/')

def is_admin(user):
    return user.is_staff


@login_required
def dashboard(request):
    # Your dashboard view logic here
    return render(request, 'admin_panel/admin_dashboard.html')


"""
PLAYERS VIEWS
"""


@login_required
def player_list(request):
    players = Player.objects.all()
    return render(request, 'admin_panel/players/player_list.html', {'players': players})


@login_required
def player_add(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_panel:player_list')
    else:
        form = PlayerForm()
    return render(request, 'admin_panel/players/player_add.html', {'form': form})


@login_required
def player_edit(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES, instance=player)
        if form.is_valid():
            form.save()
            messages.success(request, 'Player updated successfully!')
            return redirect('admin_panel:player_list')  # Redirect to the player list or detail view
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PlayerForm(instance=player)

    return render(request, 'admin_panel/players/player_edit.html', {'form': form, 'player': player})


@login_required
def player_delete(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    if request.method == 'POST':
        player.delete()
        return redirect('admin_panel:player_list')
    return render(request, 'admin_panel/players/player_delete.html', {'player': player})


"""
MATCHES VIEWS
"""


@login_required
def get_match_and_form(match_id, match_type):
    if match_type == 'S':
        match = get_object_or_404(SinglesMatch, id=match_id)
        form = SinglesMatchForm(instance=match)
    elif match_type == 'D':
        match = get_object_or_404(DoublesMatch, id=match_id)
        form = DoublesMatchForm(instance=match)
    else:
        match = None
        form = None
    return match, form


@login_required
def match_list(request):
    singles_matches = SinglesMatch.objects.all()
    doubles_matches = DoublesMatch.objects.all()
    return render(request, 'admin_panel/matches/match_list.html', {'singles_matches': singles_matches, 'doubles_matches': doubles_matches})


@login_required
def match_add(request):
    match_type = request.GET.get('match_type')
    form_singles = SinglesMatchForm(request.POST or None) if match_type == 'S' else None
    form_doubles = DoublesMatchForm(request.POST or None) if match_type == 'D' else None

    if request.method == 'POST':
        if match_type == 'S' and form_singles.is_valid():
            form_singles.save()
            messages.success(request, 'Singles match added successfully!')
            return redirect('admin_panel:match_list')
        elif match_type == 'D' and form_doubles.is_valid():
            form_doubles.save()
            messages.success(request, 'Doubles match added successfully!')
            return redirect('admin_panel:match_list')
        else:
            messages.error(request, 'The form has errors')

    return render(request, 'admin_panel/matches/match_add.html', {
        'match_type': match_type,
        'form_singles': form_singles,
        'form_doubles': form_doubles,
    })


@login_required
def match_update(request, match_id):
    match_type = request.GET.get('match_type')
    match, form = get_match_and_form(match_id, match_type)

    if request.method == 'POST':
        if match_type == 'S':
            form = SinglesMatchForm(request.POST, instance=match)
        elif match_type == 'D':
            form = DoublesMatchForm(request.POST, instance=match)

        if form.is_valid():
            form.save()
            messages.success(request, 'Match updated successfully!')
            return redirect('admin_panel:match_list')
        else:
            messages.error(request, 'There was an error with your submission.')

    return render(request, 'admin_panel/matches/match_update.html', {'form': form, 'match_type': match_type})


@login_required
def match_delete(request, match_id):
    match_type = request.GET.get('match_type')
    match, _ = get_match_and_form(match_id, match_type)

    if request.method == 'POST':
        match.delete()
        messages.success(request, 'Match deleted successfully!')
        return redirect('admin_panel:match_list')

    return render(request, 'admin_panel/matches/match_delete.html', {'match': match, 'match_type': match_type})
