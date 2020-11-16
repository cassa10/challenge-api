from django.contrib import admin
from .models import Sucursal, PuntoDeRetiro, Ubicacion, Horario

admin.site.register(Horario)
admin.site.register(Ubicacion)
admin.site.register(Sucursal)
admin.site.register(PuntoDeRetiro)
