# ttranking/matches/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.match_list, name='match_list'),
    path('<int:match_id>/', views.match_detail, name='match_detail'),
]

