from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import SinglesMatch, DoublesMatch, SinglesGame, DoublesGame
from .serializers import SinglesMatchSerializer, DoublesMatchSerializer, SinglesGameSerializer, DoublesGameSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny

class GamePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class SinglesGameViewSet(viewsets.ModelViewSet):
    queryset = SinglesGame.objects.all()
    serializer_class = SinglesGameSerializer
    pagination_class = GamePagination

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

class DoublesGameViewSet(viewsets.ModelViewSet):
    queryset = DoublesGame.objects.all()
    serializer_class = DoublesGameSerializer
    pagination_class = GamePagination

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

class MatchPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class SinglesMatchViewSet(viewsets.ModelViewSet):
    queryset = SinglesMatch.objects.all().order_by('-date')
    serializer_class = SinglesMatchSerializer
    pagination_class = MatchPagination

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]


class DoublesMatchViewSet(viewsets.ModelViewSet):
    queryset = DoublesMatch.objects.all().order_by('-date')
    serializer_class = DoublesMatchSerializer
    pagination_class = MatchPagination

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]