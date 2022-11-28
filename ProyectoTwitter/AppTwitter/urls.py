from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from .views import borrar_tweet, dejar_seguir, editar, inicio, perfil, registro, seguir_usuario



urlpatterns = [
    path('inicio/', inicio, name = 'Inicio'),
    path('registro/', registro, name = 'Registro'),
    path('', LoginView.as_view(template_name='04_login.html'), name='Login'),
    path('logout/', LogoutView.as_view(), name='Logout'),
    path('borrado/<int:id_posteo>', borrar_tweet, name='BorrarTweet'),
    path('perfil/<str:nombre_usuario>/', perfil, name='Perfil'),
    path('editar/',editar ,name='Editar'),
    path('seguir/<str:nombre_usuario>/', seguir_usuario, name='Seguir'),
    path('dejar-seguir/<str:username>/', dejar_seguir, name='DejarSeguir'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
