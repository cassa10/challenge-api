from django.test import TestCase
from sucursal_crud_api.models import Sucursal, Horario, Ubicacion
import datetime

class SucursalTest(TestCase):

    def test_creacion_sucursal_exitoso(self):
        horario = Horario(
            dia = '7', 
            apertura = datetime.datetime.now(), 
            cierre = datetime.datetime.now()
        )
        ubicacion = Ubicacion(latitud = 10.00001, longitud = 12.00002)
        sucursal = Sucursal(
            disponibilidad = horario, 
            ubicacion = ubicacion,
            direccion = "Primera Junta 123",
            nombre = "Sucursal 1"
        )
        self.assertEquals(sucursal.nombre, "Sucursal 1")
        self.assertEquals(sucursal.disponibilidad, Horario(dia = '7', apertura = horario.apertura, cierre = horario.cierre))
        self.assertEquals(sucursal.ubicacion, Ubicacion(latitud = 10.00001, longitud = 12.00002))
    
    def test_fail_creacion_sucursal_error(self):
        sucursalErronea = Sucursal(nombre = "Sucursal Erronea")
        self.assertNotEquals(sucursalErronea.nombre, None)
        self.assertNotEquals(sucursalErronea.direccion, None)
        self.assertRaises(Horario.DoesNotExist, lambda: sucursalErronea.disponibilidad)
        self.assertRaises(Ubicacion.DoesNotExist, lambda: sucursalErronea.ubicacion)
        
        