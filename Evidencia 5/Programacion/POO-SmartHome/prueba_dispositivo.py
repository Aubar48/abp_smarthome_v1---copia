"""
Pruebas TDD para la clase Dispositivo - Sistema SmartHome Simplificado
Valida funcionalidad básica de dispositivos IoT: luces, sensores y cámaras
Solo 3 tipos: luz, sensor, camara
"""
import unittest
from clase_dispositivo import Dispositivo

class TestDispositivo(unittest.TestCase):
    """
    Suite de pruebas para validar la clase Dispositivo
    Cubre: creación de dispositivos, control de estados y tipos válidos
    """

    def setUp(self):
        """Configurar dispositivos de prueba: uno de cada tipo"""
        self.luz = Dispositivo(1, "Luz Test", "luz")
        self.sensor = Dispositivo(2, "Sensor Test", "sensor")
        self.camara = Dispositivo(3, "Camara Test", "camara")

    def test_crear_dispositivo_luz(self):
        """Validar que se puede crear un dispositivo tipo luz correctamente"""
        self.assertEqual(self.luz.get_id_dispositivo(), 1)
        self.assertEqual(self.luz._nombre_dispositivo, "Luz Test")
        self.assertEqual(self.luz._tipo, "luz")
        self.assertEqual(self.luz._estado, "apagado")

    def test_encender_dispositivo(self):
        """Validar que se puede encender un dispositivo desde estado apagado"""
        self.luz.encender()
        self.assertEqual(self.luz._estado, "encendido")

    def test_apagar_dispositivo(self):
        """Validar que se puede apagar un dispositivo desde estado encendido"""
        self.luz._estado = "encendido"
        self.luz.apagar()
        self.assertEqual(self.luz._estado, "apagado")

    def test_solo_tres_tipos(self):
        """Validar que el sistema maneja exactamente 3 tipos de dispositivos"""
        tipos = [self.luz._tipo, self.sensor._tipo, self.camara._tipo]
        tipos_validos = ['luz', 'sensor', 'camara']
        
        for tipo in tipos:
            self.assertIn(tipo, tipos_validos)

    def test_solo_dos_estados(self):
        """Validar que los dispositivos solo pueden estar encendidos o apagados"""
        estados_validos = ['encendido', 'apagado']
        self.assertIn(self.luz._estado, estados_validos)
        
        self.luz.encender()
        self.assertIn(self.luz._estado, estados_validos)

if __name__ == "__main__":
    unittest.main()
