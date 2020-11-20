from django.test import TestCase
from sucursal_crud_api.utils.distanciaGeo import DistanciaGeo
from sucursal_crud_api.models import Ubicacion, Nodo

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

    def test_obtener_nodo_mas_cercano_de_lista_de_nodos(self):
        #UNQ (Universidad Nacional de Quilmes)
        nodoUNQ = Nodo(nombre = "Universidad Nacional de Quilmes", ubicacion = Ubicacion(latitud = -34.706566, longitud = -58.277687))

        #Plaza San Martin (Centro de Quilmes)
        nodoPSM = Nodo(nombre = "Plaza San Martin (Centro de Quilmes)", ubicacion = Ubicacion(latitud = -34.7200588, longitud = -58.2544012))

        #Mar del Plata (mdq)
        nodoMDQ = Nodo(nombre = "Mar del Plata", ubicacion = Ubicacion(latitud = -38.005004, longitud = -57.542606))
        
        nodos = [nodoMDQ, nodoUNQ, nodoPSM]

        ubicacionCercaDeUNQ = Ubicacion(latitud = -34.7065660, longitud = -58.2776870)

        ubicacionCercaDePSM = Ubicacion(latitud = -34.7200588, longitud = -58.2544012)

        ubicacionCercaDeMDQ = Ubicacion(latitud = -38.0050040, longitud = -57.5426060)

        self.assertEquals(nodoUNQ, self.calculadoraDistancia.getNodoCercano(nodos, ubicacionCercaDeUNQ))

        self.assertEquals(nodoPSM, self.calculadoraDistancia.getNodoCercano(nodos, ubicacionCercaDePSM))

        self.assertEquals(nodoMDQ, self.calculadoraDistancia.getNodoCercano(nodos, ubicacionCercaDeMDQ))
