from django.urls import path
from .views import * #importa todo lo que hay adentro

urlpatterns = [
    path('', inicio, name= 'inicio'),
    path('profesores/', leerProfesores, name= 'profesores'),
    path('estudiantes/', estudiantes, name= 'estudiantes'),
    path('cursos/', cursos, name= 'cursos'),
    path('entregables/', entregables, name= 'entregables'),
    #path('cursosFormulario/', cursosFormulario, name= 'cursosFormulario'),
    #path('creaCurso/', curso),
    path('busquedaComision/', busquedaComision, name= 'busquedaComision'),
    path('buscar/', buscar, name= 'buscar'),
    path('eliminarProfesor/<nombre>', eliminarProfesor, name= 'eliminarProfesor'),
    path('editarProfesor/<nombre>', editarProfesor, name= 'editarProfesor'),
    #pk es el id de django
    path('estudiante/list/', EstudiantesList.as_view(), name= 'estudiante_listar'),
    path('estudiante/<pk>/', EstudianteDetalle.as_view(), name= 'estudiante_detalle'),#pk es el id
    path('estudiante/nuevo/', EstudianteCreacion.as_view(), name= 'estudiante_crear'),
    path('estudiante/editar/<pk>/', EstudianteEdicion.as_view(), name= 'estudiante_editar'),
    path('estudiante/borrar/<pk>/', EstudianteEliminacion.as_view(), name= 'estudiante_borrar'),

]