# ttranking/core/views.py
from django.shortcuts import render


def home(request):
    return render(request, 'core/home.html')


def bad_request(request, exception):
    return render(request, 'core/400.html', status=400)


def page_not_found(request, exception):
    return render(request, 'core/404.html', status=404)


def server_error(request):
    return render(request, 'core/500.html', status=500)

