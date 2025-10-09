from ..conn.db_conn import obtener_conexion
from ..dominio.vivienda import Vivienda
from .interfaces.i_vivienda_dao import IViviendaDAO


class ViviendaDAO(IViviendaDAO):
    def crear(self, vivienda):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Vivienda (nombre_vivienda, direccion, id_administrador) VALUES (%s, %s, %s)",
            (vivienda.nombre_vivienda, vivienda.direccion, vivienda.id_administrador)
        )
        conn.commit()
        id_vivienda = cursor.lastrowid
        conn.close()
        return id_vivienda

    def obtener_todos(self):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id_vivienda, nombre_vivienda, direccion, id_administrador, activa FROM Vivienda")
        rows = cursor.fetchall()
        conn.close()
        return [Vivienda(row[0], row[1], row[2], row[3], row[4]) for row in rows]

    def obtener_por_id(self, id_vivienda):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id_vivienda, nombre_vivienda, direccion, id_administrador, activa FROM Vivienda WHERE id_vivienda = %s", (id_vivienda,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Vivienda(row[0], row[1], row[2], row[3], row[4])
        return None

    def obtener_por_usuario(self, id_usuario):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT v.id_vivienda, v.nombre_vivienda, v.direccion, v.id_administrador, v.activa 
            FROM Vivienda v
            JOIN Usuario_Vivienda uv ON v.id_vivienda = uv.id_vivienda
            WHERE uv.id_usuario = %s
        """, (id_usuario,))
        rows = cursor.fetchall()
        conn.close()
        return [Vivienda(row[0], row[1], row[2], row[3], row[4]) for row in rows]

    def actualizar(self, vivienda):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Vivienda SET nombre_vivienda = %s, direccion = %s, activa = %s, id_administrador = %s WHERE id_vivienda = %s",
            (vivienda.nombre_vivienda, vivienda.direccion, vivienda.activa,
             vivienda.id_administrador, vivienda.id_vivienda)
        )
        conn.commit()
        conn.close()

    def eliminar(self, id_vivienda):
        conn = obtener_conexion()
        cursor = conn.cursor()
        # Primero desasignar usuarios para evitar problemas de FK si es necesario
        cursor.execute(
            "DELETE FROM Usuario_Vivienda WHERE id_vivienda = %s", (id_vivienda,))
        cursor.execute(
            "DELETE FROM Vivienda WHERE id_vivienda = %s", (id_vivienda,))
        conn.commit()
        conn.close()

    def asignar_usuario(self, id_usuario, id_vivienda):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Usuario_Vivienda (id_usuario, id_vivienda) VALUES (%s, %s)",
            (id_usuario, id_vivienda)
        )
        conn.commit()
        conn.close()

    def desasignar_todas_viviendas_usuario(self, id_usuario):
        """Desasigna un usuario de todas sus viviendas"""
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM Usuario_Vivienda WHERE id_usuario = %s",
            (id_usuario,)
        )
        conn.commit()
        conn.close()
