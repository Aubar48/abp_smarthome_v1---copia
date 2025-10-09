from ..dao.vivienda_dao import ViviendaDAO
from ..dao.dispositivo_dao import DispositivoDAO
from ..dominio.vivienda import Vivienda
from ..dominio.dispositivo import Dispositivo

class ViviendaService:
    def __init__(self):
        self.vivienda_dao = ViviendaDAO()
        self.dispositivo_dao = DispositivoDAO()

    def crear_vivienda(self, nombre_vivienda, direccion, id_administrador):
        nueva_vivienda = Vivienda(None, nombre_vivienda, direccion, id_administrador)
        return self.vivienda_dao.crear(nueva_vivienda)

    def asignar_usuario_a_vivienda(self, id_usuario, id_vivienda):
        self.vivienda_dao.asignar_usuario(id_usuario, id_vivienda)

    def obtener_viviendas_por_usuario(self, id_usuario):
        return self.vivienda_dao.obtener_por_usuario(id_usuario)

    def agregar_dispositivo_a_vivienda(self, nombre, tipo, ubicacion, id_vivienda):
        nuevo_dispositivo = Dispositivo(None, nombre, tipo, 'apagado', ubicacion, id_vivienda)
        self.dispositivo_dao.crear(nuevo_dispositivo)

    def obtener_dispositivos_por_vivienda(self, id_vivienda):
        return self.dispositivo_dao.obtener_por_vivienda(id_vivienda)
