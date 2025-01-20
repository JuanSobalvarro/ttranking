# ttranking/players/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'players'

# Default routes for api consistency
router = DefaultRouter()
router.register(r'', views.PlayerViewSet)

urlpatterns = [
    path('country-choices/', views.country_choices, name='country-choices'),
    path('', include(router.urls)),
]
