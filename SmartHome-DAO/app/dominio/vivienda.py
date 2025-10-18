class Vivienda:
    def __init__(self, id_vivienda, nombre_vivienda, direccion, id_administrador, activa=True):
        self.__id_vivienda = id_vivienda
        self.__nombre_vivienda = nombre_vivienda
        self.__direccion = direccion
        self.__id_administrador = id_administrador
        self.__activa = activa

    # Getters
    @property
    def id_vivienda(self):
        return self.__id_vivienda

    @property
    def nombre_vivienda(self):
        return self.__nombre_vivienda

    @property
    def direccion(self):
        return self.__direccion

    @property
    def id_administrador(self):
        return self.__id_administrador

    @property
    def activa(self):
        return self.__activa

    # Setters
    @id_vivienda.setter
    def id_vivienda(self, value):
        self.__id_vivienda = value

    @nombre_vivienda.setter
    def nombre_vivienda(self, value):
        self.__nombre_vivienda = value

    @direccion.setter
    def direccion(self, value):
        self.__direccion = value

    @id_administrador.setter
    def id_administrador(self, value):
        self.__id_administrador = value

    @activa.setter
    def activa(self, value):
        self.__activa = value

    def __str__(self):
        return f"Vivienda(ID: {self.__id_vivienda}, Nombre: {self.__nombre_vivienda}, Admin ID: {self.__id_administrador})"
