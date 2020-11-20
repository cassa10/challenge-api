from rest_framework.views import APIView
from rest_framework import status, generics, mixins
from sucursal_crud_api.models import PuntoDeRetiro
from sucursal_crud_api.serializers import PuntoDeRetiroSerializer
from sucursal_crud_api.logger import logParamInfo

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