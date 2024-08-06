# ttranking/core/views.py
from django.http import HttpResponseServerError, HttpResponseNotFound, Http404
from django.shortcuts import render
from django.template import loader
from players.models import Player


def home(request):
    ranking = Player.objects.all().order_by('-ranking')[:20]
    top = ranking[:3]
    return render(request, 'core/home.html', {'ranking': ranking, 'top': top})


def bad_request(request, exception):
    return render(request, 'core/400.html', status=400)


def page_not_found(request, exception):
    content = loader.render_to_string('core/404.html', {}, request)
    return HttpResponseNotFound(content)


def server_error(request):
    content = loader.render_to_string('core/500.html', {}, request)
    return HttpResponseServerError(content)

