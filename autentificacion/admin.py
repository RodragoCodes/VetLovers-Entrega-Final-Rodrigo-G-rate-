from atexit import register
from django.contrib import admin
from autentificacion.models import Post, Profile, avatar
# Register your models here.

admin.site.register(avatar)
admin.site.register(Profile)
admin.site.register(Post)