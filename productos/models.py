from django.db import models

# Create your models here.
class procedimientos(models.Model):

    nombre = models.CharField(max_length=300)
    descripcion= models.CharField(max_length=9000)
    precio= models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.precio}"

class mascotas (models.Model):

    nombre_mascota = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20)
    genero= models.CharField(max_length=20)
    edad= models.IntegerField()
    cantidad_consultas= models.IntegerField(default=1)

    def __str__(self):
        return f"{self.nombre_mascota},{self.tipo}"
