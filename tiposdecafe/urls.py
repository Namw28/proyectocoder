
from django.urls import path
from .views import *


urlpatterns = [


    path('inicio/', inicio, name='inicio'),
    path('granos/', granos, name='granos'),
    path('origenes/', origenes, name='origenes'),
    path('tostado/', tostado, name='tostado'),
    path('preparacion/', preparacion, name='preparacion'),
    path('formulario_grano/', formulario_granos, name='formulario_grano'),
    path('formulario_origenes/', formulario_origenes, name='formulario_origenes'),
    path('formulario_tueste/', formulario_tueste, name='formulario_tueste'),
    path('formulario_preparacion/', formulario_preparacion, name='formulario_preparacion'),
    path('tutores',tutores, name='tutores'),
    path('historia',historia, name='historia'),
    path('busqueda_grano', busqueda_grano, name ='busqueda_grano')




]
