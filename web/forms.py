from django import forms
from .models import Sugerencia  # Elimina la importación de Usuario si no existe
from django.core.mail import send_mail
from .models import Reserva
from django.contrib import admin
from django.conf import settings




if not admin.site.is_registered(Sugerencia):
    @admin.register(Sugerencia)
    class SugerenciaAdmin(admin.ModelAdmin):
        # Configuración de SugerenciaAdmin
        pass

class SugerenciaForm(forms.ModelForm):
    class Meta:
        model = Sugerencia
        fields = ['username', 'email', 'section_text']
    def send_mail(self):
        asunto = "Nueva Sugerencia Recibida"
        mensaje = (
            f"Has recibido una nueva sugerencia de {self.cleaned_data['username']}):\n\n"
            f"Mensaje del cliente: \n{self.cleaned_data['section_text']}\n\n"
            f"Contactate con el cliente: {self.cleaned_data['email']}"
        )
        destinatario = "fernandamanriquefernandez724@gmail.com"
        send_mail(asunto, mensaje, settings.EMAIL_HOST_USER, [destinatario])




class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre', 'fecha', 'hora', 'numero_personas', 'comentarios']







