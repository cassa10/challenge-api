from rest_framework.views import APIView
from rest_framework import status, generics, mixins
from sucursal_crud_api.logger import logParamInfo
from sucursal_crud_api.serializers import NodoSerializer
from sucursal_crud_api.models import Nodo

class NodeAPIView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = NodoSerializer
    queryset = Nodo.objects.all()

    def get(self, request):
        logParamInfo(self, request = request)
        return self.list(request)