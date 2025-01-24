# ttranking/matches/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SinglesMatchViewSet, DoublesMatchViewSet, SinglesGameViewSet, DoublesGameViewSet

app_name = 'matches'

router = DefaultRouter()
router.register(r'singles-games', SinglesGameViewSet)
router.register(r'doubles-games', DoublesGameViewSet)
router.register(r'singles', SinglesMatchViewSet)
router.register(r'doubles', DoublesMatchViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

