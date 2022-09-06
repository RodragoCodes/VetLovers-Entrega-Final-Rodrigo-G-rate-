from django.urls import path, include
from autentificacion.views import *
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings
# paths

urlpatterns = [
    path('login/', Loginview, name= 'login'),
    path('error/', NoVaildo, name= 'no_valido'),
    path('register/', register_view, name= 'register'),
    path('Logout/', LogoutView.as_view(template_name='autentificacion/logout.html'), name= 'logout'),
    path('edit/', editar_usuario, name= 'EditarUsuario'),
    path('avatar/', agregar_avatar, name= 'AgregarAvatar'),
    path('chat/', chat, name='chat'),
            
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)