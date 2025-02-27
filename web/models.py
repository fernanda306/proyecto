from django.db import models
from django.contrib.auth.models import AbstractUser, User


# Create your models here.



class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    nombre = models.CharField(max_length=255)
    caracteristicas = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    cantidad = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} - ${self.precio}"
    


class Sugerencia(models.Model):

    username = models.CharField(max_length=100)
    email = models.EmailField()
    section_text = models.TextField()
    

    def __str__(self):
        return self.username



        

class Reserva(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()
    numero_personas = models.IntegerField()
    comentarios = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.fecha} {self.hora}"

