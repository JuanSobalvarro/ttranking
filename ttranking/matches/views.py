# ttranking/matches/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Match
from .forms import MatchForm

def match_list(request):
    matches = Match.objects.all().order_by('-date')
    return render(request, 'matches/match_list.html', {'matches': matches})

def match_detail(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    return render(request, 'matches/match_detail.html', {'match': match})

def match_create(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('match_list')
    else:
        form = MatchForm()
    return render(request, 'matches/match_form.html', {'form': form})

def match_update(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    if request.method == 'POST':
        form = MatchForm(request.POST, instance=match)
        if form.is_valid():
            form.save()
            return redirect('match_detail', match_id=match.id)
    else:
        form = MatchForm(instance=match)
    return render(request, 'matches/match_form.html', {'form': form})

def match_delete(request, match_id):
    match = get_object_or_404(Match, id=match_id)
    if request.method == 'POST':
        match.delete()
        return redirect('match_list')
    return render(request, 'matches/match_confirm_delete.html', {'match': match})
