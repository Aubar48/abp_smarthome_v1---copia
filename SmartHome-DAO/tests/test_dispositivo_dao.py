"""
Pruebas unitarias para DispositivoDAO
"""

from app.dominio.usuario import Usuario
from app.dominio.vivienda import Vivienda
from app.dominio.dispositivo import Dispositivo
from app.dao.usuario_dao import UsuarioDAO
from app.dao.vivienda_dao import ViviendaDAO
from app.dao.dispositivo_dao import DispositivoDAO
import unittest
import sys
import os

# Agregar el path del proyecto para importar módulos
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


class TestDispositivoDAO(unittest.TestCase):
    """Pruebas para DispositivoDAO"""

    def setUp(self):
        """Configuración antes de cada prueba"""
        self.dispositivo_dao = DispositivoDAO()
        self.vivienda_dao = ViviendaDAO()
        self.usuario_dao = UsuarioDAO()

        # Crear usuario y vivienda de prueba
        usuario_test = Usuario(None, "admin_disp@test.com",
                               "Admin Test", "pass123", "administrador")
        self.id_admin = self.usuario_dao.crear(usuario_test)

        vivienda_test = Vivienda(
            None, "Casa Dispositivos", "Test 456", self.id_admin)
        self.id_vivienda = self.vivienda_dao.crear(vivienda_test)

        self.test_dispositivo_ids = []

    def tearDown(self):
        """Limpieza después de cada prueba"""
        # Eliminar dispositivos
        for id_disp in self.test_dispositivo_ids:
            try:
                self.dispositivo_dao.eliminar(id_disp)
            except:
                pass

        # Eliminar vivienda y usuario
        try:
            self.vivienda_dao.eliminar(self.id_vivienda)
            self.usuario_dao.eliminar(self.id_admin)
        except:
            pass

    def test_crear_dispositivo(self):
        """Prueba crear un nuevo dispositivo"""
        dispositivo = Dispositivo(
            None, "Luz Test", "luz", "apagado", "Sala Test", self.id_vivienda)
        id_dispositivo = self.dispositivo_dao.crear(dispositivo)
        self.test_dispositivo_ids.append(id_dispositivo)

        self.assertIsNotNone(id_dispositivo)
        self.assertGreater(id_dispositivo, 0)

    def test_obtener_dispositivo_por_id(self):
        """Prueba obtener dispositivo por ID"""
        # Crear dispositivo
        dispositivo = Dispositivo(
            None, "Sensor Test", "sensor", "encendido", "Cocina", self.id_vivienda)
        id_dispositivo = self.dispositivo_dao.crear(dispositivo)
        self.test_dispositivo_ids.append(id_dispositivo)

        # Obtener dispositivo
        dispositivo_obtenido = self.dispositivo_dao.obtener_por_id(
            id_dispositivo)
        self.assertIsNotNone(dispositivo_obtenido)
        self.assertEqual(
            dispositivo_obtenido.nombre_dispositivo, "Sensor Test")
        self.assertEqual(dispositivo_obtenido.tipo, "sensor")

    def test_obtener_dispositivos_por_vivienda(self):
        """Prueba obtener dispositivos de una vivienda"""
        # Crear varios dispositivos
        disp1 = Dispositivo(None, "Luz 1", "luz", "apagado",
                            "Sala", self.id_vivienda)
        disp2 = Dispositivo(None, "Sensor 1", "sensor",
                            "encendido", "Cocina", self.id_vivienda)

        id1 = self.dispositivo_dao.crear(disp1)
        id2 = self.dispositivo_dao.crear(disp2)
        self.test_dispositivo_ids.extend([id1, id2])

        # Obtener dispositivos
        dispositivos = self.dispositivo_dao.obtener_por_vivienda(
            self.id_vivienda)
        self.assertGreaterEqual(len(dispositivos), 2)

    def test_actualizar_dispositivo(self):
        """Prueba actualizar estado de dispositivo"""
        # Crear dispositivo
        dispositivo = Dispositivo(
            None, "Luz Test", "luz", "apagado", "Sala", self.id_vivienda)
        id_dispositivo = self.dispositivo_dao.crear(dispositivo)
        self.test_dispositivo_ids.append(id_dispositivo)

        # Actualizar
        dispositivo_obtenido = self.dispositivo_dao.obtener_por_id(
            id_dispositivo)
        dispositivo_obtenido.estado = "encendido"
        self.dispositivo_dao.actualizar(dispositivo_obtenido)

        # Verificar
        dispositivo_verificado = self.dispositivo_dao.obtener_por_id(
            id_dispositivo)
        self.assertEqual(dispositivo_verificado.estado, "encendido")

    def test_obtener_todos_dispositivos(self):
        """Prueba obtener todos los dispositivos"""
        # Crear dispositivo
        dispositivo = Dispositivo(
            None, "Camara Test", "camara", "encendido", "Entrada", self.id_vivienda)
        id_dispositivo = self.dispositivo_dao.crear(dispositivo)
        self.test_dispositivo_ids.append(id_dispositivo)

        # Obtener todos
        dispositivos = self.dispositivo_dao.obtener_todos()
        self.assertIsNotNone(dispositivos)
        self.assertGreater(len(dispositivos), 0)

    def test_eliminar_dispositivo(self):
        """Prueba eliminar dispositivo"""
        # Crear dispositivo
        dispositivo = Dispositivo(
            None, "Luz Delete", "luz", "apagado", "Test", self.id_vivienda)
        id_dispositivo = self.dispositivo_dao.crear(dispositivo)

        # Eliminar
        self.dispositivo_dao.eliminar(id_dispositivo)

        # Verificar que no existe
        dispositivo_eliminado = self.dispositivo_dao.obtener_por_id(
            id_dispositivo)
        self.assertIsNone(dispositivo_eliminado)


if __name__ == '__main__':
    unittest.main(verbosity=2)
