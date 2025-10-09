"""
Script principal para ejecutar todas las pruebas TDD del sistema SmartHome
Sistema Simplificado con 2 roles: administrador y usuario
Solo 3 tipos de dispositivos: luz, sensor, camara
"""
import unittest
import sys
import os

# Agregar el directorio actual al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def run_all_tests():
    """
    Ejecuta todas las pruebas TDD del sistema SmartHome simplificado
    """
    print("="*80)
    print("EJECUTANDO PRUEBAS TDD ULTRA-SIMPLES - SISTEMA SMARTHOME SIMPLIFICADO")
    print("="*80)
    print("- 2 Roles: administrador, usuario")
    print("- 3 Tipos de dispositivos: luz, sensor, camara")
    print("- 3 Tipos de eventos: encendido, apagado, configuracion")
    print("- Solo 5 pruebas por clase - Las más esenciales")
    print("="*80)
    
    # Crear el test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Lista de módulos de prueba ultra-simplificados
    test_modules = [
        'prueba_usuario',            # ✅ Ultra-simplificado: 5 pruebas básicas
        'prueba_dispositivo',        # ✅ Ultra-simplificado: 5 pruebas esenciales
        'prueba_vivienda',           # ✅ Ultra-simplificado: 5 pruebas básicas
        'prueba_eventoDispositivo',  # ✅ Ultra-simplificado: 5 pruebas fundamentales
        'prueba_automatizacion'      # ✅ Ultra-simplificado: 5 pruebas básicas
    ]
    
    # Cargar todas las pruebas
    for module_name in test_modules:
        try:
            print(f"Cargando pruebas de {module_name}...")
            module = __import__(module_name)
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
    print("RESUMEN DE PRUEBAS TDD")
    print("="*80)
    print(f"Pruebas ejecutadas: {result.testsRun}")
    print(f"Errores: {len(result.errors)}")
    print(f"Fallos: {len(result.failures)}")
    
    if result.errors:
        print("\n--- ERRORES ---")
        for test, error in result.errors:
            print(f"{test}: {error}")
    
    if result.failures:
        print("\n--- FALLOS ---")
        for test, failure in result.failures:
            print(f"{test}: {failure}")
    
    if result.wasSuccessful():
        print("\n✅ TODAS LAS PRUEBAS PASARON EXITOSAMENTE!")
        print("El sistema SmartHome simplificado está funcionando correctamente.")
    else:
        print("\n❌ ALGUNAS PRUEBAS FALLARON")
        print("Revisar los errores y fallos listados arriba.")
    
    print("="*80)
    return result.wasSuccessful()

def run_specific_test(test_name):
    """
    Ejecuta pruebas específicas de una clase
    """
    print(f"Ejecutando pruebas específicas para: {test_name}")
    
    try:
        module = __import__(f'prueba_{test_name}')
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(module)
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        return result.wasSuccessful()
    except ImportError:
        print(f"No se pudo encontrar el módulo de pruebas para {test_name}")
        return False

def show_menu():
    """
    Muestra el menú de opciones para ejecutar pruebas
    """
    print("\n" + "="*60)
    print("SISTEMA DE PRUEBAS TDD ULTRA-SIMPLES - SMARTHOME SIMPLIFICADO")
    print("="*60)
    print("1. Ejecutar todas las pruebas")
    print("2. Ejecutar pruebas de Usuario")
    print("3. Ejecutar pruebas de Dispositivo")
    print("4. Ejecutar pruebas de Vivienda")
    print("5. Ejecutar pruebas de EventoDispositivo")
    print("6. Ejecutar pruebas de Automatizacion")
    print("7. Mostrar información del sistema")
    print("0. Salir")
    print("="*60)

def show_system_info():
    """
    Muestra información sobre el sistema simplificado
    """
    print("\n" + "="*60)
    print("INFORMACIÓN DEL SISTEMA SMARTHOME SIMPLIFICADO")
    print("="*60)
    print("ROLES:")
    print("  - administrador: Puede gestionar viviendas, dispositivos y usuarios")
    print("  - usuario: Puede controlar dispositivos asignados")
    print()
    print("TIPOS DE DISPOSITIVOS:")
    print("  - luz: Dispositivos de iluminación (encender/apagar)")
    print("  - sensor: Sensores de temperatura, movimiento, etc.")
    print("  - camara: Cámaras de seguridad")
    print()
    print("ESTADOS DE DISPOSITIVOS:")
    print("  - encendido: Dispositivo activo")
    print("  - apagado: Dispositivo inactivo")
    print()
    print("TIPOS DE EVENTOS:")
    print("  - encendido: Dispositivo fue encendido")
    print("  - apagado: Dispositivo fue apagado")
    print("  - configuracion: Dispositivo fue configurado")
    print()
    print("FUNCIONALIDADES IMPLEMENTADAS:")
    print("  ✅ Gestión de usuarios con 2 roles")
    print("  ✅ Control de dispositivos básico")
    print("  ✅ Registro de eventos")
    print("  ✅ Información de viviendas")
    print("  ✅ Sistema de automatizaciones básico")
    print("  ✅ Pruebas TDD ultra-simplificadas: solo 5 por clase")
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
                print("¡Gracias por usar el sistema de pruebas TDD!")
                break
            elif choice == '1':
                run_all_tests()
            elif choice == '2':
                run_specific_test('usuario')
            elif choice == '3':
                run_specific_test('dispositivo')
            elif choice == '4':
                run_specific_test('vivienda')
            elif choice == '5':
                run_specific_test('eventoDispositivo')
            elif choice == '6':
                run_specific_test('automatizacion')
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
        print("Uso: python ejecutar_pruebas_tdd.py [all|usuario|dispositivo|vivienda|eventoDispositivo|automatizacion]")