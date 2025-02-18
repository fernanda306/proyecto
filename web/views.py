from django.shortcuts import render

from django.shortcuts import render, redirect 
from django.contrib.auth.models import User 
from django.contrib import messages 
from django.contrib.auth import authenticate, login as auth_login


# Create your views here.
def home(request):
    return render (request, 'home.html')



def buzon(request):
    return render (request,'buzon.html')




def carta(request):
    return render (request, 'carta.html')



def galeria(request):
    return render (request, 'galeria.html')

def mapa(request):
    return render (request, 'mapa.html')

def mision(request):
    return render (request, 'mision.html')

def registrarse(request): 
    if request.method == 'POST': 
        username = request.POST['username'] 
        email = request.POST['email'] 
        password = request.POST['password'] 
        confirm_password = request.POST.get('confirm_password') 

        if password != confirm_password: 
            messages.error(request, 'Las contraseñas no coinciden.') 
        elif User.objects.filter(email=email).exists(): 
            messages.error(request, 'El correo ya está registrado.') 
        elif User.objects.filter(username=username).exists(): 
            messages.error(request, 'El nombre de usuario ya está en uso.') 
        else: 
            user = User.objects.create_user(username=username, email= email, password=password) 
            user = authenticate(request, username=username, password=password) 
            if user is not None: 
                auth_login(request, user) 
                messages.success(request, "¡Registro exitoso!") 
                return redirect('login')


    return render(request, 'registrarse.html')

def vision(request):
    return render (request, 'vision.html')


def fotos(request):
    return render (request, 'fotos.html')


def videos(request):
    return render (request, 'videos.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not username or not password:
            messages.error(request, 'Por favor, ingresa ambos campos.')
            return render(request, 'login.html')

        try:
            user = User.objects.get(username=username)  # Renombré User a user
        except User.DoesNotExist:  # Corregí el error tipográfico aquí
            messages.error(request, 'El usuario no existe.')
            return render(request, 'login.html')

        # Intentar autenticar al usuario
        authenticated_user = authenticate(request, username=username, password=password)
        if authenticated_user is not None:
            auth_login(request, authenticated_user)
            return redirect('home')
        else:
            messages.error(request, "Contraseña incorrecta.")
    
    return render(request, 'login.html')

            

def reservas(request):
    return render (request, 'reservas.html')

def domicilios(request):
    return render (request, 'domicilios.html')