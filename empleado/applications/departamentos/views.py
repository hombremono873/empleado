from django.shortcuts import render 
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.views.generic.list import ListView

#from applications.departamentos.forms import NewDepartamentoForm
from applications.departamentos.forms import NewDepartamentoForm
from applications.empleados.models import Empleado
from applications.departamentos.models import Departamentos
# Create your views here.

"""Se importo el modelo empleado y departamento que estan en relacion done un departamento tiene muchos empleados
"""
class ListaDepartamentos(ListView):
    model = Departamentos
    context_object_name = 'departamentos'
    template_name='departamentos/listadept.html'
    
class NewDepartamentoView(FormView):
     template_name = 'departamentos/new_departamento.html'
     form_class = NewDepartamentoForm
     
     def form_valid(self, form):
        # Aquí puedes agregar cualquier lógica adicional que necesites
               
        #Nueva instancia del modelo Empleado
        #Se recuperan los datos digitados en el formulario
        nombre=form.cleaned_data['departamento'] #'departamento' campo del formulario
        nombrecorto = form.cleaned_data['shortname'] #'shortname campo del formulario
        #Se importa el modelo departamento y se crea una nueva instancia
        depa = Departamentos.objects.create(
            name = nombre,
            short_name=nombrecorto,
        )
        #depa.save() no se requiere por que create() hace el save()
        #Se recupera datos del formulario
        
        nombre = form.cleaned_data['nombre']
        apellido = form.cleaned_data['apellidos']
        
        empl = Empleado.objects.create(
            first_name = nombre,
            last_name =apellido,
            job='1',
            departamento = depa
        )
        #empl.save() no se requiere por que crate hace el save()
        
        return super().form_valid(form)
    
     def get_success_url(self):
        # Opcionalmente puedes sobreescribir este método si quieres personalizar la URL de redirección
        return reverse_lazy('home')  # Redirige al nombre de la ruta 'home'
     