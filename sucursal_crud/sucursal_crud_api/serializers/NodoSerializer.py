from rest_framework import serializers
from .UbicacionSerializer import UbicacionSerializer
from sucursal_crud_api.models import Nodo, Ubicacion

class NodoSerializer(serializers.ModelSerializer):
    ubicacion = UbicacionSerializer()
    class Meta:
        model = Nodo
        fields = ['id','nombre','ubicacion']

    def create(self, validated_data):
        ubicacion_data = validated_data.pop('ubicacion')
        ubicacion = Ubicacion.objects.create(**ubicacion_data)
        
        nodo = Nodo.objects.create(**validated_data, ubicacion = ubicacion)
        return nodo

    def update(self, instance, validated_data):
        ubicacion_data = validated_data.pop('ubicacion')
        ubicacion = instance.ubicacion
        ubicacion.latitud = ubicacion_data.get('latitud', ubicacion.latitud)
        ubicacion.longitud = ubicacion_data.get('longitud', ubicacion.longitud)

        instance.nombre = validated_data.get('nombre', instance.nombre)

        instance.save()
        return instance