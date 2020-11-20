from rest_framework import serializers
from sucursal_crud_api.models import Horario

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = ['id','dia','apertura','cierre']