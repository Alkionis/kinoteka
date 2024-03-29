from django.contrib import admin

from .models import FilmCard,Category,Type

admin.site.register([FilmCard, Category, Type])
