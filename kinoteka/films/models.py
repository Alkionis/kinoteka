from django.db import models
from django.urls import reverse


# Модель, репрезентирующая таблипцу с фильмами в БД
class FilmCard(models.Model):
    # Fields
    id = models.BigAutoField(primary_key=True)
    film_name = models.CharField(max_length=200, help_text='Введите название фильма')
    film_name_en = models.CharField(max_length=200, help_text='Введите название фильма на английском', default="Unknown")
    film_description = models.TextField(max_length=99999, help_text='Введите описание фильма')
    film_release_date = models.DateField(default=True, help_text='Дата выпуска фильма')
    film_preview_image = models.ImageField(upload_to="main/static/img/", help_text='Превью для фильма')
    film_videofile = models.FileField(upload_to="main/static/films/", help_text='Собственно, сам фильм')
    film_kinopoisk_rating = models.FloatField(max_length=11, help_text='Оценка фильма на кинопоиске', default="0.0")
    film_user_rating = models.FloatField(max_length=11, help_text='Оценка фильма пользователями сайта', default="0.0")
    category = models.ForeignKey("Category", on_delete=models.PROTECT, null=True, help_text='Категория видеозаписи')
    type = models.ForeignKey("Type", on_delete=models.PROTECT, null=True, help_text='Тип видеозаписи')

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
