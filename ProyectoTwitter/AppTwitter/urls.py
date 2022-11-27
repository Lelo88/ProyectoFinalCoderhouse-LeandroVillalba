from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import borrar_tweet, inicio, registro


urlpatterns = [
    path('', inicio, name = 'Inicio'),
    path('registro/', registro, name = 'Registro'),
    path('login/', LoginView.as_view(template_name='04_login.html'), name='Login'),
    path('login/', LogoutView.as_view(), name='Logout'),
    path('borrado/<int:id_posteo>', borrar_tweet, name='BorrarTweet')
]
