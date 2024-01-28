from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required


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

def aboutme(request):
    return render(request, 'tiposdecafe/aboutme.html')




#guradar informacion 

def formulario_granos(request):
    if request.method == 'POST':
        form = GranoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse(granos))
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


#vista login

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                messages.success(request, '¡Inicio de sesión exitoso!')
                print(f'Usuario autenticado: {user.username}')
                return redirect('tiposdecafe:inicio')
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
                return render(request, "tiposdecafe/inicio.html", {"mensaje": "Usuario no encontrado"})
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
            print(f'Formulario no válido: {form.errors}')
            return render(request, "tiposdecafe/inicio.html", {"mensaje": "Formulario erroneo"})

    form = AuthenticationForm()
    return render(request, "registro/inicio_sesion.html", {"form": form})

# vista de registro

def registrarse(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            messages.success(request, f'¡Usuario creado! Ahora puedes iniciar sesión.')
            return redirect('tiposdecafe:inicio')
        
    else:
        form = UserRegisterForm()

    return render(request, "registro/registrarse.html", {"form": form})

#vista de loguot

def logout_request(request):
    logout(request)
    messages.success(request, '¡Has cerrado sesión exitosamente!')
    return redirect('tiposdecafe:inicio')


@method_decorator(login_required, name='dispatch')
class PerfilUsuarioUpdateView(UpdateView):
    model = CustomUser
    fields = ['nombre', 'apellido', 'edad', 'avatar']
    template_name = 'tiposdecafe/perfil_usuario_editar.html'  # Crea esta plantilla

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('tiposdecafe:inicio')


#ediar perfil de usuario
    
def editar_perfil(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cambios guardados exitosamente.')
            print(f'Datos del formulario guardados: {form.cleaned_data}')
            return redirect('donde_quieres_redirigir')  # Ajusta esto según tu aplicación
        else:
            messages.error(request, 'Error al guardar los cambios. Por favor, revisa los datos ingresados.')
            print(f'Formulario no válido: {form.errors}')

    else:
        form = CustomUserForm(instance=request.user)

    return render(request, 'tiposdecafe/editar_perfil.html', {'form': form})

def busqueda_grano(request):
    form = BusquedaForm(request.GET)
    resultados = []

    if form.is_valid():
        busqueda_grano = form.cleaned_data['busqueda_grano']
        resultados = Granos.objects.filter(nombre__icontains=busqueda_grano)

    return render(request, 'tiposdecafe/inicio.html', {'form': form, 'resultados': resultados})




