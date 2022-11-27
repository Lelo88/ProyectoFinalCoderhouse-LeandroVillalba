from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    biografia = models.CharField(default='¡Bienvenido a Twitter!', max_length=100)
    imagen = models.ImageField(default='default.png')
    
    def __str__(self):
        return f'{self.usuario.username}'
    
    def seguir(self):
        id_usuarios = Relaciones.objects.filter(de_usuario=self.usuario).values_list('a_usuario_id', flat=True)

        return User.objects.filter(id__in=id_usuarios)
    
    def seguidores(self):
        id_usuarios = Relaciones.objects.filter(a_usuario=self.usuario).values_list('de_usuario_id', flat=True)

        return User.objects.filter(id__in=id_usuarios)
    
        
class Posteo(models.Model):
    hora_posteo = models.DateTimeField(default=timezone.now)
    contenido = models.TextField()
    usuario_posteo = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posteos')
    
    class Meta:
        ordering=['-hora_posteo']
        
    def __str__(self):
        return self.contenido
    
class Relaciones(models.Model):
    de_usuario = models.ForeignKey(User, related_name='relantioships', on_delete=models.CASCADE)
    a_usuario = models.ForeignKey(User, related_name='related_to', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.de_usuario} to {self.a_usuario}'
    
    