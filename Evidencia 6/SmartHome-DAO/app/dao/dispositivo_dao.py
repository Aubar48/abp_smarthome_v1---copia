from ..conn.db_conn import obtener_conexion
from ..dominio.dispositivo import Dispositivo
from .interfaces.i_dispositivo_dao import IDispositivoDAO

class DispositivoDAO(IDispositivoDAO):
    def crear(self, dispositivo):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Dispositivo (nombre_dispositivo, tipo, estado, ubicacion, id_vivienda) VALUES (%s, %s, %s, %s, %s)",
            (dispositivo.nombre_dispositivo, dispositivo.tipo, dispositivo.estado, dispositivo.ubicacion, dispositivo.id_vivienda)
        )
        conn.commit()
        id_dispositivo = cursor.lastrowid
        conn.close()
        return id_dispositivo

    def obtener_todos(self):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT id_dispositivo, nombre_dispositivo, tipo, estado, ubicacion, id_vivienda FROM Dispositivo")
        rows = cursor.fetchall()
        conn.close()
        return [Dispositivo(row[0], row[1], row[2], row[3], row[4], row[5]) for row in rows]

    def obtener_por_id(self, id_dispositivo):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT id_dispositivo, nombre_dispositivo, tipo, estado, ubicacion, id_vivienda FROM Dispositivo WHERE id_dispositivo = %s", (id_dispositivo,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Dispositivo(row[0], row[1], row[2], row[3], row[4], row[5])
        return None
    
    def obtener_por_vivienda(self, id_vivienda):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT id_dispositivo, nombre_dispositivo, tipo, estado, ubicacion, id_vivienda FROM Dispositivo WHERE id_vivienda = %s", (id_vivienda,))
        rows = cursor.fetchall()
        conn.close()
        return [Dispositivo(row[0], row[1], row[2], row[3], row[4], row[5]) for row in rows]

    def actualizar(self, dispositivo):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Dispositivo SET nombre_dispositivo = %s, tipo = %s, estado = %s, ubicacion = %s WHERE id_dispositivo = %s",
            (dispositivo.nombre_dispositivo, dispositivo.tipo, dispositivo.estado, dispositivo.ubicacion, dispositivo.id_dispositivo)
        )
        conn.commit()
        conn.close()

    def eliminar(self, id_dispositivo):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Dispositivo WHERE id_dispositivo = %s", (id_dispositivo,))
        conn.commit()
        conn.close()
