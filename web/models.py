from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.core.validators import MinValueValidator





# Create your models here.

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    nombre = models.CharField(max_length=255)
    caracteristicas = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField()  # Asegúrate de que este campo esté definido

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
    

class Sugerencia(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)  # Added phone field
    section_text = models.TextField()

    def __str__(self):
        return f"{self.username} - {self.phone or 'No phone'}"  # Updated __str__ method


# Remove the conflicting class definition

class Reservacion(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre completo")
    email = models.EmailField(verbose_name="Correo electrónico")
    fecha = models.DateField(verbose_name="Fecha de reservación")
    hora = models.TimeField(verbose_name="Hora de reservación")
    num_personas = models.PositiveIntegerField(
        verbose_name="Número de personas",
        validators=[MinValueValidator(1)]
    )
    mensaje = models.TextField(verbose_name="Mensaje adicional", blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Reservación"
        verbose_name_plural = "Reservaciones"
        ordering = ['-fecha', '-hora']
    
    def __str__(self):
        return f"Reservación de {self.nombre} para {self.num_personas} personas el {self.fecha} a las {self.hora}"








class carritoitem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    sesion_id = models.CharField(max_length=100, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"
    
    def subtotal(self):
        return self.producto.precio * self.cantidad



class datos(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    


class Orden(models.Model):
        usuario = models. ForeignKey(User, on_delete=models. CASCADE, null=True, blank=True)
        nombre = models. CharField (max_length=200)
        email = models. EmailField ()
        telefono = models.CharField (max_length=20)
        sesion_id = models.CharField(max_length=100, null=True, blank=True)
        total = models.DecimalField(max_digits=10, decimal_places=0)
        metodo_pago = models.CharField(max_length=20, choices=[( 'nequi','Nequi'), ('bancolombia', 'Bancolombia')])
        pagado = models.BooleanField(default=False)
        fecha_creacion = models.DateTimeField (auto_now_add=True)

        def __str__(self):
            return f"orden #{self.id} - {self.nombre}"
        

class OrdenItem(models.Model):

        orden = models.ForeignKey(Orden, related_name='items', on_delete=models.CASCADE)
        producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
        precio = models.DecimalField(max_digits=10, decimal_places=2)
        cantidad = models.IntegerField(default=1)

        def __str__(self):
            return f"orden #{self.cantidad} x {self.producto.nombre}"
        
        def subtotal(self):
             return self.precio  * self.cantidad




