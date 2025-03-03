from django.contrib import admin
from django.utils.html import format_html
from .models import Producto, carritoitem, datos, Reservacion

# Register your models here.

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'precio', 'cantidad', 'mostrar_imagen')
    search_fields = ('nombre',)
    list_filter = ('precio', 'cantidad')

    def mostrar_imagen(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="50" height="50"/>'.format(obj.imagen.url))
        return "Sin imagen"
    
    mostrar_imagen.short_description = "Imagen"


@admin.register(carritoitem)
class carritoitemAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad', 'usuario', 'sesion_id', 'fecha_creacion')
    list_filter = ('fecha_creacion',)   
    search_fields = ('producto__nombre', 'usuario__username')


@admin.register(datos)
class Adminperfilusuario(admin.ModelAdmin):
    model = datos
    list_display = ('usuario', 'nombre', 'apellido')

@admin.register(Reservacion)
class ReservacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'hora', 'num_personas', 'fecha_creacion')
    list_filter = ('fecha', 'hora')
    search_fields = ('nombre', 'mensaje')
    date_hierarchy = 'fecha'

