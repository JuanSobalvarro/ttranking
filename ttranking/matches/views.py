from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import SinglesMatch, DoublesMatch
from .serializers import SinglesMatchSerializer, DoublesMatchSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny


class MatchPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 20

class SinglesMatchViewSet(viewsets.ModelViewSet):
    queryset = SinglesMatch.objects.all()
    serializer_class = SinglesMatchSerializer
    pagination_class = MatchPagination

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]


class DoublesMatchViewSet(viewsets.ModelViewSet):
    queryset = DoublesMatch.objects.all()
    serializer_class = DoublesMatchSerializer
    pagination_class = MatchPagination

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]