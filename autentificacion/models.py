

from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen= models.ImageField(upload_to= "avatares", null=True, blank= True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image= models.ImageField(default= 'Acces.jpg')
    def __str__(self):
        return f'Perfil de {self.user.username}'

class Post(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    timestamp= models.DateField(default=timezone.now)
    content= models.TextField()
    class Meta:
        ordering= ['-timestamp']

    def __str__(self):
        return f'{self.user.username} : {self.content}'