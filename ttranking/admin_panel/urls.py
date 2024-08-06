from django.urls import path
from . import views

app_name = 'admin_panel'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # login/logout
    path('login/', views.AdminLoginView.as_view(), name='login'),
    path('logout/', views.AdminLogoutView.as_view(), name='logout'),

    # players
    path('players/', views.player_list, name='player_list'),
    path('players/add/', views.player_add, name='player_add'),
    path('players/<int:pk>/', views.player_edit, name='player_edit'),
    path('players/<int:pk>/delete/', views.player_delete, name='player_delete'),

    # matches
    path('matches/', views.match_list, name='match_list'),
    path('matches/add/', views.match_add, name='match_add'),
    path('matches/<int:pk>/update/', views.match_update, name='match_update'),
    path('matches/<int:pk>/delete/', views.match_delete, name='match_delete'),
]
