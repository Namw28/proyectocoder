from django.shortcuts import render, redirect
from .models import *
from .forms import *





# vistas

def inicio(request):
    return render(request, 'tiposdecafe/inicio.html')

def granos(request):
    return render(request, 'tiposdecafe/granos.html')

def tostado(request):
    return render(request, 'tiposdecafe/tostado.html')


def origenes(request):
    return render(request, 'tiposdecafe/origenes.html')


def preparacion(request):
   return render(request, 'tiposdecafe/preparacion.html')

def tutores(request):
    return render(request, 'tiposdecafe/tutores.html')

def historia(request):
    return render(request, 'tiposdecafe/historia.html')




#guradar informacion 

def formulario_granos(request):
    if request.method == 'POST':
        form = GranoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(granos)
    else:
        form = GranoForm()

    return render(request, 'tiposdecafe/formulario_grano.html', {'form': form})


def formulario_origenes(request):
    if request.method == 'POST':
        form = OrigenesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(origenes)
    else:
        form = OrigenesForm()

    return render(request, 'tiposdecafe/formulario_origenes.html', {'form': form})

def formulario_tueste(request):
    if request.method == 'POST':
        form = TostadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(tostado)
    else:
        form = TostadoForm()

    return render(request, 'tiposdecafe/formulario_tueste.html', {'form': form})

def formulario_preparacion(request):
    if request.method == 'POST':
        form = PreparacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(preparacion)
    else:
        form = PreparacionForm()

    return render(request, 'tiposdecafe/formulario_preparacion.html', {'form': form})


#busqueda

def busqueda_grano(request):
    form = BusquedaForm(request.GET)
    resultados = []

    if form.is_valid():
        busqueda_grano = form.cleaned_data['busqueda_grano']
        resultados = Granos.objects.filter(nombre__icontains=busqueda_grano)

    return render(request, 'tiposdecafe/inicio.html', {'form': form, 'resultados': resultados})




