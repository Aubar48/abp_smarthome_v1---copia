from ..conn.db_conn import obtener_conexion
from ..dominio.evento_dispositivo import EventoDispositivo
from .interfaces.i_evento_dispositivo_dao import IEventoDispositivoDAO


class EventoDispositivoDAO(IEventoDispositivoDAO):
    def crear(self, evento):
        conn = None
        cursor = None
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO EventoDispositivo (id_dispositivo, id_usuario, tipo_evento, detalle) VALUES (%s, %s, %s, %s)",
                (evento.id_dispositivo, evento.id_usuario,
                 evento.tipo_evento, evento.detalle)
            )
            conn.commit()
            id_evento = cursor.lastrowid
            return id_evento
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Error al crear evento: {e}")
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
                "SELECT id_evento, id_dispositivo, id_usuario, tipo_evento, fecha_hora, detalle FROM EventoDispositivo")
            rows = cursor.fetchall()
            return [EventoDispositivo(row[0], row[1], row[2], row[3], row[4], row[5]) for row in rows]
        except Exception as e:
            print(f"Error al obtener todos los eventos: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def obtener_por_id(self, id_evento):
        conn = None
        cursor = None
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id_evento, id_dispositivo, id_usuario, tipo_evento, fecha_hora, detalle FROM EventoDispositivo WHERE id_evento = %s", (id_evento,))
            row = cursor.fetchone()
            if row:
                return EventoDispositivo(row[0], row[1], row[2], row[3], row[4], row[5])
            return None
        except Exception as e:
            print(f"Error al obtener evento por ID: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def obtener_por_dispositivo_id(self, id_dispositivo):
        conn = None
        cursor = None
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id_evento, id_dispositivo, id_usuario, tipo_evento, fecha_hora, detalle FROM EventoDispositivo WHERE id_dispositivo = %s", (id_dispositivo,))
            rows = cursor.fetchall()
            return [EventoDispositivo(row[0], row[1], row[2], row[3], row[4], row[5]) for row in rows]
        except Exception as e:
            print(f"Error al obtener eventos por dispositivo: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def eliminar(self, id_evento):
        conn = None
        cursor = None
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM EventoDispositivo WHERE id_evento = %s", (id_evento,))
            conn.commit()
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Error al eliminar evento: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
