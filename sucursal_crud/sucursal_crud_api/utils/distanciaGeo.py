import haversine as hs
from haversine import Unit
from .models import Ubicacion

class DistanciaGeo():

    def distanciaEnMetros(self, ubicacion1, ubicacion2):
        return hs.haversine((ubicacion1.latitud, ubicacion1.longitud),(ubicacion2.latitud,ubicacion2.longitud), unit=Unit.METERS)

    def distanciaEnMillas(self, ubicacion1, ubicacion2):
        return hs.haversine((ubicacion1.latitud,ubicacion1.longitud),(ubicacion2.latitud,ubicacion2.longitud),unit=Unit.MILES)

    # Nodos size > 0
    def getNodoCercano(self, nodos, ubicacion):
        nodoCercano = nodos[0]
        minDistance = self.distanciaEnMetros(nodoCercano.ubicacion, ubicacion)
        for nodo in nodos:
            tmpDistance = self.distanciaEnMetros(nodo.ubicacion, ubicacion)
            if minDistance > tmpDistance:
                nodoCercano = nodo
                minDistance = tmpDistance
            
        return nodoCercano