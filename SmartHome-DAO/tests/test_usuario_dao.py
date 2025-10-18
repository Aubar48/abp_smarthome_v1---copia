"""
Pruebas unitarias para UsuarioDAO
"""

from app.dominio.usuario import Usuario
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

    def test_obtener_usuario_por_id(self):
        """Prueba obtener usuario por ID"""
        # Crear usuario
        usuario = Usuario(None, self.test_email,
                          "Usuario Test", "pass123", "usuario")
        id_usuario = self.usuario_dao.crear(usuario)

        # Obtener usuario
        usuario_obtenido = self.usuario_dao.obtener_por_id(id_usuario)
        self.assertIsNotNone(usuario_obtenido)
        self.assertEqual(usuario_obtenido.id_usuario, id_usuario)
        self.assertEqual(usuario_obtenido.email, self.test_email)

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

    def test_obtener_todos_usuarios(self):
        """Prueba obtener todos los usuarios"""
        # Crear usuario de prueba
        usuario = Usuario(None, self.test_email,
                          "Usuario Test", "pass123", "usuario")
        self.usuario_dao.crear(usuario)

        # Obtener todos
        usuarios = self.usuario_dao.obtener_todos()
        self.assertIsNotNone(usuarios)
        self.assertGreater(len(usuarios), 0)


if __name__ == '__main__':
    unittest.main(verbosity=2)
