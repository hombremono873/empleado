from django.core.paginator import Paginator # type: ignore
from django.shortcuts import render # type: ignore
from django.views.generic import ( # type: ignore
      ListView, DetailView, 
      CreateView, TemplateView,
      UpdateView, DeleteView
    )
from .models import Empleado
from django.urls import reverse_lazy # type: ignore
from django.http import Http404

#Importamos el formulario que usaremos para personalizar nuestra vista
from .forms import EmpleadoForm

class ListallEmpleados(ListView):
    template_name = 'empleados/list_all.html'
    ##model = Empleado al sobre escribir get_queryset no se requiere al parametro 
    context_object_name = "empleados"
    paginate_by = 4  #Cuando se pagina , automaticamente ListView crea un objeto de paginación
    ordering = 'first_name'
    
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')  # Recuperamos la palabra clave
        lista = Empleado.objects.filter(
             first_name__icontains = palabra_clave    #Palabra clave es el name empleado
        )  # Hacemos la búsqueda de forma insensible a mayúsculas/minúsculas
        return lista
    
class ListaEmpleadosAdmin(ListView):
    template_name = 'empleados/list_empleados_admin.html'
    model = Empleado                #Al sobre escribir get_queryset no se requiere al parametro 
    context_object_name = "empleados"
    paginate_by = 10                #Cuando se pagina , automaticamente ListView crea un objeto de paginación
    ordering = 'first_name'
    
    
      
        

class ListByAreaEmpleados(ListView):
    template_name = 'empleados/list_by_area.html'

    def get_queryset(self):
        area = self.kwargs['parametro']
        lista = Empleado.objects.filter(departamento__name=area)
        return lista


class ListByAreaEmpleados_dos(ListView):
    template_name = 'empleados/list_by_area.html'
    context_object_name = 'empleados'

    # Filtro directo para el área específica
    queryset = Empleado.objects.filter(departamento__name='Mantenimiento eléctrico e Instrumentación')


class ListByAreaEmpleados1(ListView):
    template_name = 'empleados/list_by_area.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        area = 'Contabilidad'  # Área hardcodeada
        return Empleado.objects.filter(departamento__short_name=area)


class ListEmpleadoByKwords(ListView):
    template_name = 'empleados/list_by_kwords.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')  # Recuperamos la palabra clave
        lista = Empleado.objects.filter(
            #first_name__icontains=palabra_clave
            first_name = palabra_clave
        )  # Hacemos la búsqueda de forma insensible a mayúsculas/minúsculas
        #print(lista)  # Para depurar la consulta, si lo necesitas
        return lista
    
"""En el metodo get_queryset creamos el atributo tipo empleaodo y obtenemos un registro
empleado usando el id luego imprimimos el atributo many to many que es habilidades"""    
class ListarHabilidades(ListView):
    template_name = "empleados/habilidades.html"   
    context_object_name = "habilidades"
    
    def get_queryset(self):
        ident = self.request.GET.get('search')
        empleado = Empleado.objects.get(id=int(ident))
        lista = empleado.habilidades.all()
        return lista
class EmpleadoDetailView(DetailView):
    model = Empleado   
    template_name = "empleados/detalle_empleado.html"

    def get_object(self, queryset=None):
        try:
            return super().get_object(queryset)
        except Empleado.DoesNotExist:
            raise Http404("Empleado no encontrado")   
class EmpleadoDetailView1(DetailView):
    model = Empleado   
    template_name = "empleados/detalle_empleado.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        empleado = self.get_object()
        context['titulo'] = 'Detalle del Empleado'
        context['habilidades'] = empleado.habilidades.all()
        return context
       
class About(TemplateView):
    template_name = "empleados/about.html"  # Plantilla que renderiza la página
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['company_name'] = "Mi Compañía"
        context['team'] = [
            {'name': 'Juan Pérez', 'role': 'CEO'},
            {'name': 'Ana López', 'role': 'Desarrolladora'},
            {'name': 'Carlos Gómez', 'role': 'Diseñador'},
        ]
        return context

    
class EmpleadoCreateView(CreateView):
    model = Empleado  
    template_name = "empleados/createEmpleado.html"  
    form_class = EmpleadoForm
    """fields =[
        'first_name',
        'last_name',
        'job',
        'departamento', 
        'habilidades',
        'imagen',
    ]"""
    #fields =('__all__')
    #success_url = '/about'  #Redireccionamos
    def  form_valid(self, form):
        empleado = form.save() #Se salva eb BDD y ademas se asigna la data a empleado
        empleado.full_name = empleado.first_name + ' ' +empleado.last_name
        empleado.save() #Actualiza en la base de datos el atributo full_name
        return super(EmpleadoCreateView, self).form_valid(form)
    success_url = reverse_lazy('persona_app:empleados_admin')
    
#Para mostrar los datos use form form.as_p O usando cada campo asi:
#form.first_name, form.last_name .........
#Como UpdateView nos trae el contenido de los campos de un registro
#En la plantilla debemos usar el elemento <form> con el metodo POST 
class EmpleadoUpdateView(UpdateView):
    model=Empleado
    template_name = "empleados/update.html" 
    fields =['first_name', 'last_name','job','departamento', 'habilidades']
    success_url = reverse_lazy('persona_app:empleados_admin')
    
    #Observar self.object se carga con el objeto empleado
    #El parametro request trae el valor de los campos a los que se quiere procesar
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
       #Se obtiene un diccionario
        ob = request.POST.copy()
        #ob['last_name'] = "Perez"
        request.POST = ob
        return super().post(request, *args, **kwargs) 
    
    #Observemos que cargamos el objeto empleado  
    def  form_valid(self, form):
        #empleado = form.save() #Se salva eb BDD y ademas se asigna la data a empleado
        return super(EmpleadoUpdateView, self).form_valid(form) 
    
class EmpleadoDeleteView(DeleteView):
      model=Empleado
      template_name="empleados/delete.html"
      success_url = reverse_lazy('persona_app:empleados_admin')
      context_object_name="empleado"
      success_url = reverse_lazy('persona_app:empleados_admin')
class InicioView(TemplateView):
    """Pagina de incio no depende de nadie va directo"""   
    template_name = "inicio.html"       
    model = Empleado
    
    