import mysql.connector
# Se importa el módulo de errores de MySQL
from mysql.connector import errorcode

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'smarthome'
}


def obtener_conexion():
    """
    Método que permite conectar a una base de datos MySQL Server
    """
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuario o Password no válidos")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos NO existe.")
        else:
            print(err)
        return None
