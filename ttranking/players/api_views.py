# ttranking/players/api_views.py
from django.urls import reverse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Player
from .serializers import PlayerSerializer


class PlayerListCreateAPIView(APIView):
    """
    API view for players model
    """
    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):
        players = Player.objects.all().order_by('first_name', 'last_name')
        serializer = PlayerSerializer(players, many=True)
        return Response(serializer.data)


class PlayerDetailAPIView(APIView):
    """
    API view for retrieving, updating, and deleting a single player instance
    """
    def get_permissions(self):
        if self.request.method in ['GET']:
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request, pk):
        player = get_object_or_404(Player, pk=pk)
        serializer = PlayerSerializer(player)
        return Response(serializer.data)

    def post(self, request, pk):
        player = get_object_or_404(Player, pk=pk)
        serializer = PlayerSerializer(player, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        player = get_object_or_404(Player, pk=pk)
        serializer = PlayerSerializer(player, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        player = get_object_or_404(Player, pk=pk)
        player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

