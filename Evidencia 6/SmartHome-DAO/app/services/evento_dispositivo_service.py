from ..dao.evento_dispositivo_dao import EventoDispositivoDAO
from ..dominio.evento_dispositivo import EventoDispositivo


class EventoDispositivoService:
    def __init__(self):
        self.evento_dao = EventoDispositivoDAO()

    def crear_evento(self, id_dispositivo, id_usuario, tipo_evento, detalle=None):
        """Crea un nuevo evento en la base de datos"""
        nuevo_evento = EventoDispositivo(
            None, id_dispositivo, id_usuario, tipo_evento, None, detalle)
        return self.evento_dao.crear(nuevo_evento)

    def obtener_eventos_por_dispositivo(self, id_dispositivo):
        """Obtiene todos los eventos de un dispositivo específico"""
        return self.evento_dao.obtener_por_dispositivo_id(id_dispositivo)

    def obtener_todos_los_eventos(self):
        """Obtiene todos los eventos del sistema"""
        return self.evento_dao.obtener_todos()

    def obtener_evento_por_id(self, id_evento):
        """Obtiene un evento por su ID"""
        return self.evento_dao.obtener_por_id(id_evento)
