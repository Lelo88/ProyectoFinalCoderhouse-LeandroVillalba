from django.shortcuts import render, redirect
from .models import Posteo, Usuario
from .forms import Registro, FormularioPosteo

# Create your views here.
def inicio(request):
    posteos = Posteo.objects.all()
    if request.method == 'POST':
        formulario_posteo = FormularioPosteo(request.POST)
        if formulario_posteo.is_valid():
            posteo = formulario_posteo.save(commit=False)
            posteo.usuario_posteo = request.user
            posteo.save()
            return redirect('Inicio')
    else:
        formulario_posteo = FormularioPosteo()
    
    contexto = {'posteos': posteos, 'formulario': formulario_posteo}
    return render(request, '01_inicio-twitter.html', contexto)

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
            