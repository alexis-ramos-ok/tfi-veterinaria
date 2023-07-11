from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['nombre_mascota', 'raza', 'nombre_dueno', 'telefono', 'email']
