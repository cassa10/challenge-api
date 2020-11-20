from rest_framework import serializers
from .UbicacionSerializer import UbicacionSerializer
from sucursal_crud_api.models import Ubicacion, PuntoDeRetiro

class PuntoDeRetiroSerializer(serializers.ModelSerializer):
    ubicacion = UbicacionSerializer()
    class Meta:
        model = PuntoDeRetiro
        fields = ['id','nombre','capacidad','ubicacion']
    
    def create(self, validated_data):
        ubicacion_data = validated_data.pop('ubicacion')
        ubicacion = Ubicacion.objects.create(**ubicacion_data)
        puntoDeRetiro = PuntoDeRetiro.objects.create(**validated_data, ubicacion = ubicacion)
        return puntoDeRetiro
    
    def update(self, instance, validated_data):
        ubicacion_data = validated_data.pop('ubicacion')
        ubicacion = instance.ubicacion
        ubicacion.latitud = ubicacion_data.get('latitud', ubicacion.latitud)
        ubicacion.longitud = ubicacion_data.get('longitud', ubicacion.longitud)

        instance.capacidad = validated_data.get('capacidad', instance.capacidad)
        instance.nombre = validated_data.get('nombre', instance.nombre)

        instance.save()
        return instance
