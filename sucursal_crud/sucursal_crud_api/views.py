from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Sucursal
from .serializers import SucursalSerializer, UbicacionSerializer


class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.DestroyModelMixin,
    mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    serializer_class = SucursalSerializer
    queryset = Sucursal.objects.all()

    lookup_field = 'id'

    def get(self, request, id = None):
        if id: 
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)

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
