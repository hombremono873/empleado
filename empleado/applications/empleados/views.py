from django.core.paginator import Paginator # type: ignore
from django.shortcuts import render # type: ignore
from django.views.generic import ( # type: ignore
      ListView, DetailView, 
      CreateView, TemplateView,
      UpdateView, DeleteView
    )
from .models import Empleado
from django.urls import reverse_lazy # type: ignore

class ListallEmpleados(ListView):
    template_name = 'empleados/list_all.html'
    ##model = Empleado al sobre escribir get_queryset no se requiere al parametro 
    context_object_name = "empleados"
    paginate_by = 4  # Paginación, 4 empleados por página
    
    #ordering=['first_name']
    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')  # Recuperamos la palabra clave
        lista = Empleado.objects.filter(
            #first_name__icontains=palabra_clave
            first_name__icontains = palabra_clave
        )  # Hacemos la búsqueda de forma insensible a mayúsculas/minúsculas
        return lista
    
   
        

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
    model =Empleado   
    template_name="empleados/detalle_empleado.html"
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        empleado = self.get_object()
        context['titulo','habilidades'] = empleado.habilidades.all()
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
    fields =['first_name', 'last_name','job','departamento', 'habilidades']
    #fields =('__all__')
    #success_url = '/about'  #Redireccionamos
    def  form_valid(self, form):
        empleado = form.save() #Se salva eb BDD y ademas se asigna la data a empleado
        empleado.full_name = empleado.first_name + ' ' +empleado.last_name
        empleado.save() #Actualiza en la base de datos el atributo full_name
        return super(EmpleadoCreateView, self).form_valid(form)
    
    success_url = reverse_lazy('persona_app:correcto')
    
#Para mostrar los datos use form form.as_p O usando cada campo asi:
#form.first_name, form.last_name .........
#Como UpdateView nos trae el contenido de los campos de un registro
#En la plantilla debemos usar el elemento <form> con el metodo POST 
class EmpleadoUpdateView(UpdateView):
    model=Empleado
    template_name = "empleados/update.html" 
    fields =['first_name', 'last_name','job','departamento', 'habilidades']
    
    """Vifurcar hacia otra página"""
    success_url = reverse_lazy('persona_app:correcto')
    
    """Cuando necesitamos hacer un proceso extra antes de guardar los datos
    Podemos sobre-escribir los methodos Post y form_valid
    Es decir con Pos obtengo un objeto especifico los proceso segun sea necesario y luego se llama
    al form_valid"""
    #Observar self.object se carga con el objeto empleado
    #El parametro request trae el valor de los campos a los que se quiere procesar
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print("==================Methodo Post=====================")
        print(self.object.first_name)
        #Se obtiene un diccionario
        ob = request.POST.copy()
        ob['last_name'] = "Perez"
        request.POST = ob
        print(ob)
        print("***********Fin metodo Post*********")
        return super().post(request, *args, **kwargs) 
    """En el metodo post mediante request obtuvimos una copia diccionario de datos
    modificamos el dato y se salva en auto en la bdd"""
    #Observemos que cargamos el objeto empleado  
    def  form_valid(self, form):
        #empleado = form.save() #Se salva eb BDD y ademas se asigna la data a empleado
        print("********Metodo form_valid*************")
        #print(empleado.last_name)
        print("******Ened valid**********")
        return super(EmpleadoUpdateView, self).form_valid(form) 
    
class EmpleadoDeleteView(DeleteView):
      model=Empleado
      template_name="empleados/delete.html"
      success_url = reverse_lazy('persona_app:correcto')
      
class InicioView(TemplateView):
    """Pagina de incio no depende de nadie va directo"""   
    template_name = "inicio.html"       
    model = Empleado
    