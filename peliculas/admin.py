from django.contrib import admin
from .models import Genre,Pelicula,Director
# Register your models here.
admin.site.register(Director)
admin.site.register(Pelicula)
admin.site.register(Genre)