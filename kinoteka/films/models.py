from django.db import models
from django.urls import reverse


# Модель, репрезентирующая таблипцу с фильмами в БД
class FilmCard(models.Model):
    # Fields
    id = models.BigAutoField(primary_key=True)
    film_name = models.CharField(max_length=200, help_text='Введите название фильма')
    film_description = models.TextField(max_length=99999, help_text='Введите описание фильма')
    film_release_date = models.DateField(default=True, help_text='Дата выпуска фильма')
    film_preview_image = models.ImageField(upload_to="uploads/preview/", help_text='Превью для фильма')
    # TODO подумать над реализацией хранения видео / пока буду использовать models.FileField
    film_videofile = models.FileField(upload_to="uploads/films/", help_text='Собственно, сам фильм')
    category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True)
    type = models.ForeignKey("Type", on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.film_name


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name