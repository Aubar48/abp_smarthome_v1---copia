from datetime import datetime

class EventoDispositivo:
    def __init__(self, id_evento, id_dispositivo, id_usuario, tipo_evento, fecha_hora=None, detalle=None):
        self.id_evento = id_evento
        self.id_dispositivo = id_dispositivo
        self.id_usuario = id_usuario
        self.tipo_evento = tipo_evento
        self.fecha_hora = fecha_hora if fecha_hora else datetime.now()
        self.detalle = detalle

    def __str__(self):
        return f"Evento(ID: {self.id_evento}, Dispositivo ID: {self.id_dispositivo}, Usuario ID: {self.id_usuario}, Evento: {self.tipo_evento}, Fecha: {self.fecha_hora})"
