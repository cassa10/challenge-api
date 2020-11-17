from django.test import TestCase
from sucursal_crud_api.distanciaGeo import DistanciaGeo
from sucursal_crud_api.models import Ubicacion

class DistanciaGeoTest(TestCase):

    def setUp(self):
        self.calculadoraDistancia = DistanciaGeo()

    def test_distancia_entre_ubicacionA_ubicacionA_es_0(self):
        ubicacionA = Ubicacion(latitud = 10.00000, longitud = 12.0000)
        distancia = self.calculadoraDistancia.distanciaEnMetros(ubicacionA, ubicacionA)
        self.assertEqual(distancia, 0)
    
    #Distancia de tolerancia 10 metros
    def test_distancia_entre_ubicacionA_ubicacionB_es_1260metros(self):
        ubicacionA = Ubicacion(latitud = -34.706566, longitud = -58.277687)
        ubicacionB = Ubicacion(latitud = -34.698114, longitud = -58.286888)
        distancia = self.calculadoraDistancia.distanciaEnMetros(ubicacionA, ubicacionB)
        delta = 10
        self.assertAlmostEqual(distancia, 1260, None, None, delta)
