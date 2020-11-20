from django.db import models
from .nodo import Nodo
from .horario import Horario

class Sucursal(Nodo):
    disponibilidad = models.OneToOneField(Horario, on_delete=models.CASCADE, verbose_name="Horario", default=1)
    direccion = models.CharField(max_length=100)