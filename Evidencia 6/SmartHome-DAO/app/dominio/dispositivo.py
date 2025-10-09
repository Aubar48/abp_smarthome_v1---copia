class Dispositivo:
    def __init__(self, id_dispositivo, nombre_dispositivo, tipo, estado, ubicacion, id_vivienda):
        self.id_dispositivo = id_dispositivo
        self.nombre_dispositivo = nombre_dispositivo
        self.tipo = tipo
        self.estado = estado
        self.ubicacion = ubicacion
        self.id_vivienda = id_vivienda

    def __str__(self):
        return f"Dispositivo(ID: {self.id_dispositivo}, Nombre: {self.nombre_dispositivo}, Tipo: {self.tipo}, Estado: {self.estado})"
