# ttranking/matches/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import SinglesMatch, DoublesMatch
from .forms import SinglesMatchForm, DoublesMatchForm

def match_list(request):
    singles_matches = SinglesMatch.objects.all()
    doubles_matches = DoublesMatch.objects.all()
    return render(request, 'matches/match_list.html', {
        'singles_matches': singles_matches,
        'doubles_matches': doubles_matches,
    })

def match_detail(request, match_id):
    match_type = request.GET.get('match_type')
    if match_type == 'S':
        match = get_object_or_404(SinglesMatch, id=match_id)
    elif match_type == 'D':
        match = get_object_or_404(DoublesMatch, id=match_id)

    return render(request, 'matches/match_detail.html', {'match': match, 'match_type': match_type})

def match_add(request):
    match_type = request.GET.get('match_type')
    form_singles = None
    form_doubles = None

    if match_type == 'S':
        form_singles = SinglesMatchForm(request.POST or None)
    elif match_type == 'D':
        form_doubles = DoublesMatchForm(request.POST or None)

    if request.method == 'POST':
        if match_type == 'S' and form_singles.is_valid():
            form_singles.save()
            return redirect('match_list')
        elif match_type == 'D' and form_doubles.is_valid():
            form_doubles.save()
            return redirect('match_list')

    return render(request, 'matches/match_add.html', {
        'match_type': match_type,
        'form_singles': form_singles,
        'form_doubles': form_doubles,
    })

def match_update(request, match_id):
    match_type = request.GET.get('match_type')
    if match_type == 'S':
        match = get_object_or_404(SinglesMatch, id=match_id)
        form = SinglesMatchForm(instance=match)
    elif match_type == 'D':
        match = get_object_or_404(DoublesMatch, id=match_id)
        form = DoublesMatchForm(instance=match)

    if request.method == 'POST':
        if match_type == 'S':
            form = SinglesMatchForm(request.POST, instance=match)
        elif match_type == 'D':
            form = DoublesMatchForm(request.POST, instance=match)

        if form.is_valid():
            form.save()
            return redirect('match_list')

    return render(request, 'matches/match_update.html', {'form': form, 'match_type': match_type})

def match_delete(request, match_id):
    match_type = request.GET.get('match_type')
    if match_type == 'S':
        match = get_object_or_404(SinglesMatch, id=match_id)
    elif match_type == 'D':
        match = get_object_or_404(DoublesMatch, id=match_id)

    if request.method == 'POST':
        match.delete()
        return redirect('match_list')

    return render(request, 'matches/match_delete.html', {'match': match, 'match_type': match_type})
