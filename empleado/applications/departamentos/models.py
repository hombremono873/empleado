from django.db import models

# Create your models here.
class Departamentos(models.Model):
    name = models.CharField("Nombre", max_length=80)
    short_name = models.CharField('Departamentos', max_length=50)
    active = models.BooleanField("Anulado", default=False)
    
    class Meta:
         verbose_name_plural ="Departamento" #Nombre en el administrador
         ordering=['name']   #Se ordena descendente
         unique_together=('name', 'short_name') #No permite que se repita una combinacion
         
    def __str__(self):
        return self.name + '_' + self.short_name
    