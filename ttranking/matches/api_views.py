# ttranking/matches/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import SinglesMatch, DoublesMatch, MatchStats
from .serializers import SinglesMatchSerializer, DoublesMatchSerializer, MatchStatsSerializer


class SinglesMatchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SinglesMatch.objects.all().order_by('-date')
    serializer_class = SinglesMatchSerializer
    # permission_classes = [IsAuthenticated]  # Adjust permissions as needed


class DoublesMatchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = DoublesMatch.objects.all().order_by('-date')
    serializer_class = DoublesMatchSerializer
    # permission_classes = [IsAuthenticated]  # Adjust permissions as needed


class MatchStatsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = MatchStats.objects.all()
    serializer_class = MatchStatsSerializer
    # permission_classes = [IsAuthenticated]  # Adjust permissions as needed
