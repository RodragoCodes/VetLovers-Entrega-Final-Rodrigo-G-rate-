
from django.shortcuts import render, redirect
from productos.models import *
from BDDs.models import *
from productos.forms import ClienteFormularioCrea, MascotaFormularioCrea
from autentificacion.models import *


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    
    return render(request, "productos/index.html")

def about(request):
    return render(request, "productos/about.html")


def precios(request):
    avatares= avatar.objects.filter(user=request.user.id)
    lista_precios= procedimientos.objects.all
    return render(request, "productos/price.html", {"procedimientos": lista_precios, "url":avatares[0].imagen.url})

@login_required
def Clientes(request):
    avatares= avatar.objects.filter(user=request.user.id)
    lista_clientes = cliente.objects.all
    return render(request, "BDDs/Clientes.html",{"clientes": lista_clientes, "url":avatares[0].imagen.url} )

@login_required
def Mascotas(request):
    avatares= avatar.objects.filter(user=request.user.id)
    lista_mascotas = mascotas.objects.all     
    return render(request, "productos/mascotas.html", {"mascotas": lista_mascotas, "url":avatares[0].imagen.url})

def Crear_mascota(request):
    if request.method == "GET":
        formulario= MascotaFormularioCrea()
        return render(request, "productos/Crear_mascota.html", {"formulario" : formulario})
    else:  
        formulario = MascotaFormularioCrea(request.POST)
        Lista_mascota= mascotas.objects.all
        if formulario.is_valid():
            datos= formulario.cleaned_data
            nombre_mascota= datos["nombre_mascota"]
            tipo= datos["tipo"]
            genero= datos["genero"]
            edad= datos["edad"]
            cantidad_consultas= datos["cantidad_consultas"]
            C= mascotas(nombre_mascota=nombre_mascota,tipo=tipo,genero=genero, edad=edad,cantidad_consultas=cantidad_consultas)
            C.save()
            return render(request, "productos/index.html")
        else:
            return render (request, "productos/mascotas.html",{"formulario":Lista_mascota})


def Crear_cliente(request):
    if request.method == "GET":
        formulario= ClienteFormularioCrea()
        return render(request, "BDDs/Crear_Clientes.html", {"formulario" : formulario})
    else:  
        formulario = ClienteFormularioCrea(request.POST)

        if formulario.is_valid():
            datos= formulario.cleaned_data
            nombre= datos["nombre"]
            email= datos["email"]
            direccion= datos["direccion"]
            ciudad= datos["ciudad"]
            cantidad_atenciones= datos["cantidad_atenciones"]
            C= cliente(nombre=nombre, direccion=direccion,ciudad=ciudad, email=email, cantidad_atenciones=cantidad_atenciones)
            C.save()
            return render(request, "productos/index.html")
        else:
            return render (request, "BDDS/Clientes.html")

def buscar_mascota(request):
    return render (request, "productos/Busca_mascota.html")

def buscar(request):
    nombre_mascota = request.GET.get("Mascota", None)

    if not  nombre_mascota:
        return redirect('mascotas')
    
    mascota_lista= mascotas.objects.filter(nombre_mascota__icontains= nombre_mascota)
    return render(request, "productos/result_busq_mascota.html", {"Mascota" : mascota_lista})


def buscar_Cliente(request):
    return render (request, "BDDs/Busca_cliente.html")

def buscarC(request):
    nombre = request.GET.get("Cliente", None)

    if not  nombre:
        return redirect('clientes')
    
    cliente_lista= cliente.objects.filter(nombre__icontains= nombre)
    return render(request, "BDDs/result_busq_cliente.html", {"Cliente" : cliente_lista})



