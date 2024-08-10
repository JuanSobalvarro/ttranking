# matches/api_views.py
from django.urls import reverse
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SinglesMatch, DoublesMatch
from .serializers import SinglesMatchSerializer, DoublesMatchSerializer


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