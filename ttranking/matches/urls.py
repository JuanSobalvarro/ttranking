# ttranking/matches/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.match_list, name='match_list'),
    path('add/', views.match_add, name='match_add'),
    path('update/<int:match_id>/', views.match_update, name='match_update'),
    path('delete/<int:match_id>/', views.match_delete, name='match_delete'),
    path('detail/<int:match_id>/', views.match_detail, name='match_detail'),
]

