from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Prueba

class IndexView(TemplateView):
    template_name = "home/home.html" #busca en templates la home.html
    
class PersonaListView(ListView):
    template_name = 'post_list.html'
    #def get_queryset(self):
    # Define los datos que se pasarán al contexto
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
    
   
