from datetime import datetime


class EventoDispositivo:
    def __init__(self, id_evento, id_dispositivo, id_usuario, tipo_evento, fecha_hora=None, detalle=None):
        self.__id_evento = id_evento
        self.__id_dispositivo = id_dispositivo
        self.__id_usuario = id_usuario
        self.__tipo_evento = tipo_evento
        self.__fecha_hora = fecha_hora if fecha_hora else datetime.now()
        self.__detalle = detalle

    # Getters
    @property
    def id_evento(self):
        return self.__id_evento

    @property
    def id_dispositivo(self):
        return self.__id_dispositivo

    @property
    def id_usuario(self):
        return self.__id_usuario

    @property
    def tipo_evento(self):
        return self.__tipo_evento

    @property
    def fecha_hora(self):
        return self.__fecha_hora

    @property
    def detalle(self):
        return self.__detalle

    # Setters
    @id_evento.setter
    def id_evento(self, value):
        self.__id_evento = value

    @id_dispositivo.setter
    def id_dispositivo(self, value):
        self.__id_dispositivo = value

    @id_usuario.setter
    def id_usuario(self, value):
        self.__id_usuario = value

    @tipo_evento.setter
    def tipo_evento(self, value):
        self.__tipo_evento = value

    @fecha_hora.setter
    def fecha_hora(self, value):
        self.__fecha_hora = value

    @detalle.setter
    def detalle(self, value):
        self.__detalle = value

    def __str__(self):
        return f"Evento(ID: {self.__id_evento}, Dispositivo ID: {self.__id_dispositivo}, Usuario ID: {self.__id_usuario}, Evento: {self.__tipo_evento}, Fecha: {self.__fecha_hora})"
