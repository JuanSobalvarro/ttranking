from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.http import HttpResponse
from .models import SinglesMatch, DoublesMatch

MATCHES_PER_PAGE = 5


def match_list(request):
    # Get all singles matches and paginate
    singles_match_list = SinglesMatch.objects.all().order_by('-date')
    singles_page = request.GET.get('singles_page', 1)

    singles_paginator = Paginator(singles_match_list, MATCHES_PER_PAGE)  # Show MATCHES_PER_PAGE singles matches per page
    try:
        singles_matches = singles_paginator.page(singles_page)
    except PageNotAnInteger:
        singles_matches = singles_paginator.page(1)
    except EmptyPage:
        singles_matches = singles_paginator.page(singles_paginator.num_pages)

    # Get all doubles matches and paginate
    doubles_match_list = DoublesMatch.objects.all().order_by('-date')
    doubles_page = request.GET.get('doubles_page', 1)

    doubles_paginator = Paginator(doubles_match_list, MATCHES_PER_PAGE)  # Show MATCHES_PER_PAGE doubles matches per page
    try:
        doubles_matches = doubles_paginator.page(doubles_page)
    except PageNotAnInteger:
        doubles_matches = doubles_paginator.page(1)
    except EmptyPage:
        doubles_matches = doubles_paginator.page(doubles_paginator.num_pages)

    context = {
        'singles_matches': singles_matches,
        'singles_count': singles_matches.count(),
        'doubles_matches': doubles_matches,
        'doubles_count': doubles_matches.count(),
    }

    return render(request, 'matches/match_list.html', context)


def match_detail(request, pk):
    match_type = request.GET.get('match_type')
    if match_type == 'S':
        singles_match = get_object_or_404(SinglesMatch, pk=pk)
        return render(request, 'matches/match_detail.html', {'match': singles_match, 'match_type': match_type})

    elif match_type == 'D':
        doubles_match = get_object_or_404(DoublesMatch, pk=pk)
        return render(request, 'matches/match_detail.html', {'match': doubles_match, 'match_type': match_type})

    else:
        return HttpResponse('Invalid match_type')

