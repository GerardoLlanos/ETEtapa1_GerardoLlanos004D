from django.shortcuts import render, redirect
from .models import Colaborador
from .forms import ColaboradorForm

# Create your views here.

def home(request):

    return render(request, 'home.html')

def Ver(request):
    vercolaboradores = Colaborador.objects.all()

    return render(request, 'core/ver.html', context={'vercolaboradores':vercolaboradores})

def form_colaborador(request):
    if request.method == 'POST': 
        colaboradores_form = ColaboradorForm(request.POST, files=request.FILES)
        if colaboradores_form.is_valid():
            colaboradores_form.save()        #similar al insert de un modelo relacional 
            return redirect('home')
    else: 
        colaboradores_form = ColaboradorForm()
    return render(request, 'core/form_colaboradores.html', {'colaboradores_form': colaboradores_form})


def form_mod_colaborador(request, id):
    colaborador = Colaborador.objects.get(rutColaborador=id)

    datos ={
        'form': ColaboradorForm(instance=colaborador)
    }
    
    if request.method == 'POST': 
        formulario = ColaboradorForm(data=request.POST, instance = colaborador, files=request.FILES)
        if formulario.is_valid: 
            formulario.save()
            return redirect('ver')
    return render(request, 'core/form_mod_colaborador.html', datos)

def form_del_colaborador(request, id):
    colaborador = Colaborador.objects.get(rutColaborador=id)
    colaborador.delete()
    return redirect('ver')