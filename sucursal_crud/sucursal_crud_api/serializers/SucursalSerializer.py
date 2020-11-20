from rest_framework import serializers
from .UbicacionSerializer import UbicacionSerializer
from .HorarioSerializer import HorarioSerializer
from sucursal_crud_api.models import Sucursal, Ubicacion, Horario

class SucursalSerializer(serializers.ModelSerializer):
    ubicacion = UbicacionSerializer()
    disponibilidad = HorarioSerializer()
    class Meta:
        model = Sucursal
        fields = ['id','nombre','direccion','ubicacion','disponibilidad']
    
    def create(self, validated_data):
        ubicacion_data = validated_data.pop('ubicacion')
        ubicacion = Ubicacion.objects.create(**ubicacion_data)

        disponibilidad_data = validated_data.pop('disponibilidad')
        disponibilidad = Horario.objects.create(**disponibilidad_data)
        
        sucursal = Sucursal.objects.create(**validated_data, ubicacion = ubicacion, disponibilidad = disponibilidad)
        return sucursal
    
    def update(self, instance, validated_data):
        ubicacion_data = validated_data.pop('ubicacion')
        ubicacion = instance.ubicacion
        ubicacion.latitud = ubicacion_data.get('latitud', ubicacion.latitud)
        ubicacion.longitud = ubicacion_data.get('longitud', ubicacion.longitud)

        disponibilidad_data = validated_data.pop('disponibilidad')
        disponibilidad = instance.disponibilidad
        disponibilidad.dia = disponibilidad_data.get('dia',disponibilidad.dia)
        disponibilidad.apertura = disponibilidad_data.get('apertura',disponibilidad.apertura)
        disponibilidad.cierre = disponibilidad_data.get('cierre',disponibilidad.cierre)

        instance.direccion = validated_data.get('direccion', instance.direccion)
        instance.nombre = validated_data.get('nombre', instance.nombre)

        instance.save()
        return instance