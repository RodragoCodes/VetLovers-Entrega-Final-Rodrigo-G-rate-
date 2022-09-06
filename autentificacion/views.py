
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from productos.forms import PostForm, UserEditForm, AvatarForm, UserRegisterForm
from productos.views import *
from django.contrib.auth.models import User
# Create your views here.

def Loginview(request):
    if request.method== "GET":
        Formulario= AuthenticationForm()
        return render(request, "autentificacion/login.html", {"form":Formulario})
    else:
        formulario = AuthenticationForm(request, data= request.POST)
        
        if formulario.is_valid():

            data= formulario.cleaned_data
            user= authenticate(username=data["username"], password= data["password"])

            if user is not None:
                login(request, user)
                return redirect('inicio')
        return redirect('no_valido')

def NoVaildo(request):
    return render (request, "autentificacion/formulario_no_valido.html")

def register_view(request):
    
    if request.method== "GET":
        #formulario= UserCreationForm()
        formulario=UserRegisterForm()
        return render(request, "autentificacion/register.html", {"form":formulario})
    
    else:
        #formulario= UserCreationForm(request.POST)
        formulario=UserRegisterForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            
            return redirect ('inicio')
        else:
            return render(request, "autentificacion/register.html", {"form":formulario})



@login_required
def editar_usuario (request):
    avatares= avatar.objects.filter(user=request.user.id)
    if request.method=="GET":
        form = UserEditForm(initial={"email": request.user.email})
        return render(request, 'autentificacion/Update_user.html', {"form":form, "url": avatares[0].imagen.url})
    else:
        form=UserEditForm(request.POST)

        if form.is_valid():
            data= form.cleaned_data

            usuario = request.user
            usuario.email= data["email"]
            usuario.password1= data["password1"]
            usuario.password2= data["password2"]

            usuario.save()
            return redirect('inicio')
        else:
            
            return render(request, 'autentificacion/Update_user.html', {"form":form})

@login_required
def agregar_avatar(request):
    avatares= avatar.objects.filter(user=request.user.id)
    if request.method== "GET":
        form= AvatarForm()
        context= {"form":form,"url": avatares[0].imagen.url}
        return render (request, "autentificacion/agregar_avatar.html",context)
    else:
        form= AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            
            data= form.cleaned_data
            usuario= User.objects.filter(username= request.user.username).first()
            avatars= avatar(user=usuario, imagen=data['imagen'])
            avatars.save()
            return redirect('mascotas')
        else:
            return render (request, "autentificacion/agregar_avatar.html",context)

#ChatInteractivo

def chat(request):
    current_user= get_object_or_404(User,pk = request.user.pk)
    posts= Post.objects.all()
    avatares= avatar.objects.filter(user=request.user.id)
    if request.method=="POST":
        form= PostForm(request.POST)
        if form.is_valid():
           post= form.save(commit=False)
           post.user = current_user
           post.save()
           return redirect ('chat')
    else:
        form= PostForm()
    return render (request, "autentificacion/chat.html", {'posts': posts, 'form': form, "url": avatares[0].imagen.url})


