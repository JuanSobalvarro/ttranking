# players/api_urls.py
from django.urls import path, include
from rest_framework import routers
from . import api_views

router = routers.DefaultRouter()
router.register(r'players', api_views.PlayerViewSet)

urlpatterns = [
    path('', include(router.urls), name='players_list'),
]
