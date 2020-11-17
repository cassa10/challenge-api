from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view
from .models import Sucursal, PuntoDeRetiro
from .serializers import SucursalSerializer, UbicacionSerializer, PuntoDeRetiroSerializer
import logging
import inspect

logger = logging.getLogger(__name__)

def logParamInfo(source, request, id = None):
    logger.info(f' ({source.__class__.__name__}.{inspect.stack()[1][3]}) - Parameters: request = {request}, id = {id}')

class HelloApiView(APIView):
    def get(self, request):
        logParamInfo(self, request)
        return Response("Welcome to my api :D ! Available endpoints: [/api/sucursal," + 
        " /api/sucursal/<id>, /api/puntoDeRetiro, /api/puntoDeRetiro/<id>," +
        " /api/node/near ]"
        , 200)

class SucursalAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.DestroyModelMixin,
    mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    serializer_class = SucursalSerializer
    queryset = Sucursal.objects.all()

    lookup_field = 'id'

    def get(self, request, id = None):
        logParamInfo(self, request, id)
        if id: 
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        logParamInfo(self, request)
        return self.create(request)

    def put(self, request, id=None):
        logParamInfo(self, request, id)
        return self.update(request, id)

    def delete(self, request, id):
        logParamInfo(self, request, id)
        return self.destroy(request, id)

class PuntoDeRetiroAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.DestroyModelMixin,
    mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    
    serializer_class = PuntoDeRetiroSerializer
    queryset = PuntoDeRetiro.objects.all()

    lookup_field = 'id'

    def get(self, request, id = None):
        logParamInfo(self, request, id)
        if id: 
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        logParamInfo(self, request)
        return self.create(request)

    def put(self, request, id=None):
        logParamInfo(self, request, id)
        return self.update(request, id)

    def delete(self, request, id):
        logParamInfo(self, request, id)
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