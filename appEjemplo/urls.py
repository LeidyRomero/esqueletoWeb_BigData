from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('1', views.primerPunto, name='primero'),
    path('2', views.segundoPunto, name='segundo'),
    path('3', views.tercerPunto, name='tercero'),
    path('4', views.cuartoPunto, name='cuarto'),
    path('5', views.quintoPunto, name='quinto'),
    path('6', views.sextoPunto, name='sexto'),
    path('7', views.septimoPunto, name='septimo'),
    path('8', views.octavoPunto, name='octavo'),
    path('peticion', views.tercerPunto, name='tercero'),
    path('texto', views.texto, name='tercero'),
    path('varias_respuestas', views.varias, name='tercero'),
]