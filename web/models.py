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
    section_text = models.TextField()
    

    def __str__(self):
        return self.username





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







