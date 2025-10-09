from ..conn.db_conn import obtener_conexion
from ..dominio.evento_dispositivo import EventoDispositivo
from .interfaces.i_evento_dispositivo_dao import IEventoDispositivoDAO

class EventoDispositivoDAO(IEventoDispositivoDAO):
    def crear(self, evento):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO EventoDispositivo (id_dispositivo, id_usuario, tipo_evento, detalle) VALUES (%s, %s, %s, %s)",
            (evento.id_dispositivo, evento.id_usuario, evento.tipo_evento, evento.detalle)
        )
        conn.commit()
        id_evento = cursor.lastrowid
        conn.close()
        return id_evento

    def obtener_todos(self):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT id_evento, id_dispositivo, id_usuario, tipo_evento, fecha_hora, detalle FROM EventoDispositivo")
        rows = cursor.fetchall()
        conn.close()
        return [EventoDispositivo(row[0], row[1], row[2], row[3], row[4], row[5]) for row in rows]

    def obtener_por_id(self, id_evento):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT id_evento, id_dispositivo, id_usuario, tipo_evento, fecha_hora, detalle FROM EventoDispositivo WHERE id_evento = %s", (id_evento,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return EventoDispositivo(row[0], row[1], row[2], row[3], row[4], row[5])
        return None

    def obtener_por_dispositivo_id(self, id_dispositivo):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT id_evento, id_dispositivo, id_usuario, tipo_evento, fecha_hora, detalle FROM EventoDispositivo WHERE id_dispositivo = %s", (id_dispositivo,))
        rows = cursor.fetchall()
        conn.close()
        return [EventoDispositivo(row[0], row[1], row[2], row[3], row[4], row[5]) for row in rows]

    def eliminar(self, id_evento):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM EventoDispositivo WHERE id_evento = %s", (id_evento,))
        conn.commit()
        conn.close()
