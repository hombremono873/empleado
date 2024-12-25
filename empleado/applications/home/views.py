from django.shortcuts import render # type: ignore
from django.views.generic import TemplateView # type: ignore
from django.views.generic import ListView, CreateView # type: ignore
from .models import Prueba
from django.urls import reverse_lazy # type: ignore
from .forms import Pruebaform

class IndexView(TemplateView): # type: ignore
    #template_name = "home/home.html" #busca en templates la home.html
    template_name = "home/prueba2.html"

class ResumeFoundatiumView(TemplateView): # type: ignore
    #template_name = "home/home.html" #busca en templates la home.html
    template_name = "home/resumenfoundatium.html"    
    
class PersonaListView(ListView): # type: ignore
    template_name = 'post_list.html'
    #def get_queryset(self):
    #Define los datos que se pasarán al contexto
    queryset= [
            {'nombre': 'Ana', 'documento': '123456789'},
            {'nombre': 'Carlos', 'documento': '987654321'},
            {'nombre': 'Laura', 'documento': '456789123'},
            {'nombre': 'Laura', 'documento': '456789123'},
            {'nombre': 'Laura', 'documento': '456789123'},
            {'nombre': 'Laura', 'documento': '456789123'},
            {'nombre': 'Laura', 'documento': '456789123'},
            {'nombre': 'Laura', 'documento': '456789123'},
            {'nombre': 'Laura', 'documento': '456789123'},
            {'nombre': 'Laura', 'documento': '456789123'},
        ]
    context_object_name ="listapersonas" 

class ModeloPruebaListView(ListView):
    model = Prueba
    template_name = "home/listaprueba.html"
    context_object_name = "listaprueba"

"""Cuando creamos instancias de un modelo se crea automaticamente con el objeto la variable form
y puede ser usada automaticamente en el template
Renderiza los campos: Al usar {{ form }} o métodos como form.as_p,
form.as_table, o form.as_ul,"""    
#CreateView, UpdatyeView, DeleteView, FormView
class PruebaCreateView(CreateView):
    template_name="home/add.html"
    model=Prueba
    #fields=['titulo','subtitulo','cantidad']
    form_class = Pruebaform   #Nos traemos los campos del formulario
    #success_url = '/'
    success_url = reverse_lazy('prueba_add')  # Redirige automáticamente a la página de éxito después de crear un objeto
