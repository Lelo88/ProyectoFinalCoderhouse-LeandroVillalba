from django.shortcuts import render, redirect
from .models import Posteo, Usuario, Relaciones
from .forms import Registro, FormularioPosteo, EditarUsuario, EditarPerfil
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
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
        formulario_perfil = EditarPerfil(request.POST,request.FILES)
        if formulario_registro.is_valid() and formulario_perfil.is_valid():
            usuario = formulario_registro.save()
            perfil_usuario = formulario_perfil.save(commit=False)
            perfil_usuario.usuario = usuario
            perfil_usuario.save()
            return redirect('Inicio')
    
    else:
        formulario_registro = Registro()
        formulario_perfil = EditarPerfil()
        
    contexto = {'formulario_registro':formulario_registro,'formulario_perfil' :formulario_perfil}
    return render(request, '03_registro.html', contexto)

@login_required           
def borrar_tweet(request, id_posteo):
    posteo = Posteo.objects.get(id=id_posteo)
    posteo.delete()
    return redirect('Inicio')

@login_required
def perfil(request, nombre_usuario):
    nombre_usuario = User.objects.get(username=nombre_usuario)
    posteos =  Posteo.objects.filter(usuario_posteo=nombre_usuario)
    contexto = {'usuario': nombre_usuario, 'posteos': posteos}
    return render(request, '05_perfil.html', contexto)

@login_required
def editar(request):
    if request.method == 'POST':
        formulario_usuario = EditarUsuario(request.POST, instance = request.user)
        formulario_perfil = EditarPerfil(request.POST, request.FILES, instance = request.user.usuario)
        
        if formulario_usuario.is_valid() and formulario_perfil.is_valid():
            formulario_usuario.save()
            formulario_perfil.save()
            return redirect('Inicio')
    else:
        formulario_usuario = EditarUsuario(instance=request.user)
        formulario_perfil = EditarPerfil()
        
    contexto = {'formulario_usuario': formulario_usuario, 'formulario_perfil': formulario_perfil}
    
    return render(request, '06_editar.html', contexto)
        
@login_required
def seguir_usuario(request, nombre_usuario):
    usuario_actual = request.user
    a_usuario = User.objects.get(username = nombre_usuario)
    a_usuario_id = a_usuario
    rel = Relaciones(de_usuario = usuario_actual, a_usuario=a_usuario_id)
    rel.save()
    return redirect('Inicio')

@login_required
def dejar_seguir(request, username):
	current_user = request.user
	to_user = User.objects.get(username=username)
	a_usuario_id = to_user.id
	rel = Relaciones.objects.filter(de_usuario=current_user, a_usuario=a_usuario_id)
	rel.delete()
	return redirect('Inicio')

def about(request):
    return render(request, '07_aboutme.html')