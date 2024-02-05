
from django import forms
from .models import *

class GranoForm(forms.ModelForm):
    class Meta:
        model = Granos
        fields = ['nombre', 'region_produccion', 'tipo', 'altura_cultivo', 'tipo_semillas', 'tiempo_cosecha' ]



class OrigenesForm(forms.ModelForm):
    class Meta:
        model = Origenes
        fields= ['pais', 'region']


class TostadoForm(forms.ModelForm):
    class Meta:
        model = Tostado
        fields= ['nombre', 'nivel']


class PreparacionForm(forms.ModelForm):
    class Meta:
        model = Preparacion
        fields= ['nombre', 'metodo','tiempo', 'temperatura']        


class BusquedaForm(forms.Form):
    busqueda_grano = forms.CharField(label='busqueda_grano', max_length=100)



class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'edad', 'email', 'avatar', 'password1', 'password2']


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'avatar']


class SemillaForm(forms.ModelForm):
    class Meta:
        model = Granos
        fields = '__all__'