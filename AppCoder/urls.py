from django.urls import path
from .views import * #importa todo lo que hay adentro

urlpatterns = [
    path('', inicio),
    path('profesores/', profesores),
    path('estudiantes/', estudiantes),
    path('cursos/', cursos),
    path('entregables/', entregables),
    path('creaCurso/', curso),
]