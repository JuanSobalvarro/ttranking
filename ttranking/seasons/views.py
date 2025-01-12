from django.shortcuts import render
from seasons.models import Season

def season_list(request):
    seasons = Season.objects.all()
    return render(request, 'seasons/season_list.html', context={'seasons': seasons})

def season_detail(request, player_id):
    season
    return render(request, 'seasons/season_detail.html')
