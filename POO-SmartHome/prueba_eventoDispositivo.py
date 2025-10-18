"""
Pruebas TDD para la clase EventoDispositivo - Sistema SmartHome Simplificado
Valida funcionalidad básica de registro de eventos de dispositivos IoT
"""
import unittest
from datetime import datetime
from clase_eventoDispositivo import EventoDispositivo

class TestEventoDispositivo(unittest.TestCase):
    """
    Suite de pruebas para validar la clase EventoDispositivo
    Cubre: creación de eventos, acceso a propiedades y registro de actividades
    """

    def setUp(self):
        """Configurar un evento de prueba con timestamp actual"""
        self.fecha_test = datetime.now()
        self.evento = EventoDispositivo(1, self.fecha_test, "Dispositivo encendido", "encendido")

    def test_crear_evento(self):
        """Validar que se puede crear un evento con todos sus datos"""
        self.assertEqual(self.evento.id_evento, 1)
        self.assertEqual(self.evento.fecha_hora, self.fecha_test)
        self.assertEqual(self.evento.detalle, "Dispositivo encendido")
        self.assertEqual(self.evento.valor, "encendido")

    def test_obtener_id_evento(self):
        """Validar que se puede obtener el ID único del evento"""
        self.assertEqual(self.evento.id_evento, 1)

    def test_obtener_fecha_evento(self):
        """Validar que se puede obtener la fecha y hora del evento"""
        self.assertEqual(self.evento.fecha_hora, self.fecha_test)

    def test_obtener_detalle_evento(self):
        """Validar que se puede obtener la descripción del evento"""
        self.assertEqual(self.evento.detalle, "Dispositivo encendido")

    def test_obtener_valor_evento(self):
        """Validar que se puede obtener el valor/estado del evento"""
        self.assertEqual(self.evento.valor, "encendido")

if __name__ == "__main__":
    unittest.main()