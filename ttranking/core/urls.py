# ttranking/core/urls.py
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
