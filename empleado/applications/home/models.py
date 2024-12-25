from django.db import models # type: ignore

class Prueba(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo + ' ' + self.subtitulo
