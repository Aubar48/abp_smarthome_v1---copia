"""
Pruebas TDD para la clase Vivienda - Sistema SmartHome Simplificado
Valida funcionalidad básica de gestión de propiedades/casas
"""
import unittest
from clase_vivienda import Vivienda

class TestVivienda(unittest.TestCase):
    """
    Suite de pruebas para validar la clase Vivienda
    Cubre: creación de viviendas, acceso a datos y formato de información
    """

    def setUp(self):
        """Configurar una vivienda de prueba con datos básicos"""
        self.vivienda = Vivienda(1, "Calle 123", "Casa Test")

    def test_crear_vivienda(self):
        """Validar que se puede crear una vivienda con todos sus datos"""
        self.assertEqual(self.vivienda.get_id_vivienda(), 1)
        self.assertEqual(self.vivienda.get_ubicacion(), "Calle 123")
        self.assertEqual(self.vivienda._nombre_vivienda, "Casa Test")

    def test_get_id_vivienda(self):
        """Validar que se puede obtener el ID único de la vivienda"""
        self.assertEqual(self.vivienda.get_id_vivienda(), 1)

    def test_ver_datos_vivienda(self):
        """Validar que se pueden mostrar todos los datos de la vivienda"""
        datos = self.vivienda.ver_datos_vivienda()
        
        self.assertIn("ID_vivienda: 1", datos)
        self.assertIn("Nombre_vivienda: Casa Test", datos)
        self.assertIn("Ubicacion: Calle 123", datos)

    def test_registrar_nueva_vivienda(self):
        """Validar que el método de registro funciona (placeholder)"""
        # Método placeholder que no retorna nada
        resultado = self.vivienda.registrar_nueva_vivienda(2, "Calle 456", "Casa Nueva")
        self.assertIsNone(resultado)

    def test_datos_vivienda_formato_correcto(self):
        """Validar que los datos se muestran en el formato correcto"""
        datos = self.vivienda.ver_datos_vivienda()
        lineas = datos.split('\n')
        
        self.assertEqual(lineas[0], "ID_vivienda: 1")
        self.assertEqual(lineas[1], "Nombre_vivienda: Casa Test")
        self.assertEqual(lineas[2], "Ubicacion: Calle 123")

if __name__ == "__main__":
    unittest.main()
