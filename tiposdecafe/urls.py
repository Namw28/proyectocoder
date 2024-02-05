
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
    path('historia/', historia, name='historia'),
    path('inicio_sesion/', login_request, name='inicio_sesion'),
    path('registrarse/', registrarse, name='registrarse'),
    path('logout/', logout_request, name='logout'),
    path('editar_perfil/', PerfilUsuarioUpdateView.as_view(), name='editar_perfil'),
    path('aboutme/', aboutme, name='aboutme'),
    path('ver_semillas/', ver_semillas, name='ver_semillas'),  
    path('editar_grano/<int:grano_id>/', editar_semilla, name='editar_grano'), 
    path('buscar_granos/', buscar_granos, name='buscar_granos'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    