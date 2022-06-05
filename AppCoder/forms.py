from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CursoFormulario(forms.Form):
    #especificamos los campos del formulario
    nombre= forms.CharField(max_length=50)
    comision= forms.IntegerField()

class ProfeFormulario(forms.Form):
    nombre= forms.CharField(max_length=50)
    apellido= forms.CharField(max_length=50)
    email= forms.EmailField()
    profesion= forms.CharField(max_length=50)

class UserRegistrationForm(UserCreationForm):
    #especificamos los campos del formulario
    email= forms.EmailField(required= True)
    password1= forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2= forms.CharField(label= 'Confirmar Contraseña', widget= forms.PasswordInput)

    class Meta:
        model= User
        fields= ['username', 'email', 'password1', 'password2']
        help_texts= {k:"" for k in fields} #Para que no se vean las ayudas para crear contraseña

