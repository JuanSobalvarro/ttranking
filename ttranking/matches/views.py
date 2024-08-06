from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from .models import SinglesMatch, DoublesMatch


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
        singles_match = get_object_or_404(SinglesMatch, pk=match_id)
        return render(request, 'matches/match_detail.html', {'match': singles_match, 'match_type': match_type})

    elif match_type == 'D':
        doubles_match = get_object_or_404(DoublesMatch, pk=match_id)
        return render(request, 'matches/match_detail.html', {'match': doubles_match, 'match_type': match_type})

    else:
        return HttpResponse('Invalid match_type')

