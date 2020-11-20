from django.db import models
from .Ubicacion import Ubicacion

class Nodo(models.Model):
    ubicacion = models.OneToOneField(Ubicacion, on_delete=models.CASCADE, verbose_name="Ubicacion")
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre