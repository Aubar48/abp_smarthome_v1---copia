"""
Script principal para ejecutar todas las pruebas del sistema SmartHome-DAO
Sistema con patrón DAO, Servicios y capa de Dominio
Incluye pruebas de DAOs y encapsulación
"""
import unittest
import sys
import os

# Agregar el directorio actual al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def run_all_tests():
    """
    Ejecuta todas las pruebas del sistema SmartHome-DAO
    """
    print("="*80)
    print("EJECUTANDO PRUEBAS - SISTEMA SMARTHOME-DAO")
    print("="*80)
    print("- Patrón DAO (Data Access Object)")
    print("- Capa de Servicios")
    print("- Encapsulación con @property")
    print("- Conexión a MySQL")
    print("="*80)

    # Crear el test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    # Lista de módulos de prueba modularizados
    test_modules = [
        'tests.test_usuario_dao',           # ✅ Pruebas de UsuarioDAO
        'tests.test_vivienda_dao',          # ✅ Pruebas de ViviendaDAO
        'tests.test_dispositivo_dao',       # ✅ Pruebas de DispositivoDAO
        'tests.test_evento_dao',            # ✅ Pruebas de EventoDispositivoDAO
        'tests.test_dominio'                # ✅ Pruebas de encapsulación
    ]

    # Cargar todas las pruebas
    for module_name in test_modules:
        try:
            print(f"Cargando pruebas de {module_name}...")
            module = __import__(module_name, fromlist=[''])
            suite.addTests(loader.loadTestsFromModule(module))
        except ImportError as e:
            print(f"Error al importar {module_name}: {e}")
        except Exception as e:
            print(f"Error inesperado con {module_name}: {e}")

    # Ejecutar las pruebas
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Mostrar resumen
    print("\n" + "="*80)
    print("RESUMEN DE PRUEBAS")
    print("="*80)
    print(f"Pruebas ejecutadas: {result.testsRun}")
    print(f"Errores: {len(result.errors)}")
    print(f"Fallos: {len(result.failures)}")

    if result.errors:
        print("\n--- ERRORES ---")
        for test, error in result.errors:
            print(f"{test}: {error[:200]}...")  # Limitar tamaño del error

    if result.failures:
        print("\n--- FALLOS ---")
        for test, failure in result.failures:
            print(f"{test}: {failure[:200]}...")  # Limitar tamaño del fallo

    if result.wasSuccessful():
        print("\n✅ TODAS LAS PRUEBAS PASARON EXITOSAMENTE!")
        print("El sistema SmartHome-DAO está funcionando correctamente.")
    else:
        print("\n❌ ALGUNAS PRUEBAS FALLARON")
        print("Revisar los errores y fallos listados arriba.")
        print("\n⚠️  Nota: Asegúrate de que MySQL esté corriendo y la BD configurada.")

    print("="*80)
    return result.wasSuccessful()


def run_specific_test(test_name):
    """
    Ejecuta pruebas específicas de un módulo
    """
    print(f"Ejecutando pruebas específicas para: {test_name}")

    # Mapeo de nombres cortos a módulos completos
    test_map = {
        'usuario': 'tests.test_usuario_dao',
        'vivienda': 'tests.test_vivienda_dao',
        'dispositivo': 'tests.test_dispositivo_dao',
        'evento': 'tests.test_evento_dao',
        'dominio': 'tests.test_dominio'
    }

    module_name = test_map.get(test_name, f'tests.test_{test_name}')

    try:
        module = __import__(module_name, fromlist=[''])
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(module)
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        return result.wasSuccessful()
    except ImportError as e:
        print(f"No se pudo encontrar el módulo de pruebas para {test_name}")
        print(f"Error: {e}")
        return False


def show_menu():
    """
    Muestra el menú de opciones para ejecutar pruebas
    """
    print("\n" + "="*60)
    print("SISTEMA DE PRUEBAS - SMARTHOME-DAO")
    print("="*60)
    print("1. Ejecutar todas las pruebas")
    print("2. Ejecutar pruebas de UsuarioDAO")
    print("3. Ejecutar pruebas de ViviendaDAO")
    print("4. Ejecutar pruebas de DispositivoDAO")
    print("5. Ejecutar pruebas de EventoDispositivoDAO")
    print("6. Ejecutar pruebas de Encapsulación (Dominio)")
    print("7. Mostrar información del sistema")
    print("0. Salir")
    print("="*60)


def show_system_info():
    """
    Muestra información sobre el sistema SmartHome-DAO
    """
    print("\n" + "="*60)
    print("INFORMACIÓN DEL SISTEMA SMARTHOME-DAO")
    print("="*60)
    print("ARQUITECTURA:")
    print("  - Patrón DAO (Data Access Object)")
    print("  - Capa de Servicios (Business Logic)")
    print("  - Capa de Dominio (Modelos con encapsulación)")
    print("  - Capa de Conexión (MySQL)")
    print()
    print("MÓDULOS DE PRUEBA:")
    print("  📦 test_usuario_dao.py")
    print("     - Pruebas CRUD de usuarios")
    print("     - Validaciones de email y rol")
    print("     - Búsquedas y actualizaciones")
    print()
    print("  📦 test_vivienda_dao.py")
    print("     - Pruebas CRUD de viviendas")
    print("     - Gestión de usuarios asignados")
    print("     - Estados de viviendas")
    print()
    print("  📦 test_dispositivo_dao.py")
    print("     - Pruebas CRUD de dispositivos")
    print("     - Tipos: luz, sensor, camara")
    print("     - Estados: encendido, apagado")
    print()
    print("  📦 test_evento_dao.py")
    print("     - Registro de eventos de dispositivos")
    print("     - Tipos: encendido, apagado, configuracion")
    print("     - Consultas por dispositivo y vivienda")
    print()
    print("  📦 test_dominio.py")
    print("     - Pruebas de encapsulación con @property")
    print("     - Validaciones en setters")
    print("     - Modelos: Usuario, Vivienda, Dispositivo, Evento")
    print()
    print("TECNOLOGÍAS:")
    print("  ✅ Python 3.8+")
    print("  ✅ MySQL Connector")
    print("  ✅ unittest (Framework de pruebas)")
    print("  ✅ Patrón DAO")
    print()
    print("REQUISITOS:")
    print("  ⚠️  MySQL Server corriendo")
    print("  ⚠️  Base de datos 'smarthome_db' creada")
    print("  ⚠️  Conexión configurada en app/conn/db_conn.py")
    print("="*60)


def main():
    """
    Función principal del sistema de pruebas
    """
    while True:
        show_menu()

        try:
            choice = input("\nSeleccione una opción: ").strip()

            if choice == '0':
                print("¡Gracias por usar el sistema de pruebas SmartHome-DAO!")
                break
            elif choice == '1':
                run_all_tests()
            elif choice == '2':
                run_specific_test('usuario')
            elif choice == '3':
                run_specific_test('vivienda')
            elif choice == '4':
                run_specific_test('dispositivo')
            elif choice == '5':
                run_specific_test('evento')
            elif choice == '6':
                run_specific_test('dominio')
            elif choice == '7':
                show_system_info()
            else:
                print("Opción inválida. Por favor seleccione una opción válida.")

        except KeyboardInterrupt:
            print("\n\nProceso interrumpido por el usuario.")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")

        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    # Si se ejecuta directamente, mostrar el menú
    if len(sys.argv) == 1:
        main()
    elif len(sys.argv) == 2:
        # Si se pasa un argumento, ejecutar pruebas específicas
        if sys.argv[1] == "all":
            run_all_tests()
        else:
            run_specific_test(sys.argv[1])
    else:
        print(
            "Uso: python ejecutar_pruebas2_tdd.py [all|usuario|vivienda|dispositivo|evento|dominio]")
