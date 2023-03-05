from django.urls import include, re_path
from peliculas import views

urlpatterns=[
    re_path(r'^$',views.index,name='index')
]