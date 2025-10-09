class Vivienda:
    def __init__(self, id_vivienda, nombre_vivienda, direccion, id_administrador, activa=True):
        self.id_vivienda = id_vivienda
        self.nombre_vivienda = nombre_vivienda
        self.direccion = direccion
        self.id_administrador = id_administrador
        self.activa = activa

    def __str__(self):
        return f"Vivienda(ID: {self.id_vivienda}, Nombre: {self.nombre_vivienda}, Admin ID: {self.id_administrador})"
