from django import forms
from .models import Sugerencia, Orden  # Elimina la importación de Usuario si no existe
from django.core.mail import send_mail
from django.core.validators import RegexValidator

from django.contrib import admin
from django.conf import settings

from .models import Reservacion



from django.core.validators import MaxValueValidator, MinValueValidator


from django.core.exceptions import ValidationError







if not admin.site.is_registered(Sugerencia):
    @admin.register(Sugerencia)
    class SugerenciaAdmin(admin.ModelAdmin):
        # Configuración de SugerenciaAdmin
        pass


class SugerenciaForm(forms.ModelForm):
    phone_number = forms.CharField(
        validators=[
            RegexValidator(
                regex=r'^\+?57\d{10}$',  # Colombian phone number format
                message="Ingrese un número de celular colombiano válido. Ejemplo: +573001234567"
            )
        ],
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '+573001234567',
            'class': 'form-control'
        })
    )

    class Meta:
        model = Sugerencia
        fields = ['username', 'email', 'section_text', 'phone_number']

    def send_mail(self):
        asunto = "Nueva Sugerencia Recibida"
        mensaje = (
            f"Has recibido una nueva sugerencia de {self.cleaned_data['username']}:\n\n"
            f"Mensaje del cliente: \n{self.cleaned_data['section_text']}\n\n"
            f"Correo electrónico del cliente: {self.cleaned_data['email']}\n"
            f"Número de contacto: {self.cleaned_data['phone_number']}\n\n"
            f"Contacta al cliente por correo o teléfono."
        )
        destinatario = "fernandamanriquefernandez724@gmail.com"
        send_mail(asunto, mensaje, settings.EMAIL_HOST_USER, [destinatario])

    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number']
        # Additional cleaning if needed (e.g., removing spaces or formatting)
        return phone










class ReservacionForm(forms.ModelForm):
    MESA_CHOICES = [
        ('interior', 'Mesa Interior'),
        ('terraza', 'Mesa Terraza'),
        ('ventana', 'Mesa Cerca de Ventana'),
        ('privada', 'Mesa Privada'),
    ]
    
    mesa = forms.ChoiceField(
        choices=MESA_CHOICES, 
        required=True, 
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Reservacion
        fields = ['nombre', 'fecha', 'hora', 'num_personas', 'mesa', 'mensaje']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
            'mensaje': forms.Textarea(attrs={'rows': 4}),
            'num_personas': forms.NumberInput(attrs={'min': 1, 'max': 10})
        }

    def clean_num_personas(self):
        num_personas = self.cleaned_data['num_personas']
        if num_personas > 10:
            raise ValidationError("El número máximo de personas es 10.")
        return num_personas

    def clean_hora(self):
        hora = self.cleaned_data['hora']
        # Validar solo horario de PM
        if hora.hour < 12:
            raise ValidationError("Solo se permiten reservas en horario de tarde/noche (PM).")
        return hora

    def send_mail(self):
        asunto = "Nueva Reservación Recibida"
        mensaje = (
            f"Detalles de la Reservación:\n\n"
            f"Nombre: {self.cleaned_data['nombre']}\n"
            f"Fecha: {self.cleaned_data['fecha']}\n"
            f"Hora: {self.cleaned_data['hora']}\n"
            f"Número de Personas: {self.cleaned_data['num_personas']}\n"
            f"Mesa: {dict(self.MESA_CHOICES)[self.cleaned_data['mesa']]}\n"
            f"Mensaje Adicional: {self.cleaned_data['mensaje']}\n"
        )
        destinatario = "fernandamanriquefernandez724@gmail.com"
        send_mail(asunto, mensaje, settings.EMAIL_HOST_USER, [destinatario])



# class OrdenForm(forms.ModelForm):
#     METODOS_PAGO =[
#         ('nequi', 'Nequi'),
#         ('bancolombia', 'Bancolombia'),
#         ('contraentrega','Contraentrega')

#     ]


#     metodo_pago = forms.ChoiceField(

#         choices=METODOS_PAGO,
#         widget=forms.RadioSelect,
#         required=True

#     )

#     class Meta:

#         model = Orden
#         fields = ['nombre', 'email', 'telefono', 'metodo_pago']
#         widgets = {
#            'nombre': forms.TextInput(attrs={'class': 'form-control',
#     'placeholder': 'Tu nombre completo'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control',
#     'placeholder': 'tucorreo@ejemplo.com'}),
#             'telefono': forms.TextInput(attrs={'class': 'form-control',
#     'placeholder': 'Tu número de teléfono'})
# }

class OrdenForm(forms.ModelForm):
    METODOS_PAGO = [
        ('nequi', 'Nequi'),
        ('bancolombia', 'Bancolombia'),
        ('contraentrega', 'Contraentrega')
    ]
    
    # Remove this field definition if it's already defined in your model with the same choices
    # Or ensure it exactly matches your model's field
    metodo_pago = forms.ChoiceField(
        choices=METODOS_PAGO,
        widget=forms.RadioSelect,
        required=True
    )
    
    class Meta:
        model = Orden
        fields = ['nombre', 'email', 'telefono', 'metodo_pago']
        # rest of your code...

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control',
     'placeholder': 'Tu nombre completo'}),
             'email': forms.EmailInput(attrs={'class': 'form-control',
     'placeholder': 'tucorreo@ejemplo.com'}),
             'telefono': forms.TextInput(attrs={'class': 'form-control',
     'placeholder': 'Tu número de teléfono'})
 }