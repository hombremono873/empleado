from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.

admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name','Nombre_Completo', 'departamento', 'job',)
    search_fields = ('first_name', 'last_name',)
    list_filter = ('departamento', 'habilidades',)
    ordering = ['first_name']
    fields = ('first_name', 'last_name', 'departamento', 'job', 'habilidades',)
    filter_horizontal = ('habilidades',)  # Mejora la interfaz para ManyToMany
    
    def Nombre_Completo(self, obj):
        return f"{obj.first_name} {obj.last_name}" #obj es una instancia del modelo empleado
    nombre_completo = 'Nombre_Completo'
    
    list_per_page = 10
    
admin.site.register(Empleado, EmpleadoAdmin)    