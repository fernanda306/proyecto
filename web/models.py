from django.db import models

# Create your models here.

class producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion= models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateField(auto_now_add= True)

    def _str_(self):
     return self.nombre


