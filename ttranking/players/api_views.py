# players/api_views.py
from rest_framework import generics, viewsets, permissions
from .models import Player
from .serializers import PlayerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows players to be viewed or edited.
    """
    queryset = Player.objects.all().order_by('first_name', 'last_name')
    serializer_class = PlayerSerializer
    permission_classes = [permissions.IsAuthenticated]

