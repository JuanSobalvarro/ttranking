from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
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
    match, _ = get_match_and_form(match_id, match_type)

    return render(request, 'matches/match_detail.html', {'match': match, 'match_type': match_type})



