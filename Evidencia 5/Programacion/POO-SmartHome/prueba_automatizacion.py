"""
Pruebas TDD para la clase Automatizacion - Sistema SmartHome Simplificado
Valida funcionalidad básica de reglas de automatización del hogar
Solo 3 tipos: horario, sensor, manual
"""
import unittest
from clase_automatizacion import Automatizacion

class TestAutomatizacion(unittest.TestCase):
    """
    Suite de pruebas para validar la clase Automatizacion
    Cubre: creación de reglas, condiciones, acciones y tipos de automatización
    """

    def setUp(self):
        """Configurar una regla de automatización de prueba"""
        self.automatizacion = Automatizacion(1, "hora >= 20:00", "encender luces")

    def test_crear_automatizacion(self):
        """Validar que se puede crear una regla de automatización completa"""
        self.assertEqual(self.automatizacion.get_id_auto(), 1)
        self.assertEqual(self.automatizacion.condicion, "hora >= 20:00")
        self.assertEqual(self.automatizacion.accion, "encender luces")

    def test_get_id_auto(self):
        """Validar que se puede obtener el ID único de la automatización"""
        self.assertEqual(self.automatizacion.get_id_auto(), 1)

    def test_obtener_condicion(self):
        """Validar que se puede obtener la condición de activación"""
        self.assertEqual(self.automatizacion.condicion, "hora >= 20:00")

    def test_ver_info_automatizacion(self):
        """Validar que se puede mostrar toda la información de la regla"""
        datos = self.automatizacion.ver_info_automatizacion()
        
        self.assertIn("ID Automatizacion: 1", datos)
        self.assertIn("Condicion: hora >= 20:00", datos)
        self.assertIn("Accion: encender luces", datos)

    def test_diferentes_tipos_automatizacion(self):
        """Validar los 3 tipos de automatización: horario, sensor y manual"""
        auto_horario = Automatizacion(1, "hora >= 22:00", "apagar luces")
        auto_sensor = Automatizacion(2, "temperatura < 18°C", "activar calefacción")
        auto_manual = Automatizacion(3, "usuario presiona botón", "encender cámara")
        
        # Todas deben crearse correctamente
        self.assertEqual(auto_horario.get_id_auto(), 1)
        self.assertEqual(auto_sensor.get_id_auto(), 2)
        self.assertEqual(auto_manual.get_id_auto(), 3)

if __name__ == "__main__":
    unittest.main()