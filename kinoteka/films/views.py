from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import FilmCard
from .serializers import FilmSerializer

class FilmViewSet(viewsets.ModelViewSet):
    queryset = FilmCard.objects.all()
    serializer_class = FilmSerializer
class FilmsAPIView(generics.ListCreateAPIView):
    queryset = FilmCard.objects.all()
    serializer_class = FilmSerializer
class FilmAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FilmCard.objects.all()
    serializer_class = FilmSerializer
