from django.db import models
from django.core.validators import MinValueValidator
from .nodo import Nodo

class PuntoDeRetiro(Nodo):
    capacidad = models.IntegerField(validators=[MinValueValidator(1)])