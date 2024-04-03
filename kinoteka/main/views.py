from django.shortcuts import render
from films.models import FilmCard


def index(request):
    films = FilmCard.objects.all()
    context = {'films': films}
    for n in range(len(films)):
        films[n].film_preview_image = str(films[n].film_preview_image).split('main/')[1]
    return render(request, 'index.html', context)
