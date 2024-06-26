# Generated by Django 5.0.3 on 2024-04-03 10:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_category_type_filmcard_category_filmcard_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmcard',
            name='film_kinopoisk_rating',
            field=models.FloatField(default='0.0', help_text='Оценка фильма на кинопоиске', max_length=11),
        ),
        migrations.AddField(
            model_name='filmcard',
            name='film_name_en',
            field=models.CharField(default='Unknown', help_text='Введите название фильма на английском', max_length=200),
        ),
        migrations.AddField(
            model_name='filmcard',
            name='film_user_rating',
            field=models.FloatField(default='0.0', help_text='Оценка фильма пользователями сайта', max_length=11),
        ),
        migrations.AlterField(
            model_name='filmcard',
            name='category',
            field=models.ForeignKey(help_text='Категория видеозаписи', null=True, on_delete=django.db.models.deletion.PROTECT, to='films.category'),
        ),
        migrations.AlterField(
            model_name='filmcard',
            name='film_preview_image',
            field=models.ImageField(help_text='Превью для фильма', upload_to='main/static/img/'),
        ),
        migrations.AlterField(
            model_name='filmcard',
            name='film_videofile',
            field=models.FileField(help_text='Собственно, сам фильм', upload_to='main/static/films/'),
        ),
        migrations.AlterField(
            model_name='filmcard',
            name='type',
            field=models.ForeignKey(help_text='Тип видеозаписи', null=True, on_delete=django.db.models.deletion.PROTECT, to='films.type'),
        ),
    ]
