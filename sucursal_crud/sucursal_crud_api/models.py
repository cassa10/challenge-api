from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

class Ubicacion(models.Model):
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f'{self.latitud}, {self.longitud}'

class Horario(models.Model):
    DIAS = (
        ('1','Lunes'),
        ('2','Martes'),
        ('3','Miercoles'),
        ('4','Jueves'),
        ('5','Viernes'),
        ('6','Sabado'),
        ('7','Domingo'),
    )
    dia = models.CharField(max_length=1, choices=DIAS)
    apertura = models.TimeField()
    cierre = models.TimeField()

    def __str__(self):
        return f'{self.DIAS[int(self.dia)][1]}|{self.apertura.strftime("%H:%M")}-{self.cierre.strftime("%H:%M")}'

class Nodo(models.Model):
    ubicacion = models.OneToOneField(Ubicacion, on_delete=models.CASCADE, verbose_name="Ubicacion")
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        abstract = True

class Sucursal(Nodo):
    disponibilidad = models.OneToOneField(Horario, on_delete=models.CASCADE, verbose_name="Horario", default=1)
    direccion = models.CharField(max_length=100)

class PuntoDeRetiro(Nodo):
    capacidad = models.IntegerField(validators=[MinValueValidator(1)])



