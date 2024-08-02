# ttranking/players/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.player_list, name='player_list'),
    path('<int:player_id>/', views.player_detail, name='player_detail'),
    path('create/', views.player_create, name='player_create'),
    path('<int:player_id>/edit/', views.player_update, name='player_update'),
    path('<int:player_id>/delete/', views.player_delete, name='player_delete'),
]
