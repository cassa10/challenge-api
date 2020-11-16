from django.test import TestCase
from sucursal_crud_api.models import Sucursal

class SucursalTest(TestCase):

    def setUp(self):
        self.sucursal1 = Sucursal(nombre="Sucursal 1")
        self.sucursal2 = Sucursal(nombre="Sucursal 2")

    def tearDown(self):
        pass

    def test_001_sucursal_nombre(self):
        self.assertEqual(self.sucursal1.nombre,"Sucursal 1")
        self.assertEqual(self.sucursal2.nombre,"Sucursal 2")

    def test_002_sucursal_must_fail(self):
        self.assertEqual(1,2)