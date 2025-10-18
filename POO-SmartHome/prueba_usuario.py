"""
Pruebas TDD para la clase Usuario - Sistema SmartHome Simplificado
Valida funcionalidad básica de autenticación y gestión de usuarios
Solo 2 roles: administrador y usuario
"""
import unittest
from clase_usuario import Usuario

class TestUsuario(unittest.TestCase):
    """
    Suite de pruebas para validar la clase Usuario
    Cubre: creación de usuarios, autenticación, cambio de contraseñas y roles
    """
    
    def setUp(self):
        """Configurar datos de prueba: un admin y un usuario normal"""
        self.admin = Usuario("admin@test.com", "Admin", "123", "administrador")
        self.user = Usuario("user@test.com", "User", "456", "usuario")

    def test_crear_usuario_admin(self):
        """Validar que se puede crear un usuario administrador correctamente"""
        self.assertEqual(self.admin.get_email(), "admin@test.com")
        self.assertEqual(self.admin._nombre, "Admin")
        self.assertEqual(self.admin._rol, "administrador")

    def test_crear_usuario_normal(self):
        """Validar que se puede crear un usuario normal correctamente"""
        self.assertEqual(self.user.get_email(), "user@test.com")
        self.assertEqual(self.user._nombre, "User")
        self.assertEqual(self.user._rol, "usuario")

    def test_iniciar_sesion_correcto(self):
        """Validar que el inicio de sesión funciona con credenciales correctas"""
        resultado = self.admin.iniciar_sesion("admin@test.com", "123")
        self.assertEqual(resultado, "Sesión iniciada correctamente.")
        self.assertTrue(self.admin._sesion_activa)

    def test_cambiar_contraseña(self):
        """Validar que se puede cambiar la contraseña del usuario"""
        self.admin.set_contraseña("nueva123")
        self.assertEqual(self.admin.get_contraseña(), "nueva123")

    def test_solo_dos_roles(self):
        """Validar que el sistema maneja exactamente 2 roles: admin y usuario"""
        self.assertEqual(self.admin._rol, "administrador")
        self.assertEqual(self.user._rol, "usuario")

if __name__ == "__main__":
    unittest.main()


