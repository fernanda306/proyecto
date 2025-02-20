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
<<<<<<< HEAD
from django.urls import path
from django.urls import path, include

from django.urls import path
=======
from django.conf import settings
from django.conf.urls.static import static



>>>>>>> a77b5d777e7bf2b608827958df88ac334517cce9



urlpatterns = [

    path('admin/', admin.site.urls),
    # path('', include('main.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('',views.home,name='home'),
<<<<<<< HEAD

    path('carta',views.carta,name='carta'),
=======
    # path('buzon',views.buzon,name='buzon'),
    # path('carta',views.carta,name='carta'),
>>>>>>> a77b5d777e7bf2b608827958df88ac334517cce9
    path('galeria',views.galeria,name='galeria'),
    path('mapa',views.mapa,name='mapa'),
    path('mision',views.mision,name='mision'),
    path('registrarse',views.registrarse,name='registrarse'),
    path('vision',views.vision,name='vision'),
    path('fotos',views.fotos,name='fotos'),
    path('videos',views.videos,name='videos'),
    path('login',views.login,name='login'),
    
    path('domicilios',views.domicilios,name='domicilios'),
     path('reservas',views.reservas,name='reservas'),
    path('productos/',views.productos, name='productos'),
    path('buzon/', views.buzon, name='buzon'),
     

    

<<<<<<< HEAD
    path('buzon/', views.buzon, name='buzon'),
    path('gracias/', views.gracias, name='gracias'),

    
]

=======
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
>>>>>>> a77b5d777e7bf2b608827958df88ac334517cce9

