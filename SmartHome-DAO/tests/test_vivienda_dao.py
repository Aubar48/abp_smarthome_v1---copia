"""
Pruebas unitarias para ViviendaDAO
"""

from app.dominio.usuario import Usuario
from app.dominio.vivienda import Vivienda
from app.dao.usuario_dao import UsuarioDAO
from app.dao.vivienda_dao import ViviendaDAO
import unittest
import sys
import os

# Agregar el path del proyecto para importar módulos
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


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

    def test_actualizar_vivienda(self):
        """Prueba actualizar datos de vivienda"""
        # Crear vivienda
        vivienda = Vivienda(None, "Casa Test", "Calle Test 123", self.id_admin)
        id_vivienda = self.vivienda_dao.crear(vivienda)
        self.test_vivienda_ids.append(id_vivienda)

        # Actualizar
        vivienda_obtenida = self.vivienda_dao.obtener_por_id(id_vivienda)
        vivienda_obtenida.nombre_vivienda = "Casa Actualizada"
        self.vivienda_dao.actualizar(vivienda_obtenida)

        # Verificar
        vivienda_verificada = self.vivienda_dao.obtener_por_id(id_vivienda)
        self.assertEqual(vivienda_verificada.nombre_vivienda,
                         "Casa Actualizada")

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

    def test_obtener_viviendas_por_usuario(self):
        """Prueba obtener viviendas asignadas a un usuario"""
        # Crear usuario y vivienda
        usuario = Usuario(None, "usuario_test2@test.com",
                          "Usuario Test 2", "pass123", "usuario")
        id_usuario = self.usuario_dao.crear(usuario)

        vivienda = Vivienda(None, "Casa Test 2",
                            "Calle Test 456", self.id_admin)
        id_vivienda = self.vivienda_dao.crear(vivienda)
        self.test_vivienda_ids.append(id_vivienda)

        # Asignar usuario
        self.vivienda_dao.asignar_usuario(id_usuario, id_vivienda)

        # Obtener viviendas
        viviendas = self.vivienda_dao.obtener_por_usuario(id_usuario)
        self.assertGreater(len(viviendas), 0)

        # Limpiar
        self.vivienda_dao.desasignar_todas_viviendas_usuario(id_usuario)
        self.usuario_dao.eliminar(id_usuario)

    def test_obtener_todas_viviendas(self):
        """Prueba obtener todas las viviendas"""
        # Crear vivienda
        vivienda = Vivienda(None, "Casa Test 3",
                            "Calle Test 789", self.id_admin)
        id_vivienda = self.vivienda_dao.crear(vivienda)
        self.test_vivienda_ids.append(id_vivienda)

        # Obtener todas
        viviendas = self.vivienda_dao.obtener_todos()
        self.assertIsNotNone(viviendas)
        self.assertGreater(len(viviendas), 0)

    def test_eliminar_vivienda(self):
        """Prueba eliminar vivienda"""
        # Crear vivienda
        vivienda = Vivienda(None, "Casa Test Delete",
                            "Calle Delete", self.id_admin)
        id_vivienda = self.vivienda_dao.crear(vivienda)

        # Eliminar
        self.vivienda_dao.eliminar(id_vivienda)

        # Verificar que no existe
        vivienda_eliminada = self.vivienda_dao.obtener_por_id(id_vivienda)
        self.assertIsNone(vivienda_eliminada)


if __name__ == '__main__':
    unittest.main(verbosity=2)
