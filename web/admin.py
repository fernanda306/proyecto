from django.contrib import admin
from django.contrib import admin
from django.utils.html import format_html
from .models import Producto



# Register your models here.
# class  productoAdmin(admin.ModelAdmin):
#     model = producto
#     list_display =('nombre','descripcion','pecio','fecha_creacion')

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
