from rest_framework import serializers
from .models import FilmCard


class FilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmCard
        fields = ('id', 'film_name', 'film_description', 'film_release_date', 'film_preview_image', 'film_videofile')