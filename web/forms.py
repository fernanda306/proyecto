from django import forms
from .models import Sugerencia  # Elimina la importación de Usuario si no existe
from django.core.mail import send_mail

from django.contrib import admin
from django.conf import settings

from .models import Reservacion








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











class ReservacionForm(forms.ModelForm):
    class Meta:
        model = Reservacion
        fields = ['nombre', 'fecha', 'hora', 'num_personas', 'mensaje']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
            'mensaje': forms.Textarea(attrs={'rows': 4}),
        }

    def send_mail(self):
        asunto = "Nueva reservacion Recibida"
        mensaje = (
            f"Has recibido una nueva reservacion de: {self.cleaned_data['nombre']}):\n\n"
              f"la fecha de reservacion es: {self.cleaned_data['fecha']}):\n\n"
                f"la hora de la reservacion es: {self.cleaned_data['hora']}):\n\n"
                  f"las especificaciones del cliente son: {self.cleaned_data['mensaje']}):\n\n"
           
          
        )
        destinatario = "fernandamanriquefernandez724@gmail.com"
        send_mail(asunto, mensaje, settings.EMAIL_HOST_USER, [destinatario])



