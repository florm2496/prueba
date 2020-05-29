from .models import Emergencia
from django import forms 

class CrearEmergenciaForm(forms.ModelForm):
     class Meta:
        model =Emergencia
        fields = (
        'categoria',
        'escuela',
        'descripcion',
        )
