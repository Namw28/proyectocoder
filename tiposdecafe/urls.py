
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


app_name = 'tiposdecafe'

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
    path('busqueda_grano', busqueda_grano, name ='busqueda_grano'),
   # path('login', inicio_sesion, name='inicio_sesion'),
    path('inicio_sesion/', login_request, name='inicio_sesion'),
    path('registrarse/', registrarse, name='registrarse'),
    path('logout/', logout_request, name='logout'),
    path('editar_perfil/', PerfilUsuarioUpdateView.as_view(), name='editar_perfil'),
    path('aboutme/', aboutme, name='aboutme')
 


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
