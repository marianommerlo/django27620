from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Curso(models.Model):#curso hereda de Model
    nombre= models.CharField(max_length=50)
    comision= models.IntegerField()

    def __str__(self):
        return self.nombre +" "+ str(self.comision)

class Estudiante(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()

    def __str__(self):
        return self.nombre +" "+ self.apellido

class Profesor(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    email= models.EmailField()
    profesion= models.CharField(max_length=50)

    def __str__(self):
        return self.nombre +" "+ self.apellido

class Entregable(models.Model):
    nombre= models.CharField(max_length=50)
    fecha_entrega= models.DateField()
    entregado= models.BooleanField(default=False, blank=True)

class Avatar(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)#Borro usuario, borra avatar
    avatar= models.ImageField(upload_to='avatar', blank=True, null=True)#Puedo dejarlo en blanco
                                    #donde subo la imagen


