import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'smarthome'
}

def obtener_conexion():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"Error al conectar a la base de datos MySQL: {e}")
        if e.errno == 1049: # Base de datos desconocida
            print("La base de datos 'smarthome' no existe. Creándola...")
            try:
                # Conectar sin especificar la base de datos para poder crearla
                temp_conn_config = DB_CONFIG.copy()
                del temp_conn_config['database']
                conn = mysql.connector.connect(**temp_conn_config)
                cursor = conn.cursor()
                cursor.execute("CREATE DATABASE smarthome")
                cursor.close()
                conn.close()
                print("Base de datos 'smarthome' creada. Por favor, ejecute el programa de nuevo.")
            except Error as create_e:
                print(f"No se pudo crear la base de datos: {create_e}")
        return None
