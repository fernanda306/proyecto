"""
URL configuration for sitio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web import views 
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

# from django.urls import path  # This line is already imported above
# from .views import views  # This line is incorrect and should be removed


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('galeria', views.galeria, name='galeria'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('registrarse', views.registrarse, name='registrarse'),
    path('fotos', views.fotos, name='fotos'),
    path('videos', views.videos, name='videos'),
    path('login', views.login, name='login'),
    path('domicilios', views.domicilios, name='domicilios'),
    path('productos/', views.productos, name='productos'),
    path('sugerencia', views.sugerencias, name='sugerencia'),
    path('gracias/', views.gracias, name='gracias'),
    path('logout/', views.cerrar_sesion, name='logout'),

    path('resetear/', views.resetear, name='resetear'),
    path("cambiar/<uidb64>/<token>/", views.cambiar, name="cambiar"),
    path("cambiada", views.cambiada, name="cambiada"),
      path('perfil/', views.perfil, name='perfil'),



# Agrega estas líneas a tus urlpatterns existentes
path('reservacion/', views.reservacion, name='reservacion'),
path('reservacion/exitosa/', views.reservacion_exitosa, name='reservacion_exitosa'),






] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)










