from django.shortcuts import render
from .models import Posteo, Usuario
from .forms import Registro

# Create your views here.
def inicio(request):
    posteos = Posteo.objects.all()
    return render(request, '01_inicio-twitter.html', {'posteos': posteos})

