class Dispositivo:
    def __init__(self, id_dispositivo, nombre_dispositivo, tipo, estado, ubicacion, id_vivienda):
        self.__id_dispositivo = id_dispositivo
        self.__nombre_dispositivo = nombre_dispositivo
        self.__tipo = tipo
        self.__estado = estado
        self.__ubicacion = ubicacion
        self.__id_vivienda = id_vivienda

    # Getters
    @property
    def id_dispositivo(self):
        return self.__id_dispositivo

    @property
    def nombre_dispositivo(self):
        return self.__nombre_dispositivo

    @property
    def tipo(self):
        return self.__tipo

    @property
    def estado(self):
        return self.__estado

    @property
    def ubicacion(self):
        return self.__ubicacion

    @property
    def id_vivienda(self):
        return self.__id_vivienda

    # Setters
    @id_dispositivo.setter
    def id_dispositivo(self, value):
        self.__id_dispositivo = value

    @nombre_dispositivo.setter
    def nombre_dispositivo(self, value):
        self.__nombre_dispositivo = value

    @tipo.setter
    def tipo(self, value):
        if value not in ['luz', 'sensor', 'camara']:
            raise ValueError("El tipo debe ser 'luz', 'sensor' o 'camara'")
        self.__tipo = value

    @estado.setter
    def estado(self, value):
        if value not in ['encendido', 'apagado']:
            raise ValueError("El estado debe ser 'encendido' o 'apagado'")
        self.__estado = value

    @ubicacion.setter
    def ubicacion(self, value):
        self.__ubicacion = value

    @id_vivienda.setter
    def id_vivienda(self, value):
        self.__id_vivienda = value

    def __str__(self):
        return f"Dispositivo(ID: {self.__id_dispositivo}, Nombre: {self.__nombre_dispositivo}, Tipo: {self.__tipo}, Estado: {self.__estado})"
