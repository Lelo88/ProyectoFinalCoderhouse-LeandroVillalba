from django import forms
from .models import Posteo, Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Registro(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email','password1', 'password2']
        
class FormularioPosteo(forms.ModelForm):
    contenido = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control w-100', 'id':'contentsBox',
                                                            'rows':'3', 'placeholder':'¿Qué está pasando?'}))
    
    class Meta:
        model = Posteo
        fields = ['contenido']
        
class EditarUsuario(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'username']
        
class EditarPerfil(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['biografia', 'imagen']