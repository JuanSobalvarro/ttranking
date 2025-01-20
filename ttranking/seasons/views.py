from rest_framework import viewsets
from .models import Season
from .serializers import SeasonSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

class SeasonViewSet(viewsets.ModelViewSet):
    queryset = Season.objects.all().order_by('start_date')
    serializer_class = SeasonSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticatedOrReadOnly]
        return [permission() for permission in permission_classes]
