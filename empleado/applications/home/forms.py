from django import forms 
from .models import Prueba 

class Pruebaform(forms.ModelForm):
    
    class Meta:
        model= Prueba
        #fields = ('__all__')
        fields =(
            'titulo',
            'subtitulo', 
            'cantidad',)
        widgets={
            'titulo': forms.TextInput(attrs={
                'placeholder':'Ingrese texto aqui'
            }),
            'cantidad':forms.NumberInput(attrs={
                'class':'form-control',
                'min':'10'
            }),
                                    
        }
    def clean_cantidad(self):
        cantidad = self.cleaned_data["cantidad"]
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un valor mayor a 10')
        return cantidad
        
        
