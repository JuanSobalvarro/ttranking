# ttranking/matches/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import SinglesMatchViewSet, DoublesMatchViewSet, MatchStatsViewSet

router = DefaultRouter()
router.register(r'singles_matches', SinglesMatchViewSet)
router.register(r'doubles_matches', DoublesMatchViewSet)
router.register(r'match_stats', MatchStatsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
