# ttranking/core/views.py
from django.shortcuts import render
from players.models import Player


def home(request):
    ranking = Player.objects.all().order_by('-ranking')[:20]
    return render(request, 'core/home.html', {'ranking': ranking})


def bad_request(request, exception):
    return render(request, 'core/400.html', status=400)


def page_not_found(request, exception):
    return render(request, 'core/404.html', status=404)


def server_error(request):
    return render(request, 'core/500.html', status=500)

