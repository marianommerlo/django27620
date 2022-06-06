from dataclasses import fields
from http.client import HTTPResponse
from django.shortcuts import render
from .models import Curso, Estudiante, Profesor, Entregable, Avatar
from django.http import HttpResponse
from AppCoder.forms import CursoFormulario, ProfeFormulario, UserRegistrationForm, UserEditForm, AvatarForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# Create your views here.

def curso(self):
    curso= Curso(nombre="Curso de Django", comision= 4567)
    curso.save()
    texto= f"Curso: {curso.nombre} Comision: {curso.comision}"
    return HttpResponse(texto)

def inicio(request):
    avatar= Avatar.objects.filter(user= request.user)
    return render(request, 'AppCoder/inicio.html', {'url': avatar[0].avatar.url})

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiante_list.html')

#def cursos(request):
#    return render(request, 'AppCoder/cursos.html')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')

@login_required
def cursos(request):
    
    if request.method == 'POST':
        miFormulario= CursoFormulario(request.POST)
        
        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            curso= Curso(nombre=informacion['nombre'], comision= informacion['comision'])
            curso.save()
            return render(request, 'AppCoder/inicio.html')

    else:
        miFormulario= CursoFormulario()
    
    return render(request, 'AppCoder/cursos.html', {'formulario': miFormulario})
        #curso= Curso(nombre= request.POST['nombre'], comision= request.POST['comision'])
        #curso.save()
        #return render(request, 'AppCoder/inicio.html')

    #return render(request, 'AppCoder/cursosFormulario.html')

def busquedaComision(request):
    return render(request, 'AppCoder/busquedaComision.html')

def buscar(request):
    if request.GET['comision']:
        comision= request.GET['comision']
        cursos= Curso.objects.filter(comision= comision)

        return render(request, 'AppCoder/resultadosBusqueda.html', {'cursos': cursos, 'comision': comision})

    else:
        respuesta= "No se ingresó ninguna comision"
        return render(request, 'AppCoder/resultadosBusqueda.html', {'respuesta': respuesta})


    return render(request, 'AppCoder/cursosFormulario.html')

@login_required
def leerProfesores(request):
    profesores= Profesor.objects.all()
    contexto= {'profesores': profesores}
    
    return render(request, 'AppCoder/profesores.html', contexto)

@login_required
def eliminarProfesor(request, nombre):
    profesor= Profesor.objects.get(nombre= nombre)
    profesor.delete()
    
    profesores= Profesor.objects.all()
    contexto= {'profesores': profesores}
        
    return render(request, 'AppCoder/profesores.html', contexto)

#---------------------------------------------------------------------------------------------------------------

def editarProfesor(request, nombre):
    profesor= Profesor.objects.get(nombre= nombre) #recibo el nombre del profesor para modificar
    if request.method == 'POST':
        formulario= ProfeFormulario(request.POST)
        if formulario.is_valid():
            informacion= formulario.cleaned_data
            profesor.nombre= informacion['nombre']
            profesor.apellido= informacion['apellido']
            profesor.email= informacion['email']
            profesor.profesion= informacion['profesion']
            profesor.save()
            #Luego muestro la lista de profesores de nuevo
            profesores= Profesor.objects.all()
            contexto= {'profesores': profesores}
    
            return render(request, 'AppCoder/profesores.html', contexto)
    #Probar esto en otras vistas
    else:
        formulario= ProfeFormulario(initial={'nombre': profesor.nombre, 'apellido': profesor.apellido, 'email': profesor.email, 'profesion': profesor.profesion})
    
    return render(request, 'AppCoder/editarProfesor.html', {'formulario': formulario, 'nombre': nombre})


#CRUD DE ESTUDIANTES EN VISTAS-----------------------------------------------------------------

class EstudiantesList(LoginRequiredMixin, ListView):
    model= Estudiante
    template_name= 'AppCoder/estudiantes.html'


class EstudianteDetalle(LoginRequiredMixin, DetailView):
    model= Estudiante
    template_name= 'AppCoder/estudiante_detalle.html'

class EstudianteCreacion(CreateView): #esta view no funciona
    model= Estudiante
    success_url= reverse_lazy('estudiante_listar')
    fields= ['nombre', 'apellido', 'email']

class EstudianteEdicion(UpdateView):
    model= Estudiante
    success_url= reverse_lazy('estudiante_listar')
    fields= ['nombre', 'apellido', 'email']

class EstudianteEliminacion(DeleteView):
    model= Estudiante
    success_url= reverse_lazy('estudiante_listar')
    fields= ['nombre', 'apellido', 'email']

#LOGIN-------------------------------------------------------------------------------------------------------

def login_request(request):

    if request.method == "POST":
        formulario= AuthenticationForm(request, data= request.POST)

        if formulario.is_valid():
            usuario= formulario.cleaned_data.get('username')
            clave= formulario.cleaned_data.get('password')

            user= authenticate(username= usuario, password= clave)
            
            if user is not None:
                login(request, user)
                return render(request, 'AppCoder/inicio.html', {'mensaje': f'Bienvenido al Sistema {usuario}'})

            else:
                return render(request, 'AppCoder/login.html', {'formulario': formulario, 'mensaje': 'Usuario incorrecto, vuelva a loguearse'})
        
        else:
            return render(request, 'AppCoder/login.html', {'formulario': formulario, 'mensaje': 'Formulario inválido, vuelva a loguearse'})
    
    else:
        formulario= AuthenticationForm()
        return render(request, 'AppCoder/login.html', {'formulario': formulario})


def register(request):
    if request.method == 'POST':
        formulario = UserRegistrationForm(request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data.get('username')
            formulario.save()

            return render(request, 'AppCoder/inicio.html', {'mensaje': f'Usuario {username} creado satisfactoriamente'})

        else:
            return render(request, 'AppCoder/inicio.html', {'mensaje': 'No se pudo crear el usuario'})

    else:
        formulario= UserRegistrationForm()
        return render(request, 'AppCoder/register.html', {'formulario': formulario})

#EDICION DE PERFIL-------------------------------------------------------------------------------------------

@login_required
def editarPerfil(request):
    usuario= request.user

    if request.method == 'POST':
        formulario= UserEditForm(request.POST, instance= usuario)

        if formulario.is_valid():
            informacion= formulario.cleaned_data
            usuario.email= informacion['email']
            usuario.password1= informacion['password1']
            usuario.password2= informacion['password2']
            usuario.save()

            return render(request, 'AppCoder/inicio.html', {'usuario': usuario, 'mensaje': f'Perfil de {usuario} editado satisfactoriamente'})

    else:
        formulario= UserEditForm(instance= usuario)
        
    return render(request, 'AppCoder/editarPerfil.html', {'formulario': formulario, 'usuario': usuario.username})

#CRUD AVATARES-----------------------------------------------------------------------------------------------

def agregarAvatar(request):
    user= User.objects.get(username= request.user)
    if request.method == 'POST':
        formulario= AvatarForm(request.POST, request.FILES)
        
        if formulario.is_valid():
            avatarViejo= Avatar.objects.get(user= request.user)

            if(avatarViejo.avatar):
                avatarViejo.delete()
                
            avatar= Avatar(user= user, avatar=formulario.cleaned_data['avatar'])
            avatar.save()
            return render(request, 'AppCoder/inicio.html', {'usuario': user, 'mensaje': f'Avatar de {user} agregado satisfactoriamente'})

    else:
        formulario= AvatarForm()
    
    return render(request, 'AppCoder/agregarAvatar.html', {'formulario': formulario, 'usuario': user})

