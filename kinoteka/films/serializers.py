from rest_framework import serializers
from .models import FilmCard, Type, Category


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmCard
        fields = ('id', 'film_name', 'film_description', 'film_release_date', 'film_preview_image',
                  'film_videofile', 'category', 'type')


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('name',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)
