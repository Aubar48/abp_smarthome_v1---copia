"""
Pruebas unitarias para las clases de dominio
Verificación de encapsulación y validaciones
"""

from app.dominio.evento_dispositivo import EventoDispositivo
from app.dominio.dispositivo import Dispositivo
from app.dominio.vivienda import Vivienda
from app.dominio.usuario import Usuario
import unittest
import sys
import os

# Agregar el path del proyecto para importar módulos
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


class TestUsuarioEncapsulacion(unittest.TestCase):
    """Pruebas de encapsulación para Usuario"""

    def test_usuario_getters(self):
        """Prueba que los getters funcionan correctamente"""
        usuario = Usuario(1, "test@test.com", "Test User",
                          "pass123", "usuario")

        self.assertEqual(usuario.id_usuario, 1)
        self.assertEqual(usuario.email, "test@test.com")
        self.assertEqual(usuario.nombre, "Test User")
        self.assertEqual(usuario.contraseña, "pass123")
        self.assertEqual(usuario.rol, "usuario")
        self.assertTrue(usuario.activo)

    def test_usuario_setters(self):
        """Prueba que los setters funcionan correctamente"""
        usuario = Usuario(1, "test@test.com", "Test", "pass", "usuario")

        usuario.nombre = "Nuevo Nombre"
        usuario.email = "nuevo@test.com"
        usuario.contraseña = "newpass"
        usuario.activo = False

        self.assertEqual(usuario.nombre, "Nuevo Nombre")
        self.assertEqual(usuario.email, "nuevo@test.com")
        self.assertEqual(usuario.contraseña, "newpass")
        self.assertFalse(usuario.activo)

    def test_usuario_validacion_rol(self):
        """Prueba validación de rol"""
        usuario = Usuario(1, "test@test.com", "Test", "pass", "usuario")

        # Rol válido
        usuario.rol = "administrador"
        self.assertEqual(usuario.rol, "administrador")

        # Rol inválido
        with self.assertRaises(ValueError):
            usuario.rol = "rol_invalido"

    def test_usuario_str(self):
        """Prueba método __str__"""
        usuario = Usuario(1, "test@test.com", "Test User", "pass", "usuario")
        resultado = str(usuario)
        self.assertIn("Usuario", resultado)
        self.assertIn("Test User", resultado)


class TestViviendaEncapsulacion(unittest.TestCase):
    """Pruebas de encapsulación para Vivienda"""

    def test_vivienda_getters(self):
        """Prueba que los getters funcionan correctamente"""
        vivienda = Vivienda(1, "Casa Test", "Calle 123", 1, True)

        self.assertEqual(vivienda.id_vivienda, 1)
        self.assertEqual(vivienda.nombre_vivienda, "Casa Test")
        self.assertEqual(vivienda.direccion, "Calle 123")
        self.assertEqual(vivienda.id_administrador, 1)
        self.assertTrue(vivienda.activa)

    def test_vivienda_setters(self):
        """Prueba que los setters funcionan correctamente"""
        vivienda = Vivienda(1, "Casa Test", "Calle 123", 1)

        vivienda.nombre_vivienda = "Casa Nueva"
        vivienda.direccion = "Av. Principal 456"
        vivienda.activa = False

        self.assertEqual(vivienda.nombre_vivienda, "Casa Nueva")
        self.assertEqual(vivienda.direccion, "Av. Principal 456")
        self.assertFalse(vivienda.activa)

    def test_vivienda_str(self):
        """Prueba método __str__"""
        vivienda = Vivienda(1, "Casa Test", "Calle 123", 1)
        resultado = str(vivienda)
        self.assertIn("Vivienda", resultado)
        self.assertIn("Casa Test", resultado)


class TestDispositivoEncapsulacion(unittest.TestCase):
    """Pruebas de encapsulación para Dispositivo"""

    def test_dispositivo_getters(self):
        """Prueba que los getters funcionan correctamente"""
        dispositivo = Dispositivo(1, "Luz Sala", "luz", "apagado", "Sala", 1)

        self.assertEqual(dispositivo.id_dispositivo, 1)
        self.assertEqual(dispositivo.nombre_dispositivo, "Luz Sala")
        self.assertEqual(dispositivo.tipo, "luz")
        self.assertEqual(dispositivo.estado, "apagado")
        self.assertEqual(dispositivo.ubicacion, "Sala")
        self.assertEqual(dispositivo.id_vivienda, 1)

    def test_dispositivo_setters(self):
        """Prueba que los setters funcionan correctamente"""
        dispositivo = Dispositivo(1, "Luz", "luz", "apagado", "Sala", 1)

        dispositivo.nombre_dispositivo = "Luz Principal"
        dispositivo.estado = "encendido"
        dispositivo.ubicacion = "Comedor"

        self.assertEqual(dispositivo.nombre_dispositivo, "Luz Principal")
        self.assertEqual(dispositivo.estado, "encendido")
        self.assertEqual(dispositivo.ubicacion, "Comedor")

    def test_dispositivo_validacion_tipo(self):
        """Prueba validación de tipo"""
        dispositivo = Dispositivo(1, "Luz", "luz", "apagado", "Sala", 1)

        # Tipos válidos
        dispositivo.tipo = "sensor"
        self.assertEqual(dispositivo.tipo, "sensor")

        dispositivo.tipo = "camara"
        self.assertEqual(dispositivo.tipo, "camara")

        # Tipo inválido
        with self.assertRaises(ValueError):
            dispositivo.tipo = "tipo_invalido"

    def test_dispositivo_validacion_estado(self):
        """Prueba validación de estado"""
        dispositivo = Dispositivo(1, "Luz", "luz", "apagado", "Sala", 1)

        # Estados válidos
        dispositivo.estado = "encendido"
        self.assertEqual(dispositivo.estado, "encendido")

        dispositivo.estado = "apagado"
        self.assertEqual(dispositivo.estado, "apagado")

        # Estado inválido
        with self.assertRaises(ValueError):
            dispositivo.estado = "estado_invalido"

    def test_dispositivo_str(self):
        """Prueba método __str__"""
        dispositivo = Dispositivo(1, "Luz Sala", "luz", "apagado", "Sala", 1)
        resultado = str(dispositivo)
        self.assertIn("Dispositivo", resultado)
        self.assertIn("Luz Sala", resultado)


class TestEventoDispositivoEncapsulacion(unittest.TestCase):
    """Pruebas de encapsulación para EventoDispositivo"""

    def test_evento_getters(self):
        """Prueba que los getters funcionan correctamente"""
        evento = EventoDispositivo(
            1, 1, 1, "encendido", None, "Evento de prueba")

        self.assertEqual(evento.id_evento, 1)
        self.assertEqual(evento.id_dispositivo, 1)
        self.assertEqual(evento.id_usuario, 1)
        self.assertEqual(evento.tipo_evento, "encendido")
        self.assertEqual(evento.detalle, "Evento de prueba")
        self.assertIsNotNone(evento.fecha_hora)

    def test_evento_setters(self):
        """Prueba que los setters funcionan correctamente"""
        evento = EventoDispositivo(1, 1, 1, "encendido", None, "Detalle")

        evento.tipo_evento = "apagado"
        evento.detalle = "Nuevo detalle"

        self.assertEqual(evento.tipo_evento, "apagado")
        self.assertEqual(evento.detalle, "Nuevo detalle")

    def test_evento_str(self):
        """Prueba método __str__"""
        evento = EventoDispositivo(1, 1, 1, "encendido", None, "Prueba")
        resultado = str(evento)
        self.assertIn("Evento", resultado)


if __name__ == '__main__':
    unittest.main(verbosity=2)
