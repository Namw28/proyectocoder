from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Granos, CustomUser
from .forms import GranoForm, OrigenesForm, TostadoForm, PreparacionForm, UserRegisterForm, CustomUserForm, SemillaForm

# Vistas

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



def historia(request):
    return render(request, 'tiposdecafe/historia.html')

def aboutme(request):
    return render(request, 'tiposdecafe/aboutme.html')

# Guardar información
def guardar_informacion(request, form_class, template_name, redirect_url):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = form_class()

    return render(request, template_name, {'form': form})

@login_required(login_url='tiposdecafe:inicio_sesion')
def formulario_granos(request):
    return guardar_informacion(request, GranoForm, 'tiposdecafe/formulario_grano.html', 'tiposdecafe:granos')

@login_required(login_url='tiposdecafe:inicio_sesion')
def formulario_origenes(request):
    return guardar_informacion(request, OrigenesForm, 'tiposdecafe/formulario_origenes.html', 'tiposdecafe:origenes')

@login_required
def formulario_tueste(request):
    return guardar_informacion(request, TostadoForm, 'tiposdecafe/formulario_tueste.html', 'tiposdecafe:tostado')

@login_required(login_url='tiposdecafe:inicio_sesion')
def formulario_preparacion(request):
    return guardar_informacion(request, PreparacionForm, 'tiposdecafe/formulario_preparacion.html', 'tiposdecafe:preparacion')

# Vista de inicio de sesión
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, '¡Inicio de sesión exitoso!')

            return redirect('tiposdecafe:inicio')
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')

    else:


        form = AuthenticationForm()

    return render(request, 'registro/inicio_sesion.html', {'form': form})



# Vista de registro

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

    return render(request, 'registro/registrarse.html', {'form': form})

# Vista de cierre de sesión
def logout_request(request):
    logout(request)
    messages.success(request, '¡Has cerrado sesión exitosamente!')
    return redirect('tiposdecafe:inicio')


# Vista de edición de perfil de usuario
@method_decorator(login_required, name='dispatch')
class PerfilUsuarioUpdateView(UpdateView):
    model = CustomUser
    form_class = CustomUserForm  
    template_name = 'tiposdecafe/perfil_usuario_editar.html'

    def get_object(self, queryset=None):
        return self.request.user
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  
        return context

    def form_valid(self, form):
        messages.success(self.request, '¡Perfil actualizado exitosamente!')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('tiposdecafe:inicio')


# Búsqueda de granos
def buscar_granos(request):
    search_text = request.GET.get('search_text', '')
    granos = Granos.objects.filter(
        nombre__icontains=search_text
    ) | Granos.objects.filter(
        region_produccion__icontains=search_text
    )
    data = {
        'granos': granos
    }
    html = render_to_string('tiposdecafe/granos_table_body.html', data)
    return JsonResponse({'html': html})

# Vista para ver todas las semillas
def ver_semillas(request):
    semillas = Granos.objects.all()
    return render(request, 'tiposdecafe/ver_semillas.html', {'semillas': semillas})

# Vista para editar una semilla
@login_required(login_url='tiposdecafe:inicio_sesion')
def editar_semilla(request, grano_id):
    semilla = get_object_or_404(Granos, id=grano_id)
    if request.method == 'POST':

        form = SemillaForm(request.POST, instance=semilla)
        if form.is_valid():
            form.save()
            return redirect('tiposdecafe:ver_semillas')
    else:
        form = SemillaForm(instance=semilla)

    return render(request, 'tiposdecafe/editar_grano.html', {'form': form})
