"""
Script de verificación de dependencias para SmartHome-DAO
Verifica que todas las dependencias necesarias estén instaladas correctamente
"""

import sys
import platform


def verificar_python():
    """Verifica la versión de Python"""
    print("=" * 70)
    print("VERIFICACIÓN DE PYTHON")
    print("=" * 70)

    version = sys.version_info
    print(
        f"✓ Versión de Python: {version.major}.{version.minor}.{version.micro}")
    print(f"✓ Ejecutable: {sys.executable}")
    print(f"✓ Plataforma: {platform.system()} {platform.release()}")

    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("\n❌ ADVERTENCIA: Se requiere Python 3.8 o superior")
        print("   Tu versión actual puede no ser compatible")
        return False
    else:
        print("\n✅ Versión de Python compatible")
        return True


def verificar_dependencias():
    """Verifica las dependencias instaladas"""
    print("\n" + "=" * 70)
    print("VERIFICACIÓN DE DEPENDENCIAS")
    print("=" * 70)

    dependencias = {
        'mysql.connector': 'mysql-connector-python'
    }

    todas_instaladas = True

    for modulo, nombre_paquete in dependencias.items():
        try:
            # Intentar importar el módulo
            if modulo == 'mysql.connector':
                import mysql.connector
                version = mysql.connector.__version__
                print(f"✅ {nombre_paquete}: {version}")
            else:
                __import__(modulo)
                print(f"✅ {nombre_paquete}: Instalado")

        except ImportError:
            print(f"❌ {nombre_paquete}: NO INSTALADO")
            todas_instaladas = False

    return todas_instaladas


def verificar_conexion_mysql():
    """Verifica si se puede conectar a MySQL"""
    print("\n" + "=" * 70)
    print("VERIFICACIÓN DE CONEXIÓN A MYSQL")
    print("=" * 70)

    try:
        import mysql.connector

        # Intentar una conexión básica (puede fallar si no hay servidor)
        print("ℹ️  Intentando conectar a MySQL en localhost...")
        print("   (Es normal que falle si MySQL no está corriendo)")

        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',  # Usuario por defecto
                password='',  # Sin contraseña por defecto
                connect_timeout=2
            )
            conn.close()
            print("✅ Conexión a MySQL exitosa")
            return True
        except mysql.connector.Error as err:
            if err.errno == 2003:
                print("⚠️  No se pudo conectar: MySQL no está corriendo")
            elif err.errno == 1045:
                print("⚠️  Error de autenticación: Verifica usuario/contraseña")
            else:
                print(f"⚠️  Error de conexión: {err}")
            print("   Configura la conexión en app/conn/db_conn.py")
            return False

    except ImportError:
        print("❌ mysql-connector-python no está instalado")
        return False


def mostrar_instrucciones():
    """Muestra instrucciones si faltan dependencias"""
    print("\n" + "=" * 70)
    print("INSTRUCCIONES DE INSTALACIÓN")
    print("=" * 70)
    print("\nPara instalar las dependencias faltantes:")
    print("\n1. Opción recomendada (usando requirements.txt):")
    print("   pip install -r requirements.txt")
    print("\n2. Instalación manual:")
    print("   pip install mysql-connector-python==8.2.0")
    print("\n3. Si pip no funciona, usa:")
    print("   python -m pip install -r requirements.txt")


def main():
    """Función principal"""
    print("\n")
    print("🔍 VERIFICADOR DE DEPENDENCIAS - SMARTHOME-DAO")
    print("\n")

    # Verificar Python
    python_ok = verificar_python()

    # Verificar dependencias
    deps_ok = verificar_dependencias()

    # Verificar conexión MySQL
    mysql_ok = verificar_conexion_mysql()

    # Resumen
    print("\n" + "=" * 70)
    print("RESUMEN")
    print("=" * 70)

    if python_ok and deps_ok:
        print("\n✅ Todas las dependencias están instaladas correctamente")

        if mysql_ok:
            print("✅ MySQL está accesible")
            print("\n🎉 ¡El proyecto está listo para ejecutarse!")
            print("\nPróximos pasos:")
            print("1. Configurar conexión en app/conn/db_conn.py")
            print("2. Crear base de datos con scripts DDL")
            print("3. Ejecutar: python main.py")
        else:
            print("\n⚠️  Configuración de MySQL pendiente")
            print("\nPróximos pasos:")
            print("1. Iniciar servidor MySQL")
            print("2. Configurar conexión en app/conn/db_conn.py")
            print("3. Crear base de datos con scripts DDL")
            print("4. Ejecutar: python main.py")
    else:
        print("\n❌ Faltan dependencias por instalar")
        mostrar_instrucciones()

    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
