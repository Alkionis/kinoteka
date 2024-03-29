from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import FilmCard, Type, Category
from .serializers import FilmSerializer, TypeSerializer, CategorySerializer


class FilmViewSet(viewsets.ModelViewSet):
    queryset = FilmCard.objects.all()
    serializer_class = FilmSerializer


class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
# class FilmsAPIView(generics.ListCreateAPIView):
#     queryset = FilmCard.objects.all()
#     serializer_class = FilmSerializer
# class FilmAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = FilmCard.objects.all()
#     serializer_class = FilmSerializer
