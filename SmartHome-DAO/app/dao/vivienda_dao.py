from ..conn.db_conn import obtener_conexion
from ..dominio.vivienda import Vivienda
from .interfaces.i_vivienda_dao import IViviendaDAO


class ViviendaDAO(IViviendaDAO):
    def crear(self, vivienda):
        conn = None
        cursor = None
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Vivienda (nombre_vivienda, direccion, id_administrador) VALUES (%s, %s, %s)",
                (vivienda.nombre_vivienda, vivienda.direccion,
                 vivienda.id_administrador)
            )
            conn.commit()
            id_vivienda = cursor.lastrowid
            return id_vivienda
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Error al crear vivienda: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def obtener_todos(self):
        conn = None
        cursor = None
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id_vivienda, nombre_vivienda, direccion, id_administrador, activa FROM Vivienda")
            rows = cursor.fetchall()
            return [Vivienda(row[0], row[1], row[2], row[3], row[4]) for row in rows]
        except Exception as e:
            print(f"Error al obtener todas las viviendas: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def obtener_por_id(self, id_vivienda):
        conn = None
        cursor = None
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id_vivienda, nombre_vivienda, direccion, id_administrador, activa FROM Vivienda WHERE id_vivienda = %s", (id_vivienda,))
            row = cursor.fetchone()
            if row:
                return Vivienda(row[0], row[1], row[2], row[3], row[4])
            return None
        except Exception as e:
            print(f"Error al obtener vivienda por ID: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def obtener_por_usuario(self, id_usuario):
        conn = None
        cursor = None
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT v.id_vivienda, v.nombre_vivienda, v.direccion, v.id_administrador, v.activa 
                FROM Vivienda v
                JOIN Usuario_Vivienda uv ON v.id_vivienda = uv.id_vivienda
                WHERE uv.id_usuario = %s
            """, (id_usuario,))
            rows = cursor.fetchall()
            return [Vivienda(row[0], row[1], row[2], row[3], row[4]) for row in rows]
        except Exception as e:
            print(f"Error al obtener viviendas por usuario: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def actualizar(self, vivienda):
        conn = None
        cursor = None
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE Vivienda SET nombre_vivienda = %s, direccion = %s, activa = %s, id_administrador = %s WHERE id_vivienda = %s",
                (vivienda.nombre_vivienda, vivienda.direccion, vivienda.activa,
                 vivienda.id_administrador, vivienda.id_vivienda)
            )
            conn.commit()
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Error al actualizar vivienda: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def eliminar(self, id_vivienda):
        conn = None
        cursor = None
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            # Primero desasignar usuarios para evitar problemas de FK si es necesario
            cursor.execute(
                "DELETE FROM Usuario_Vivienda WHERE id_vivienda = %s", (id_vivienda,))
            cursor.execute(
                "DELETE FROM Vivienda WHERE id_vivienda = %s", (id_vivienda,))
            conn.commit()
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Error al eliminar vivienda: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def asignar_usuario(self, id_usuario, id_vivienda):
        conn = None
        cursor = None
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()

            # Verificar si el usuario ya está asignado a la vivienda
            cursor.execute(
                "SELECT COUNT(*) FROM Usuario_Vivienda WHERE id_usuario = %s AND id_vivienda = %s",
                (id_usuario, id_vivienda)
            )
            existe = cursor.fetchone()[0]

            if existe > 0:
                return False  # Usuario ya asignado

            cursor.execute(
                "INSERT INTO Usuario_Vivienda (id_usuario, id_vivienda) VALUES (%s, %s)",
                (id_usuario, id_vivienda)
            )
            conn.commit()
            return True  # Asignación exitosa
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Error al asignar usuario a vivienda: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def desasignar_todas_viviendas_usuario(self, id_usuario):
        """Desasigna un usuario de todas sus viviendas"""
        conn = None
        cursor = None
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM Usuario_Vivienda WHERE id_usuario = %s",
                (id_usuario,)
            )
            conn.commit()
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Error al desasignar viviendas del usuario: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
