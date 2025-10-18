"""
Pruebas unitarias para los DAOs del sistema SmartHome
Ejecutar con: python -m unittest tests/test_daos.py
"""

from app.dominio.evento_dispositivo import EventoDispositivo
from app.dominio.dispositivo import Dispositivo
from app.dominio.vivienda import Vivienda
from app.dominio.usuario import Usuario
from app.dao.evento_dispositivo_dao import EventoDispositivoDAO
from app.dao.dispositivo_dao import DispositivoDAO
from app.dao.vivienda_dao import ViviendaDAO
from app.dao.usuario_dao import UsuarioDAO
import unittest
import sys
import os

# Agregar el path del proyecto para importar módulos
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


class TestUsuarioDAO(unittest.TestCase):
    """Pruebas para UsuarioDAO"""

    def setUp(self):
        """Configuración antes de cada prueba"""
        self.usuario_dao = UsuarioDAO()
        self.test_email = "test_usuario@test.com"

    def tearDown(self):
        """Limpieza después de cada prueba"""
        # Intentar eliminar el usuario de prueba si existe
        try:
            usuario = self.usuario_dao.obtener_por_email(self.test_email)
            if usuario:
                self.usuario_dao.eliminar(usuario.id_usuario)
        except:
            pass

    def test_crear_usuario(self):
        """Prueba crear un nuevo usuario"""
        usuario = Usuario(None, self.test_email,
                          "Usuario Test", "pass123", "usuario")
        id_usuario = self.usuario_dao.crear(usuario)
        self.assertIsNotNone(id_usuario)
        self.assertGreater(id_usuario, 0)

    def test_obtener_usuario_por_email(self):
        """Prueba obtener usuario por email"""
        # Crear usuario
        usuario = Usuario(None, self.test_email,
                          "Usuario Test", "pass123", "usuario")
        self.usuario_dao.crear(usuario)

        # Obtener usuario
        usuario_obtenido = self.usuario_dao.obtener_por_email(self.test_email)
        self.assertIsNotNone(usuario_obtenido)
        self.assertEqual(usuario_obtenido.email, self.test_email)
        self.assertEqual(usuario_obtenido.nombre, "Usuario Test")

    def test_actualizar_usuario(self):
        """Prueba actualizar datos de usuario"""
        # Crear usuario
        usuario = Usuario(None, self.test_email,
                          "Usuario Test", "pass123", "usuario")
        id_usuario = self.usuario_dao.crear(usuario)

        # Obtener y actualizar
        usuario_obtenido = self.usuario_dao.obtener_por_id(id_usuario)
        usuario_obtenido.nombre = "Nombre Actualizado"
        self.usuario_dao.actualizar(usuario_obtenido)

        # Verificar actualización
        usuario_verificado = self.usuario_dao.obtener_por_id(id_usuario)
        self.assertEqual(usuario_verificado.nombre, "Nombre Actualizado")

    def test_eliminar_usuario(self):
        """Prueba eliminar usuario"""
        # Crear usuario
        usuario = Usuario(None, self.test_email,
                          "Usuario Test", "pass123", "usuario")
        id_usuario = self.usuario_dao.crear(usuario)

        # Eliminar
        self.usuario_dao.eliminar(id_usuario)

        # Verificar que no existe
        usuario_eliminado = self.usuario_dao.obtener_por_id(id_usuario)
        self.assertIsNone(usuario_eliminado)


class TestViviendaDAO(unittest.TestCase):
    """Pruebas para ViviendaDAO"""

    def setUp(self):
        """Configuración antes de cada prueba"""
        self.vivienda_dao = ViviendaDAO()
        self.usuario_dao = UsuarioDAO()

        # Crear un usuario administrador de prueba
        usuario_test = Usuario(None, "admin_test@test.com",
                               "Admin Test", "pass123", "administrador")
        self.id_admin = self.usuario_dao.crear(usuario_test)
        self.test_vivienda_ids = []

    def tearDown(self):
        """Limpieza después de cada prueba"""
        # Eliminar viviendas de prueba
        for id_vivienda in self.test_vivienda_ids:
            try:
                self.vivienda_dao.eliminar(id_vivienda)
            except:
                pass

        # Eliminar usuario administrador de prueba
        try:
            self.usuario_dao.eliminar(self.id_admin)
        except:
            pass

    def test_crear_vivienda(self):
        """Prueba crear una nueva vivienda"""
        vivienda = Vivienda(None, "Casa Test", "Calle Test 123", self.id_admin)
        id_vivienda = self.vivienda_dao.crear(vivienda)
        self.test_vivienda_ids.append(id_vivienda)

        self.assertIsNotNone(id_vivienda)
        self.assertGreater(id_vivienda, 0)

    def test_obtener_vivienda_por_id(self):
        """Prueba obtener vivienda por ID"""
        # Crear vivienda
        vivienda = Vivienda(None, "Casa Test", "Calle Test 123", self.id_admin)
        id_vivienda = self.vivienda_dao.crear(vivienda)
        self.test_vivienda_ids.append(id_vivienda)

        # Obtener vivienda
        vivienda_obtenida = self.vivienda_dao.obtener_por_id(id_vivienda)
        self.assertIsNotNone(vivienda_obtenida)
        self.assertEqual(vivienda_obtenida.nombre_vivienda, "Casa Test")
        self.assertEqual(vivienda_obtenida.direccion, "Calle Test 123")

    def test_asignar_usuario_a_vivienda(self):
        """Prueba asignar usuario a vivienda"""
        # Crear usuario y vivienda
        usuario = Usuario(None, "usuario_test@test.com",
                          "Usuario Test", "pass123", "usuario")
        id_usuario = self.usuario_dao.crear(usuario)

        vivienda = Vivienda(None, "Casa Test", "Calle Test 123", self.id_admin)
        id_vivienda = self.vivienda_dao.crear(vivienda)
        self.test_vivienda_ids.append(id_vivienda)

        # Asignar usuario
        resultado = self.vivienda_dao.asignar_usuario(id_usuario, id_vivienda)
        self.assertTrue(resultado)

        # Verificar asignación duplicada
        resultado_duplicado = self.vivienda_dao.asignar_usuario(
            id_usuario, id_vivienda)
        self.assertFalse(resultado_duplicado)

        # Limpiar
        self.vivienda_dao.desasignar_todas_viviendas_usuario(id_usuario)
        self.usuario_dao.eliminar(id_usuario)


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


class TestEncapsulacionDominio(unittest.TestCase):
    """Pruebas para verificar encapsulación de clases de dominio"""

    def test_usuario_encapsulacion(self):
        """Prueba que Usuario usa properties correctamente"""
        usuario = Usuario(1, "test@test.com", "Test", "pass", "usuario")

        # Verificar getters
        self.assertEqual(usuario.id_usuario, 1)
        self.assertEqual(usuario.email, "test@test.com")

        # Verificar setters
        usuario.nombre = "Nuevo Nombre"
        self.assertEqual(usuario.nombre, "Nuevo Nombre")

        # Verificar validación de rol
        with self.assertRaises(ValueError):
            usuario.rol = "rol_invalido"

    def test_dispositivo_validaciones(self):
        """Prueba validaciones en Dispositivo"""
        dispositivo = Dispositivo(1, "Luz", "luz", "apagado", "Sala", 1)

        # Validar tipo
        with self.assertRaises(ValueError):
            dispositivo.tipo = "tipo_invalido"

        # Validar estado
        with self.assertRaises(ValueError):
            dispositivo.estado = "estado_invalido"


if __name__ == '__main__':
    print("=" * 70)
    print("EJECUTANDO PRUEBAS UNITARIAS - SMARTHOME DAO")
    print("=" * 70)
    unittest.main(verbosity=2)
