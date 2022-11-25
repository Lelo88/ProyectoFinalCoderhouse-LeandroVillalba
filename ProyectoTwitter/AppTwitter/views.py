from django.shortcuts import render
from .models import Posteo, Usuario

# Create your views here.
def inicio(request):
    posteos = Posteo.objects.all()
    return render(request, '01_inicio-twitter.html', {'posteos': posteos})