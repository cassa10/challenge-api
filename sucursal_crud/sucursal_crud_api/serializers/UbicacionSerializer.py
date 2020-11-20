from rest_framework import serializers
from sucursal_crud_api.models import Ubicacion

class UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ubicacion
        fields = ['id','latitud','longitud']