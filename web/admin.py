from django.contrib import admin
from django.contrib import admin
from django.utils.html import format_html
from .models import Producto


from django.contrib import admin
from .models import Reservacion



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




@admin.register(Reservacion)
class ReservacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha', 'hora', 'num_personas', 'fecha_creacion')
    list_filter = ('fecha', 'hora')
    search_fields = ('nombre', 'mensaje')
    date_hierarchy = 'fecha'





