from django import forms
from .models import Empleado

#Vamos a crear un formulario que dependa de un modelo

from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = (
            "first_name",
            "last_name",
            "full_name",
            "job",
            "departamento",
            "imagen",
            "habilidades",
        )
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el primer nombre',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el apellido',
            }),
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre completo',
            }),
            'job': forms.Select(attrs={
                'class': 'form-select',
            }),
            'departamento': forms.Select(attrs={
                'class': 'form-select',
            }),
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            'habilidades': forms.CheckboxSelectMultiple(attrs={
                'class': 'form-check-input',
            }),
        }

#Despues de creado el formulario debemos importarlo en la vista