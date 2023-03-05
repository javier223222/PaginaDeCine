from django.shortcuts import render
from .models import Director,Pelicula,Genre
# Create your views here.
def index(request):
    num_movie=Pelicula.objects.all().count()
    num_director=Director.objects.all().count()

    return render(
        request,
        'index.html',
        context={
        'peliculas':num_movie,
        'directores':num_director,
        'fulanito':"s"
       
        }
    )
