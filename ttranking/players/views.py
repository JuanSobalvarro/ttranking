# ttrankin/players/views.py
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny
from rest_framework.pagination import PageNumberPagination
from .models import Player, COUNTRY_CHOICES
from .serializers import PlayerSerializer

PLAYERS_PER_PAGE = 6

@api_view(['GET'])
def country_choices(request):
    countries = COUNTRY_CHOICES
    return Response(countries)

class PlayerPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 20

class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all().order_by('first_name', 'last_name')
    serializer_class = PlayerSerializer
    pagination_class = PlayerPagination

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    # def list(self, request):
    #     pass
    #
    # def create(self, request):
    #     pass
    #
    # def retrieve(self, request, pk=None):
    #     pass
    #
    # def update(self, request, pk=None):
    #     pass
    #
    # def partial_update(self, request, pk=None):
    #     pass
    #
    # def destroy(self, request, pk=None):
    #     pass


# def player_list(request):
#     player_list = Player.objects.all().order_by('first_name', 'last_name')
#     paginator = Paginator(player_list, PLAYERS_PER_PAGE)  # Show PLAYERS_PER_PAGE players per page
#
#     page = request.GET.get('page', 1)
#     try:
#         players = paginator.page(page)
#     except PageNotAnInteger:
#         players = paginator.page(1)
#     except EmptyPage:
#         players = paginator.page(paginator.num_pages)
#
#     return render(request, 'players/player_list.html', {'players': players})
#
#
# def player_detail(request, player_id):
#     player = get_object_or_404(Player, id=player_id)
#     return render(request, 'players/player_detail.html', {'player': player})
