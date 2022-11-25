from django.urls import path
from .views import inicio, registro

urlpatterns = [
    path('', inicio, name = 'Inicio'),
    path('registro/', registro, name = 'Registro')
]
