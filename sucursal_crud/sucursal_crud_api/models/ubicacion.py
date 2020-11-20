from django.db import models

class Ubicacion(models.Model):
    latitud = models.DecimalField(max_digits=9, decimal_places=6)
    longitud = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return f'{self.latitud}, {self.longitud}'
    
    def __eq__(self, obj):
        if isinstance(obj, Ubicacion):
                return (self.latitud == obj.latitud and self.longitud == obj.longitud)
        return False
