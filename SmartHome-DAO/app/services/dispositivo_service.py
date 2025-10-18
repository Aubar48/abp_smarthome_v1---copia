from ..dao.dispositivo_dao import DispositivoDAO
from ..dao.evento_dispositivo_dao import EventoDispositivoDAO
from ..dominio.dispositivo import Dispositivo
from ..dominio.evento_dispositivo import EventoDispositivo


class DispositivoService:
    def __init__(self):
        self.dispositivo_dao = DispositivoDAO()
        self.evento_dao = EventoDispositivoDAO()

    def crear_dispositivo_completo(self, nombre, tipo, ubicacion, id_vivienda):
        """Crea un nuevo dispositivo en la base de datos"""
        nuevo_dispositivo = Dispositivo(
            None, nombre, tipo, 'apagado', ubicacion, id_vivienda)
        return self.dispositivo_dao.crear(nuevo_dispositivo)

    def cambiar_estado_dispositivo(self, id_dispositivo, nuevo_estado, id_usuario):
        """Cambia el estado de un dispositivo y registra el evento"""
        dispositivo = self.dispositivo_dao.obtener_por_id(id_dispositivo)
        if dispositivo:
            estado_anterior = dispositivo.estado
            dispositivo.estado = nuevo_estado
            self.dispositivo_dao.actualizar(dispositivo)

            # Registrar el evento con el tipo correcto según el nuevo estado
            tipo_evento = nuevo_estado  # 'encendido' o 'apagado'
            detalle = f"Estado cambiado de '{estado_anterior}' a '{nuevo_estado}'"
            evento = EventoDispositivo(
                None, id_dispositivo, id_usuario, tipo_evento, None, detalle)
            self.evento_dao.crear(evento)
            return True
        return False

    def actualizar_dispositivo_completo(self, id_dispositivo, nombre, tipo, estado, ubicacion):
        """Actualiza los datos de un dispositivo"""
        dispositivo = self.dispositivo_dao.obtener_por_id(id_dispositivo)
        if dispositivo:
            dispositivo.nombre_dispositivo = nombre
            dispositivo.tipo = tipo
            dispositivo.estado = estado
            dispositivo.ubicacion = ubicacion
            self.dispositivo_dao.actualizar(dispositivo)
            return dispositivo
        return None

    def obtener_dispositivo_por_id(self, id_dispositivo):
        """Obtiene un dispositivo por su ID"""
        return self.dispositivo_dao.obtener_por_id(id_dispositivo)

    def obtener_todos_los_dispositivos(self):
        """Obtiene todos los dispositivos del sistema"""
        return self.dispositivo_dao.obtener_todos()
