from django.db import models

# Create your models here.

class cliente (models.Model):
    nombre = models.CharField(max_length=50)
    direccion= models.CharField(max_length=50)
    ciudad= models.CharField(max_length=20)
    email= models.EmailField()
    cantidad_atenciones= models.IntegerField()
        

    def __str__(self):
        return f"{self.nombre}, {self.email}"

