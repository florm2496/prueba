from django import forms

from .models import modelo , carpeta



class uploadForm(forms.ModelForm):
    class Meta:
        model=modelo
        fields=('nombre',
                'archivo',
                'carpeta',
                )
        widgets={
            'archivo':forms.ClearableFileInput(
                attrs={
                    'multiple': True,
                }
            
            )
  
        }

    
class carpetaForm(forms.ModelForm):
    class Meta:
        model=carpeta
        fields=('nombre',)

    def clean_nombre(self):
        nombre=self.cleaned_data['nombre']
        if nombre=='':
            print('------------')
            raise forms.ValidationError('introduzca un nombre')

        return nombre
        