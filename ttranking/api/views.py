# api/views.py
from django.urls import reverse

from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from players.models import Player
from players.serializers import PlayerSerializer

from matches.models import SinglesMatch, DoublesMatch
from matches.serializers import SinglesMatchSerializer, DoublesMatchSerializer


class APIRootView(APIView):
    """
    API root view
    """
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        return Response({
            'players': reverse('api:player_list'),
            'singles_matches': reverse('api:single_match_list'),
            'doubles_matches': reverse('api:double_match_list'),
        })


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

    def post(self, request):
        serializer = PlayerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
MATCHES
"""


class SingleMatchListCreateAPIView(APIView):
    """
    API view for singles matches model
    """
    def get(self, request):
        singles = SinglesMatch.objects.all().order_by('date')
        serializer = SinglesMatchSerializer(singles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SinglesMatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoubleMatchListCreateAPIView(APIView):
    """
    API view for doubles matches model
    """
    def get(self, request):
        doubles = DoublesMatch.objects.all().order_by('date')
        serializer = DoublesMatchSerializer(doubles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DoublesMatchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
