# ttranking/api/urls.py
from django.urls import path, include
from rest_framework import status
from core.views import APIRootView
from players.api_views import PlayerListCreateAPIView, PlayerDetailAPIView
from matches.api_views import SingleMatchListCreateAPIView, DoubleMatchListCreateAPIView

app_name = 'api'

urlpatterns = [
    path('', APIRootView.as_view(), name='api_root'),
    path('players/', PlayerListCreateAPIView.as_view(), name='player_list'),
    path('players/<int:pk>/', PlayerDetailAPIView.as_view(), name='player_detail'),
    path('single_matches/', SingleMatchListCreateAPIView.as_view(), name='single_match_list'),
    path('double_matches/', DoubleMatchListCreateAPIView.as_view(), name='double_match_list'),
]
