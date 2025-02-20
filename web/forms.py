

from django import forms

class SugerenciaForm(forms.Form):
    email = forms.EmailField(required=False, label='Tu correo (opcional)')
    sugerencia = forms.CharField(widget=forms.Textarea, label='Tu sugerencia')