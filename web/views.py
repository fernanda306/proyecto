import logging
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from .forms import SugerenciaForm
from .models import  carritoitem, Reservacion, datos, pedido
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.tokens import default_token_generator 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode 
from django.utils.encoding import force_bytes, force_str
from django.urls import reverse
from django.urls import path
from .forms import ReservacionForm
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Producto
from django.contrib.auth.decorators import login_required


from .models import Orden, OrdenItem, carritoitem
from .forms import OrdenForm

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


def sugerencias(request):
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
    form = ReservacionForm()
    if request.method == 'POST':
        form = ReservacionForm(request.POST)
        if form.is_valid():
            form.save()
            form.send_mail()
            return redirect('reservacion_exitosa')
    return render(request, 'reservacion.html', {'form': form})

def reservacion_exitosa(request):
    return render(request, 'reservacion_exitosa.html')



def productos(request):
    productos = Producto.objects.all()
    return render(request, 'productos.html', {'productos': productos})





def productos(request):
    producto_lista = Producto.objects.all()

    if request.method == "POST" and 'producto_id' in request.POST:
        producto_id = request.POST.get('producto_id')
        try:
            producto = Producto.objects.get(id=producto_id)
            
            if not request.user.is_authenticated:
                if not request.session.session_key:
                    request.session.create()
                sesion_id = request.session.session_key
                
                carrito_item, created = carritoitem.objects.get_or_create(
                    producto=producto,
                    sesion_id=sesion_id,
                    usuario=None
                )
                
                if not created:
                    carrito_item.cantidad += 1
                    carrito_item.save()
            else:
                carrito_item, created = carritoitem.objects.get_or_create(
                    producto=producto,
                    usuario=request.user,
                    sesion_id=None
                )
                
                if not created:
                    carrito_item.cantidad += 1
                    carrito_item.save()
            
            messages.success(request, f"{producto.nombre} añadido al carrito")
        except Producto.DoesNotExist:
            messages.error(request, "Producto no encontrado")
    
    return render(request, 'productos.html', {'productos': producto_lista})

    










def cerrar_sesion(request):
    logout(request)
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







@login_required
def perfil(request):
  
    user = request.user
    
    context = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'full_name': f"{user.first_name} {user.last_name}",
        'email': user.email,
        'is_active': user.is_active,
        'date_joined': user.date_joined,
        'last_login': user.last_login,
       
    }
    context['is_staff'] = user.is_staff
    context['is_superuser'] = user.is_superuser
    context['groups'] = user.groups.all()
    
    return render(request, 'perfil.html', context)




def ver_carrito(request):
     carrito_items = []
     total = 0

     if request.user.is_authenticated:
         carrito_items = carritoitem.objects.filter(usuario=request.user)
     else:
         if request.session.session_key:
             carrito_items = carritoitem.objects.filter(sesion_id=request.session.session_key)
            
     for item in carrito_items:
         total += item.subtotal()

     return render(request, 'carrito.html', {
         'carrito_items': carrito_items,
         'total': total,
     })





def actualizar_carrito(request, item_id):
    try:
        item = carritoitem.objects.get(id=item_id)

        if request.user.is_authenticated and item.usuario == request.user or \
            not request.user.is_authenticated and item.sesion_id == request.session.session_key:

            cantidad = int(request. POST.get ( 'cantidad', 1))
            if cantidad > 0:
                item. cantidad = cantidad
                item. save()
            else:
                item. delete()

            messages. success (request, "Carrito actualizado")
        else:
            messages.error(request, "No tienes permiso para modificar este item")
    except carritoitem.DoesNotExist:
        messages.error (request, "Item no encontrado")
    return redirect('ver_carrito')

def eliminar_item(request, item_id):
    try:
        item = carritoitem.objects.get(id=item_id)
        if request.user.is_authenticated and item.usuario == request.user or \
           not request.user.is_authenticated and item.sesion_id == request.session.session_key:
            item.delete()
            messages.success(request, "Item eliminado del carrito")
        else:
            messages.error(request, "No tienes permiso para eliminar este item")
    except carritoitem.DoesNotExist:
        messages.error(request, "Item no encontrado")
    return redirect('ver_carrito')







def pasarela(request):
    carrito_items = []
    total = 0
    
    # Verificar si el usuario está autenticado o si hay una sesión activa
    if request.user.is_authenticated:
        carrito_items = carritoitem.objects.filter(usuario=request.user)
    elif request.session.session_key:
        carrito_items = carritoitem.objects.filter(sesion_id=request.session.session_key)
    
    # Si el carrito está vacío, mostrar advertencia y redirigir
    if not carrito_items.exists():
        messages.warning(request, "Tu carrito está vacío")
        return redirect('ver_carrito')
    
    # Calcular el total del pedido
    for item in carrito_items:
        total += item.subtotal()
    
    if request.method == 'POST':
        form = OrdenForm(request.POST)
        metodo_pago = request.POST.get('metodo_pago')
        
        if form.is_valid():
            orden = form.save(commit=False)
            
            if request.user.is_authenticated:
                orden.usuario = request.user
            else:
                orden.sesion_id = request.session.session_key
            
            orden.total = total
            
            # Verificar si se seleccionó un método de pago
            if metodo_pago:
                orden.metodo_pago = metodo_pago
                
                # Si es contraentrega, establecer estado específico
                if metodo_pago == 'contraentrega':
                    orden.estado = 'pendiente'
                
                orden.save()
                
                # Guardar los productos en la orden
                for item in carrito_items:
                    OrdenItem.objects.create(
                        orden=orden,
                        producto=item.producto,
                        precio=item.producto.precio,
                        cantidad=item.cantidad
                    )
                
                # Vaciar el carrito después del pago
                carrito_items.delete()
                
                # 📧 Enviar el correo de confirmación
                enviar_correo_confirmacion(orden)
                
                messages.success(request, "Tu pedido ha sido procesado con éxito")
                return redirect('confirmar', orden_id=orden.id)
            else:
                messages.error(request, "Por favor selecciona un método de pago válido.")
        else:
            messages.error(request, "Por favor verifica los datos del formulario.")
    else:
        # Precargar los datos del usuario en el formulario
        initial_data = {}
        if request.user.is_authenticated:
            try:
                datos_usuario = datos.objects.get(usuario=request.user)
                initial_data = {
                    'nombre': f"{datos_usuario.nombre} {datos_usuario.apellido}",
                    'email': request.user.email
                }
            except datos.DoesNotExist:
                initial_data = {
                    'nombre': request.user.username,
                    'email': request.user.email
                }
        
        form = OrdenForm(initial=initial_data)
    
    return render(request, 'pasarela.html', {
        'form': form,
        'carrito_items': carrito_items,
        'total': total
    })










def confirmacion(request, orden_id):
    try:
        if request.user.is_authenticated:
            orden = Orden.objects.get(id=orden_id, usuario=request.user)
        else:
            orden = Orden.objects.get(id=orden_id, sesion_id=request.session.session_key)
        
        # Obtener los items de la orden en ambos casos
        items = OrdenItem.objects.filter(orden=orden)
        
        return render(request, 'confirmacion.html', {
            'orden': orden,
            'items': items
        })
    except Orden.DoesNotExist:
        # Manejar el caso donde la orden no existe
        messages.error(request, "No se encontró la orden especificada.")
        return redirect('home')  # O redirigir a donde sea apropiado
    


    except Orden.DoesNotExist:
        messages.error(request, "Orden no encontrada")
        return redirect('productos')
    

def enviar_correo_confirmacion(orden):

    asunto = f"Confirmación de Pedido #{orden.id}"
    mensaje = f"""
    Hola {orden.nombre},
        Gracias por tu compra. Hemos recibido verificar la compra en su cuenta .
        🛍 *Detalles del Pedido*
        - Número de Pedido: {orden.id}
        - Total: ${orden.total}
        - Método de Pago: {orden.get_metodo_pago_display()}
        - Fecha: {orden.fecha_creacion.strftime('%d/%m/%Y %H:%M')}
        📦 *Productos Comprados*:
        """
# Agregar productos al mensaje
    items = OrdenItem.objects.filter(orden=orden)
    for item in items:
        mensaje += f"\n - {item.cantidad} x {item.producto.nombre} (${item.precio} c/u)"
     
    #  (${items.precio}c/u)"
        mensaje += f"\n - {item.cantidad} x {item.producto.nombre}"
    send_mail(
    asunto,
    mensaje,
    'jalmpa77@gmail.com', # Correo del remitente
    [orden.email],
    fail_silently=False,
    )




# def historial(request):
#      return render (request, 'historial.html')


def historial(request):
    # Filter by date if provided
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    
    # Get user's orders
    ordenes = Orden.objects.filter(usuario=request.user)
    
    # Apply date filters if provided
    if fecha_inicio:
        ordenes = ordenes.filter(fecha_creacion__gte=fecha_inicio)
    if fecha_fin:
        ordenes = ordenes.filter(fecha_creacion__lte=fecha_fin)
    
    # Order by date (newest first)
    ordenes = ordenes.order_by('-fecha_creacion')
    
    context = {
        'ordenes': ordenes,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin
    }
    
    return render(request, 'historial.html', context)




def manual(request):
    return render (request, 'manual.html')