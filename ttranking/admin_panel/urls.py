# admin_panel/urls.py
from django.urls import path
from .views import AdminHomeView

app_name = 'admin'

urlpatterns = [
    path('home/', AdminHomeView.as_view(), name='admin_home'),
]