from django.urls import path
from productos.views import *
from autentificacion.views import *

urlpatterns = [
    path("home/", index, name= "inicio"),
    path('about/', about, name= "about"),
    path('precios/', precios, name= "precios"),
    path('clientes/', Clientes, name= "clientes"),
    path("mascotas/", Mascotas, name= "mascotas"),
    path('mascota/crear/', Crear_mascota, name= "mascotacrear"),
    path ('clientes/crear/', Crear_cliente, name= "clientecrear"),
    path('buscar/', buscar_mascota, name = 'buscarM'),
    path('resultadoM/', buscar, name="buscarmascota"),
    path('buscarC/',buscar_Cliente, name='buscarC'),
    path('resultadoC/', buscarC, name= "buscarcliente"),
        
    ]