from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from sucursal_crud_api.logger import logParamInfo
from sucursal_crud_api.serializers import NodoSerializer
from sucursal_crud_api.distanciaGeo import DistanciaGeo
from sucursal_crud_api.models import Nodo, Ubicacion

class NearNodeAPIView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = NodoSerializer
    queryset = Nodo.objects.all()
    
    # If use expresion (lat and lng), when parameter is 0  => False
    def validateLocation(self, lat, lng):
        try:
            float(lat)
            float(lng)
            return True
        except:
            return False

    def get(self, request, lat, lng):
        logParamInfo(self, request = request, lat = lat, lng = lng)
        if not self.validateLocation(lat, lng):
            return Response("Invalid request data, try again with float values", 400)

        reqUbicacion = Ubicacion(latitud = float(lat), longitud = float(lng))
        geoDistanceCalculator = DistanciaGeo()

        #Validate at least exist one node
        if not Nodo.objects.exists():
            return Response("It does not exist any node", 200)

        nodo = geoDistanceCalculator.getNodoCercano(list(Nodo.objects.get_queryset()), reqUbicacion)
        return Response(self.serializer_class(nodo).data, 200)
