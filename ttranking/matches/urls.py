# ttranking/matches/urls.py
from django.urls import path
from . import views

app_name = 'matches'

urlpatterns = [
    path('', views.match_list, name='match_list'),
    # path('<int:pk>/', views.match_detail, name='match_detail'),
]

