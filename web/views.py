import logging
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from .forms import SugerenciaForm
from .models import Producto, Reservacion
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib.auth.tokens import default_token_generator 
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from django.utils.encoding import force_bytes, force_str
from django.urls import reverse
from django.urls import path
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ReservacionForm


from django.shortcuts import render
from django.contrib.auth.decorators import login_required




logger = logging.getLogger(__name__)

# Create your views here.
def home(request):
    return render (request, 'home.html')







def galeria(request):
    return render (request, 'galeria.html')



def nosotros(request):
    return render (request, 'nosotros.html')




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





def domicilios(request):
    return render (request, 'domicilios.html')


def gracias(request):
    return render (request, 'gracias.html')



def sugerencias (request):
    if request.method == 'POST':
        form = SugerenciaForm(request.POST)
        if form.is_valid():
            form.save()
            form.send_mail()
            return redirect('sugerencia')
    else:
        form = SugerenciaForm()

    return render(request, 'sugerencia.html', {'form': form})





def reservacion(request):
    if request.method == 'POST':
        form = ReservacionForm(request.POST)
        if form.is_valid():
            form.save()
            form.send_mail()
            return redirect('reservacion_exitosa')
    else:
        form = ReservacionForm()
    
    return render(request, 'reservacion.html', {'form': form})

def reservacion_exitosa(request):
    return render(request, 'reservacion_exitosa.html')





def productos(request):
    productos = Producto.objects.all()  # Obtiene todos los productos
    return render(request, 'productos.html', {'productos': productos})



def cerrar_sesion(request):
    logout(request)
    # messages.success(request, "¡Hasta luego!")

    return redirect('home')






# Añade estas nuevas vistas
def resetear(request):
    if request.method == 'POST':
        email = request.POST['email']
        user = User.objects.filter(email=email).first()
        if user:
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            enlace = request.build_absolute_uri(reverse("cambiar", kwargs={'uidb64': uid, 'token': token}))
            send_mail(
               "restablecimiento de contraseña",
               f"Da clic en el siguiente enlace para restablecer tu contraseña: {enlace}",
               "fernandamanriquefernandez724@gmail.com",
               [email],
               fail_silently=False,
            )
            messages.error(request, "Se ha enviado un enlace de restablecimiento a su correo.")
            return redirect('resetear')
        else:
            messages.error(request, "No se encontró un usuario con ese correo.")
            return redirect('resetear')
    return render(request, 'resetear.html')

def cambiar(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
        
        if user is not None and default_token_generator.check_token(user, token):
            if request.method == "POST":
                nueva_contraseña = request.POST['password']
                user.set_password(nueva_contraseña)
                user.save()
                return redirect('cambiada')
            
            return render(request, 'cambiar.html')
        else:
            return redirect("login")
            
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        return redirect("login")

def cambiada(request):
    return render(request, 'cambiada.html')





        





@login_required  # Asegura que solo usuarios conectados puedan ver esta página
def perfil(request):
    # El usuario actual está disponible como request.user
    usuario = request.user
    
    # Puedes añadir más contexto si lo necesitas
    context = {
        'usuario': usuario
    }
    
    return render(request, 'perfil.html', context)


@login_required
def perfil(request):
    usuario = request.user
    
    # Acceder al perfil extendido (asumiendo que tienes un modelo Profile relacionado)
    try:
        perfil = usuario.profile  # o el nombre que hayas dado a la relación
    except:
        perfil = None
    
    context = {
        'usuario': usuario,
        'perfil': perfil
    }
    
    return render(request, 'perfil.html', context)



@login_required
def perfil(request):
    usuario = request.user
    
    # Obtener reservaciones de este usuario (suponiendo que tienes un campo usuario en el modelo Reservacion)
    reservaciones = Reservacion.objects.filter(nombre=usuario.username).order_by('-fecha')
    
    context = {
        'usuario': usuario,
        'reservaciones': reservaciones
    }
    
    return render(request, 'perfil.html', context)


from datetime import date

@login_required
def perfil(request):
    usuario = request.user
    reservaciones = Reservacion.objects.filter(nombre=usuario.username).order_by('-fecha')
    
    context = {
        'usuario': usuario,
        'reservaciones': reservaciones,
        'today': date.today()
    }
    
    return render(request, 'perfil.html', context)












