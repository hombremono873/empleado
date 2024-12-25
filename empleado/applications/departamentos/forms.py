from django import forms
from django.urls import reverse_lazy # type: ignore
class NewDepartamentoForm(forms.Form):
    nombre =forms.CharField(max_length=50, required = True)
    apellidos =forms.CharField(max_length=50, required = True)
    departamento = forms.CharField(max_length=50, required=True)
    shortname = forms.CharField(max_length=20)
    #success_url = 'home/'
    
    def form_valid(self, form):
        print("**********Estamos validando*************")
        return super(NewDepartamentoForm, self).form_valid(form)
    