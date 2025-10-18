"""
Suite de pruebas completa - Sistema SmartHome DAO
Ejecuta todas las pruebas unitarias modularizadas
"""

from tests.test_dominio import (
    TestUsuarioEncapsulacion,
    TestViviendaEncapsulacion,
    TestDispositivoEncapsulacion,
    TestEventoDispositivoEncapsulacion
)
from tests.test_evento_dao import TestEventoDispositivoDAO
from tests.test_dispositivo_dao import TestDispositivoDAO
from tests.test_vivienda_dao import TestViviendaDAO
from tests.test_usuario_dao import TestUsuarioDAO
import unittest
import sys
import os

# Agregar el path del proyecto
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

# Importar todos los módulos de prueba


def suite():
    """Crea y retorna la suite completa de pruebas"""
    test_suite = unittest.TestSuite()

    # Agregar pruebas de DAOs
    test_suite.addTests(unittest.TestLoader(
    ).loadTestsFromTestCase(TestUsuarioDAO))
    test_suite.addTests(unittest.TestLoader(
    ).loadTestsFromTestCase(TestViviendaDAO))
    test_suite.addTests(unittest.TestLoader(
    ).loadTestsFromTestCase(TestDispositivoDAO))
    test_suite.addTests(unittest.TestLoader(
    ).loadTestsFromTestCase(TestEventoDispositivoDAO))

    # Agregar pruebas de dominio
    test_suite.addTests(unittest.TestLoader(
    ).loadTestsFromTestCase(TestUsuarioEncapsulacion))
    test_suite.addTests(unittest.TestLoader(
    ).loadTestsFromTestCase(TestViviendaEncapsulacion))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        TestDispositivoEncapsulacion))
    test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        TestEventoDispositivoEncapsulacion))

    return test_suite


if __name__ == '__main__':
    print("=" * 70)
    print("SUITE COMPLETA DE PRUEBAS UNITARIAS - SMARTHOME DAO")
    print("=" * 70)
    print("\n📋 Módulos de prueba:")
    print("  ✅ test_usuario_dao.py - Pruebas de UsuarioDAO")
    print("  ✅ test_vivienda_dao.py - Pruebas de ViviendaDAO")
    print("  ✅ test_dispositivo_dao.py - Pruebas de DispositivoDAO")
    print("  ✅ test_evento_dao.py - Pruebas de EventoDispositivoDAO")
    print("  ✅ test_dominio.py - Pruebas de encapsulación")
    print("\n" + "=" * 70 + "\n")

    # Ejecutar suite completa
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite())

    # Resumen final
    print("\n" + "=" * 70)
    print("RESUMEN DE PRUEBAS")
    print("=" * 70)
    print(f"Total de pruebas ejecutadas: {result.testsRun}")
    print(
        f"✅ Exitosas: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"❌ Fallidas: {len(result.failures)}")
    print(f"⚠️  Errores: {len(result.errors)}")
    print("=" * 70)

    # Retornar código de salida apropiado
    sys.exit(0 if result.wasSuccessful() else 1)
