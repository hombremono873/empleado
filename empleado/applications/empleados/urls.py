
from django.urls import path # type: ignore
from . import views

app_name = 'persona_app'
urlpatterns = [
    path('listar_all_empleados/',
         views.ListallEmpleados.as_view()
         , name='empleados_all'
    ),#Llamamos la lista generica
    
    path('listar_by_area/<parametro>', views.ListByAreaEmpleados.as_view()),
    path('listar_by_kwords/', views.ListEmpleadoByKwords.as_view()),
    path('listar_habilidades/', views.ListarHabilidades.as_view()),
    path('detalle_empleado/<pk>/', views.EmpleadoDetailView.as_view(), name="empleado_detalle"),
    path('create_empleado/', views.EmpleadoCreateView.as_view(), name="nuevo_empleado"),
    #Etiqueta name = 'correcto' usada para acceder de manera compacta a la url
    path('about/', views.About.as_view(), name='correcto'),
    path('empleadoupdate/<pk>/', views.EmpleadoUpdateView.as_view(), name='modificar_empleado'),
    path('delete/<pk>/', views.EmpleadoDeleteView.as_view(), name='delete_empleado'),
    path('', views.InicioView.as_view(), name='inicio'),
    path('lista_empleados_admin/', views.ListaEmpleadosAdmin.as_view(), name='empleados_admin'),
 ]