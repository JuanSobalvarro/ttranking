# ttranking/players/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.player_list, name='player_list'),
    path('<int:player_id>/', views.player_detail, name='player_detail'),
    path('create/', views.player_create, name='player_create'),
    path('edit/<int:player_id>/', views.player_edit, name='player_edit'),
    path('delete/<int:player_id>', views.player_delete, name='player_delete'),
]
