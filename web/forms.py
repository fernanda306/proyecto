from django import forms
from django.contrib import admin
from .models import Sugerencia, User



@admin.register(Sugerencia)
class SugerenciaAdmin(admin.ModelAdmin):
    list_display = ("username", "email")
    search_fields = ("username", "email" )

class SugerenciaForm(forms.ModelForm):
    class Meta:
        model = Sugerencia
        fields = ["username", "email", "section_text"]


