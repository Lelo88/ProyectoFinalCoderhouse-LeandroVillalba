from django.shortcuts import render, redirect
from .models import Posteo, Usuario
from .forms import Registro

# Create your views here.
def inicio(request):
    posteos = Posteo.objects.all()
    return render(request, '01_inicio-twitter.html', {'posteos': posteos})

def registro(request):
    if request.method == 'POST':
        formulario_registro = Registro(request.POST)
        if formulario_registro.is_valid():
            formulario_registro.save()
            
            return redirect('Inicio')
    
    else:
        formulario_registro = Registro()
        
    contexto = {'formulario':formulario_registro}
    return render(request, '03_registro.html', contexto)
            