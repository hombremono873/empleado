from django.contrib import admin
from .models import Empleado, Habilidades

# Registro del modelo Habilidades
admin.site.register(Habilidades)

# Personalización del modelo Empleado en el admin
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name','full_name','Nombre_Completo', 'departamento', 'job',)
    search_fields = ('first_name', 'last_name',)
    list_filter = ('departamento', 'job', 'habilidades',)
    ordering = ['first_name']
    fields = ('first_name', 'last_name','full_name', 'departamento', 'job', 'habilidades',)
    filter_horizontal = ('habilidades',)  # Mejora la interfaz para ManyToMany

    def Nombre_Completo(self, obj):
        return f"{obj.first_name} {obj.last_name}"  # obj es una instancia del modelo Empleado
    
    Nombre_Completo.short_description = 'Nombre Completo'  # Cambia el nombre en el admin

    list_per_page = 10

# Registro del modelo Empleado con la clase personalizada
admin.site.register(Empleado, EmpleadoAdmin)
