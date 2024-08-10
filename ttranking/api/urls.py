# players/api_urls.py
from django.urls import path, include
from rest_framework import status
from .views import APIRootView, PlayerListCreateAPIView, SingleMatchListCreateAPIView, DoubleMatchListCreateAPIView

app_name = 'api'

urlpatterns = [
    path('', APIRootView.as_view(), name='api_root'),
    path('players/', PlayerListCreateAPIView.as_view(), name='player_list'),
    path('single_matches/', SingleMatchListCreateAPIView.as_view(), name='single_match_list'),
    path('double_matches/', DoubleMatchListCreateAPIView.as_view(), name='double_match_list'),
]
