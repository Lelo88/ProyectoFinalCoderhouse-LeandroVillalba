from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from .views import borrar_tweet, inicio, registro



urlpatterns = [
    path('', inicio, name = 'Inicio'),
    path('registro/', registro, name = 'Registro'),
    path('login/', LoginView.as_view(template_name='04_login.html'), name='Login'),
    path('login/', LogoutView.as_view(), name='Logout'),
    path('borrado/<int:id_posteo>', borrar_tweet, name='BorrarTweet')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
