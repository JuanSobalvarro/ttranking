from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SeasonViewSet

app_name = 'seasons'

router = DefaultRouter()
router.register(r'', SeasonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]