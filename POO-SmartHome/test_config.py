"""
Configuración para las pruebas TDD del sistema SmartHome
"""
import sys
import os

# Agregar el directorio actual al path para importar las clases
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Constantes para las pruebas
TEST_USER_ADMIN = {
    'email': 'admin@test.com',
    'nombre': 'Admin Test',
    'contraseña': 'test123',
    'rol': 'administrador'
}

TEST_USER_NORMAL = {
    'email': 'user@test.com',
    'nombre': 'User Test',
    'contraseña': 'test123',
    'rol': 'usuario'
}

TEST_VIVIENDA = {
    'id_vivienda': 1,
    'nombre_vivienda': 'Casa Test',
    'ubicacion': 'Test Address 123'
}

TEST_DISPOSITIVO_LUZ = {
    'id_dispositivo': 1,
    'nombre_dispositivo': 'Luz Test',
    'tipo': 'luz'
}

TEST_DISPOSITIVO_SENSOR = {
    'id_dispositivo': 2,
    'nombre_dispositivo': 'Sensor Test',
    'tipo': 'sensor'
}

TEST_DISPOSITIVO_CAMARA = {
    'id_dispositivo': 3,
    'nombre_dispositivo': 'Camara Test',
    'tipo': 'camara'
}