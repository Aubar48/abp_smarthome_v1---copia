"""
Pruebas unitarias para EventoDispositivoDAO
"""

from app.dominio.usuario import Usuario
from app.dominio.vivienda import Vivienda
from app.dominio.dispositivo import Dispositivo
from app.dominio.evento_dispositivo import EventoDispositivo
from app.dao.usuario_dao import UsuarioDAO
from app.dao.vivienda_dao import ViviendaDAO
from app.dao.dispositivo_dao import DispositivoDAO
from app.dao.evento_dispositivo_dao import EventoDispositivoDAO
import unittest
import sys
import os

# Agregar el path del proyecto para importar módulos
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


class TestEventoDispositivoDAO(unittest.TestCase):
    """Pruebas para EventoDispositivoDAO"""

    def setUp(self):
        """Configuración antes de cada prueba"""
        self.evento_dao = EventoDispositivoDAO()
        self.dispositivo_dao = DispositivoDAO()
        self.vivienda_dao = ViviendaDAO()
        self.usuario_dao = UsuarioDAO()

        # Crear usuario, vivienda y dispositivo de prueba
        usuario_test = Usuario(None, "admin_evento@test.com",
                               "Admin Test", "pass123", "administrador")
        self.id_usuario = self.usuario_dao.crear(usuario_test)

        vivienda_test = Vivienda(None, "Casa Eventos",
                                 "Test 789", self.id_usuario)
        self.id_vivienda = self.vivienda_dao.crear(vivienda_test)

        dispositivo_test = Dispositivo(
            None, "Luz Eventos", "luz", "apagado", "Sala", self.id_vivienda)
        self.id_dispositivo = self.dispositivo_dao.crear(dispositivo_test)

        self.test_evento_ids = []

    def tearDown(self):
        """Limpieza después de cada prueba"""
        # Eliminar eventos
        for id_evento in self.test_evento_ids:
            try:
                self.evento_dao.eliminar(id_evento)
            except:
                pass

        # Eliminar dispositivo, vivienda y usuario
        try:
            self.dispositivo_dao.eliminar(self.id_dispositivo)
            self.vivienda_dao.eliminar(self.id_vivienda)
            self.usuario_dao.eliminar(self.id_usuario)
        except:
            pass

    def test_crear_evento(self):
        """Prueba crear un nuevo evento"""
        evento = EventoDispositivo(None, self.id_dispositivo, self.id_usuario,
                                   "encendido", None, "Prueba de evento")
        id_evento = self.evento_dao.crear(evento)
        self.test_evento_ids.append(id_evento)

        self.assertIsNotNone(id_evento)
        self.assertGreater(id_evento, 0)

    def test_obtener_evento_por_id(self):
        """Prueba obtener evento por ID"""
        # Crear evento
        evento = EventoDispositivo(None, self.id_dispositivo, self.id_usuario,
                                   "apagado", None, "Evento de prueba")
        id_evento = self.evento_dao.crear(evento)
        self.test_evento_ids.append(id_evento)

        # Obtener evento
        evento_obtenido = self.evento_dao.obtener_por_id(id_evento)
        self.assertIsNotNone(evento_obtenido)
        self.assertEqual(evento_obtenido.tipo_evento, "apagado")
        self.assertEqual(evento_obtenido.detalle, "Evento de prueba")

    def test_obtener_eventos_por_dispositivo(self):
        """Prueba obtener eventos de un dispositivo"""
        # Crear varios eventos
        evento1 = EventoDispositivo(None, self.id_dispositivo, self.id_usuario,
                                    "encendido", None, "Evento 1")
        evento2 = EventoDispositivo(None, self.id_dispositivo, self.id_usuario,
                                    "apagado", None, "Evento 2")

        id1 = self.evento_dao.crear(evento1)
        id2 = self.evento_dao.crear(evento2)
        self.test_evento_ids.extend([id1, id2])

        # Obtener eventos
        eventos = self.evento_dao.obtener_por_dispositivo_id(
            self.id_dispositivo)
        self.assertGreaterEqual(len(eventos), 2)

    def test_obtener_todos_eventos(self):
        """Prueba obtener todos los eventos"""
        # Crear evento
        evento = EventoDispositivo(None, self.id_dispositivo, self.id_usuario,
                                   "configuracion", None, "Configuración inicial")
        id_evento = self.evento_dao.crear(evento)
        self.test_evento_ids.append(id_evento)

        # Obtener todos
        eventos = self.evento_dao.obtener_todos()
        self.assertIsNotNone(eventos)
        self.assertGreater(len(eventos), 0)

    def test_eliminar_evento(self):
        """Prueba eliminar evento"""
        # Crear evento
        evento = EventoDispositivo(None, self.id_dispositivo, self.id_usuario,
                                   "encendido", None, "Evento a eliminar")
        id_evento = self.evento_dao.crear(evento)

        # Eliminar
        self.evento_dao.eliminar(id_evento)

        # Verificar que no existe
        evento_eliminado = self.evento_dao.obtener_por_id(id_evento)
        self.assertIsNone(evento_eliminado)


if __name__ == '__main__':
    unittest.main(verbosity=2)
