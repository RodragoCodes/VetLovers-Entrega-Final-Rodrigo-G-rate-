

from django.forms import Form,CharField,IntegerField,EmailField, PasswordInput, EmailInput, ImageField, Textarea
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from autentificacion.models import *


from autentificacion.models import Post
#formularios de busquedas

class Busqueda_mascotas(Form):
    nombre_mascota= CharField(max_length=150)

#formularios de Creacion

class MascotaFormularioCrea(Form):
    nombre_mascota= CharField()
    tipo= CharField()
    genero= CharField()
    edad= IntegerField()
    cantidad_consultas= IntegerField()

class ClienteFormularioCrea(Form):

    nombre= CharField()
    direccion= CharField()
    ciudad= CharField()
    email= EmailField()
    cantidad_atenciones= IntegerField()

class UserEditForm(UserCreationForm):
    email= EmailField(label='Modificar email', widget= EmailInput)
    password1= CharField(label='Nueva contraseña', widget=PasswordInput)
    password2= CharField(label="repetir Nueva contraseña", widget= PasswordInput)

    class Meta:
        model= User
        fields= ["email", "password1", "password2"]
        help_text= {"email":"", "password1":"", "password2":""}

class AvatarForm(Form):
    imagen= ImageField()

class UserRegisterForm (UserCreationForm):
    username= CharField(label='Nombre de Usuario')
    email= EmailField(label='Email', widget= EmailInput)
    password1= CharField(label='Contraseña', widget=PasswordInput)
    password2= CharField(label="Repetir contraseña", widget= PasswordInput)
    imagen= ImageField(label="Subir Imagen de Perfil")

    class Meta:
        model= User
        fields= ["username","email", "password1", "password2","imagen"]
        help_text= {"username":"","email":"", "password1":"", "password2":"","imagen":""}

class PostForm(forms.ModelForm):
    content= forms.CharField(label='', widget= Textarea )
    
    
    
    class Meta:
        model = Post
        fields = ["content"]
