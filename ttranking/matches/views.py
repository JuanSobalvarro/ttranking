from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import SinglesMatch, DoublesMatch
from .forms import SinglesMatchForm, DoublesMatchForm


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


def match_list(request):
    singles_matches = SinglesMatch.objects.all()
    doubles_matches = DoublesMatch.objects.all()
    return render(request, 'matches/match_list.html', {
        'singles_matches': singles_matches,
        'doubles_matches': doubles_matches,
    })


def match_detail(request, match_id):
    match_type = request.GET.get('match_type')
    match, _ = get_match_and_form(match_id, match_type)

    return render(request, 'matches/match_detail.html', {'match': match, 'match_type': match_type})


def match_add(request):
    match_type = request.GET.get('match_type')
    form_singles = SinglesMatchForm(request.POST or None) if match_type == 'S' else None
    form_doubles = DoublesMatchForm(request.POST or None) if match_type == 'D' else None

    if request.method == 'POST':
        if match_type == 'S' and form_singles.is_valid():
            form_singles.save()
            messages.success(request, 'Singles match added successfully!')
            return redirect('match_list')
        elif match_type == 'D' and form_doubles.is_valid():
            form_doubles.save()
            messages.success(request, 'Doubles match added successfully!')
            return redirect('match_list')
        else:
            messages.error(request, 'The form has errors')

    return render(request, 'matches/match_add.html', {
        'match_type': match_type,
        'form_singles': form_singles,
        'form_doubles': form_doubles,
    })


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
            return redirect('match_list')
        else:
            messages.error(request, 'There was an error with your submission.')

    return render(request, 'matches/match_update.html', {'form': form, 'match_type': match_type})


def match_delete(request, match_id):
    match_type = request.GET.get('match_type')
    match, _ = get_match_and_form(match_id, match_type)

    if request.method == 'POST':
        match.delete()
        messages.success(request, 'Match deleted successfully!')
        return redirect('match_list')

    return render(request, 'matches/match_delete.html', {'match': match, 'match_type': match_type})
