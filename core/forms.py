from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Paises, Colaborador            


class ColaboradorForm(forms.ModelForm):
    rutColaborador = forms.CharField(label='Rut de Colaborador',max_length=10, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))  
    imagen = forms.ImageField(label='Fotografía', widget=forms.FileInput(
        attrs={
            'class':'form-control' 
        }
    )) 
    nombreCompleto = forms.CharField(label='Nombre Completo',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    )) 
    telefono = forms.CharField(label='Teléfono',max_length=12, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    )) 
    direccion = forms.CharField(label='Dirección',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    )) 
    email = forms.CharField(label='Email',max_length=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    )) 
    pais = forms.ModelChoiceField(queryset=Paises.objects.all(), label='País',widget=forms.Select(
        attrs={
            'class':'form-control'
        }
    ))
    contraseña = forms.CharField(label='Contraseña',max_length=200, widget=forms.PasswordInput(
        attrs={
            'class':'form-control'
        }
    )) 



    class Meta: 
        model = Colaborador
        fields = ['rutColaborador', 'imagen', 'nombreCompleto', 'telefono', 'direccion', 'email', 'pais', 'contraseña']
    
     