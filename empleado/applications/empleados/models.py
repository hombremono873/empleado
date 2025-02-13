from django.db import models # type: ignore
from applications.departamentos.models import Departamentos
# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)
    class Meta:
        verbose_name = "Habilidad"
        verbose_name_plural = "Habilidades empleados"
        
    def __str__(self):
      if self.id and self.habilidad:
        return f"{self.id}-{self.habilidad}"
      return "Objeto no inicializado"
    
class Empleado(models.Model):
    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2','ECONOMISTA'),
        ('3', 'OTRO'),
    )
    
    first_name = models.CharField(max_length=60, null=False)
    last_name = models.CharField(max_length=60, null=False)
    full_name = models.name = models.CharField(
        'Nombres Completos',
        max_length=120,
        blank=True
    )
    
    job = models.CharField(max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamentos, on_delete=models.CASCADE) 
    imagen = models.ImageField(upload_to="empleado", blank = True,null=True
                              ,height_field=None
                              ,width_field=None
                              ,max_length=None)
    habilidades = models.ManyToManyField(Habilidades)
    
    class Meta:
        verbose_name_plural = "Empleados"
        verbose_name = "Empleado"
        ordering = ['-first_name']
    def __str__(self):
        return str(self.id) + '_' + self.first_name + '_' + self.last_name
                   
