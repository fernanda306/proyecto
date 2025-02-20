

<<<<<<< HEAD


=======
from django import forms

class SugerenciaForm(forms.Form):
    email = forms.EmailField(required=False, label='Tu correo (opcional)')
    sugerencia = forms.CharField(widget=forms.Textarea, label='Tu sugerencia')
>>>>>>> a77b5d777e7bf2b608827958df88ac334517cce9
