"""
Clase Dispositivo - Sistema SmartHome Simplificado
Representa dispositivos IoT: luces, sensores y cámaras
"""

class Dispositivo:
    """
    Clase que representa un dispositivo IoT en el sistema SmartHome
    Maneja estados básicos (encendido/apagado) y operaciones CRUD
    """
    
    def __init__(self, id_dispositivo, nombre_dispositivo, tipo): 
        """Constructor: crear un nuevo dispositivo con ID, nombre y tipo"""
        self._nombre_dispositivo = nombre_dispositivo   # Nombre descriptivo del dispositivo
        self._tipo = tipo                              # Tipo: 'luz', 'sensor', 'camara'
        self._estado = "apagado"                       # Estado inicial: apagado por defecto
        self.__id_dispositivo = id_dispositivo         # Identificador único (privado)

    def get_id_dispositivo(self):
        """Obtener el ID único del dispositivo"""
        return self.__id_dispositivo
    
    def registrar_nuevos_dispositivo(self, id_dispositivo, nombre_dispositivo, tipo):
        """Registrar un nuevo dispositivo en el sistema (placeholder)"""
        pass
    
    def modificar_datos_dispositivo(self, id_dispositivo, nombre_dispositivo, tipo):
        """Actualizar información del dispositivo (placeholder)"""
        pass    
    
    def listar_dispositivos(self):
        """Mostrar lista de todos los dispositivos (placeholder)"""
        pass
    
    def eliminar_dispositivo(self, id_dispositivo):
        """Eliminar dispositivo del sistema (placeholder)"""
        pass
    
    def encender(self):
        """Cambiar estado del dispositivo a encendido"""
        if self._estado == "apagado":
            self._estado = "encendido"
            print(f"{self._nombre_dispositivo} encendido.")
        

    def apagar(self):
        """Cambiar estado del dispositivo a apagado"""        
        if self._estado == "encendido":
            self._estado = "apagado"
            print(f"{self._nombre_dispositivo} apagado.")

    def modificarConfiguracion(self, configuracion):
        """Modificar configuración específica del dispositivo (placeholder)"""
        pass
    