from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view
from .models import Sucursal, PuntoDeRetiro, Nodo, Ubicacion
from .distanciaGeo import DistanciaGeo
from .serializers import SucursalSerializer, UbicacionSerializer, PuntoDeRetiroSerializer, NodoSerializer
import logging
import inspect

logger = logging.getLogger(__name__)

# normal arguments are ignored, used keyword arguments for logging
# kwargs can be n params
def logParamInfo(source, **kwargs):
    params = []
    for key, value in kwargs.items():
        params.append(f'{key}: {value}')
    
    logger.info(f' ({source.__class__.__name__}.{inspect.stack()[1][3]}) - Parameters: {params}')

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

class NodeAPIView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = NodoSerializer
    queryset = Nodo.objects.all()

    def get(self, request):
        logParamInfo(self, request = request)
        return self.list(request)

class SucursalAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = SucursalSerializer
    queryset = Sucursal.objects.all()
    
    def get(self, request):
        logParamInfo(self, request = request)
        return self.list(request)

    def post(self, request):
        logParamInfo(self, request = request)
        return self.create(request)

class SucursalDetailAPIView(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    serializer_class = SucursalSerializer
    queryset = Sucursal.objects.all()

    lookup_field = 'id'

    def get(self, request, id):
        logParamInfo(self, request = request, id = id)
        return self.retrieve(request)


    def put(self, request, id):
        logParamInfo(self, request = request, id = id)
        self.validateId(id)
        return self.update(request, id)

    def delete(self, request, id):
        logParamInfo(self, request = request, id = id)
        self.validateId(id)
        return self.destroy(request, id)


class PuntoDeRetiroAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = PuntoDeRetiroSerializer
    queryset = PuntoDeRetiro.objects.all()

    def get(self, request):
        logParamInfo(self, request = request)
        return self.list(request)

    def post(self, request):
        logParamInfo(self, request = request)
        return self.create(request)

class PuntoDeRetiroDetailAPIView(generics.GenericAPIView, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    serializer_class = PuntoDeRetiroSerializer
    queryset = PuntoDeRetiro.objects.all()
    
    lookup_field = 'id'

    def get(self, request, id):
        logParamInfo(self, request = request, id = id)
        return self.retrieve(request)

    def put(self, request, id):
        logParamInfo(self, request = request, id = id)
        return self.update(request, id)

    def delete(self, request, id):
        logParamInfo(self, request = request, id = id)
        return self.destroy(request, id)
"""
class SucursalApiView(APIView):
    serializer_class = SucursalSerializer
    def get(self, request):
        sucursales = Sucursal.objects.all()
        serializer = self.serializer_class(sucursales, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class SucursalInfoApiView(APIView):
    serializer_class = SucursalSerializer
    def get_object(self, id):
        try:
            return Sucursal.objects.get(id = id)

        except Sucursal.DoesNotExist:
            return HttpResponse(status = status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        sucursal = self.get_object(id)
        serializer = self.serializer_class(sucursal)
        return Response(serializer.data)

    def put(self, request, id):
        sucursal = self.get_object(id)
        serializer = self.serializer_class(sucursal, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        sucursal = self.get_object(id)
        sucursal.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
"""