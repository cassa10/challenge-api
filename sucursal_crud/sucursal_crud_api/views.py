from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    
    def get(self, request, format=None):
        an_apiview = [
            'Hola',
            'WACHEEEM'
        ]
        return Response({'message': 'Holandaa', 'am_apiview': an_apiview})
