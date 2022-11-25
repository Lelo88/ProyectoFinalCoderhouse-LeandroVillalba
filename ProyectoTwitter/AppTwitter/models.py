from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = models.CharField(default='¡Bienvenido a Twitter!', max_length=100)
    
    def __str__(self):
        return f'{self.usuario.username}'

class Posteo(models.Model):
    hora_posteo = models.DateTimeField(default=timezone.now)
    contenido = models.TextField()
    usuario_posteo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posteos')
    
    class Meta:
        ordering=['-hora_posteo']
        
    def __str__(self):
        return self.contenido
    
    