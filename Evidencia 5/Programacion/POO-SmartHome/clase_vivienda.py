"""
Clase Vivienda - Sistema SmartHome Simplificado
Representa las propiedades/casas donde se instalan dispositivos IoT
"""

class Vivienda:
    """
    Clase que representa una vivienda en el sistema SmartHome
    Almacena información básica: ID, nombre y ubicación física
    """
    
    def __init__(self, id_vivienda, ubicacion, nombre_vivienda):
        """Constructor: crear una nueva vivienda con ID, ubicación y nombre"""
        self._nombre_vivienda = nombre_vivienda     # Nombre descriptivo de la propiedad
        self.__ubicacion = ubicacion               # Dirección física (privado)
        self.__id_vivienda = id_vivienda           # Identificador único (privado)
        
    def get_ubicacion(self):
        """Obtener la ubicación/dirección de la vivienda"""
        return self.__ubicacion

    def get_id_vivienda(self):
        """Obtener el ID único de la vivienda"""
        return self.__id_vivienda  
        
    def ver_datos_vivienda(self):
        """Mostrar toda la información de la vivienda"""
        return (
            f"ID_vivienda: {self.__id_vivienda}\n"
            f"Nombre_vivienda: {self._nombre_vivienda}\n"
            f"Ubicacion: {self.__ubicacion}\n"
        )

    def registrar_nueva_vivienda(self, id_vivienda, ubicacion, nombre_vivienda):
        """Registrar una nueva vivienda en el sistema (placeholder)"""
        pass
    
    def modificar_datos_vivienda(self, id_vivienda, ubicacion, nombre_vivienda):
        """Actualizar información de la vivienda (placeholder)"""
        pass    
    
   