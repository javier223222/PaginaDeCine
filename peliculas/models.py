import uuid
from django.db import models

# Create your models here.
class Genre(models.Model):
    name=models.CharField(max_length=64,help_text="pon el nombre del genro")
    def __str__(self) :
        return self.name
class Pelicula(models.Model):
    title=models.CharField(max_length=40)
    director=models.ForeignKey('Director',on_delete=models.SET_NULL,null=True)
    genero=models.ManyToManyField(Genre)
    time=models.IntegerField(help_text="ingrese la duracion de la pelicula")
    descripcion=models.TextField(max_length=100,help_text="ingrese descripcion de la pelicula")
    def __str__(self) :
        return self.title
     
# class PeliculaInstance(models.Model):
#     id=models.UUIDField(primary_key=True,default=uuid.uuid4,help_text="id para la pelicula")
#     pelicula=models.ForeignKey('Pelicula',on_delete=models.SET_NULL,null=True)
#     imprint=models.CharField(max_length=200)  
#     due_back=models.DateField(null=True,blank=True) 

class Director(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    date_of_birth=models.DateField(null=True,blank=True)
    date_of_death=models.DateField('Died',null=True,blank=True) 

    def __str__(self) :
        return '%s,%s' %(self.last_name,self.first_name)