from django.urls import path
from . import views

app_name = 'seasons'

urlpatterns = [
    path('', views.season_list, name='season_list'),
    path('<int:season_id>/', views.season_detail, name='season_detail'),
]