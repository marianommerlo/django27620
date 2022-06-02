from django.urls import path
from .views import * #importa todo lo que hay adentro

urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('profesores/', profesores, name= 'profesores'),
    path('estudiantes/', estudiantes, name= 'estudiantes'),
    path('cursos/', cursos, name= 'cursos'),
    path('entregables/', entregables, name= 'entregables'),
    #path('cursosFormulario/', cursosFormulario, name= 'cursosFormulario'),
    #path('creaCurso/', curso),
    path('busquedaComision/', busquedaComision, name= 'busquedaComision'),
    path('buscar/', buscar, name= 'buscar'),
]