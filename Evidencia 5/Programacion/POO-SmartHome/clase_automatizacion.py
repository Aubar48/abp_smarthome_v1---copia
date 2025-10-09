"""
Clase Automatizacion - Sistema SmartHome Simplificado
Maneja reglas automáticas: si ocurre X condición, entonces ejecutar Y acción
"""

class Automatizacion:
    """
    Clase que representa una regla de automatización del hogar
    Define condiciones (sensores) y acciones (controlar dispositivos)
    """
    
    def __init__(self, id_auto, condicion, accion):   
        """Constructor: crear una nueva regla con ID, condición y acción"""
        self.__id_auto = id_auto        # Identificador único (privado)
        self.condicion = condicion      # Condición que activa la regla              
        self.accion = accion            # Acción a ejecutar cuando se cumple                    
        
    def get_id_auto(self):
        """Obtener el ID único de la automatización"""
        return self.__id_auto
        
    def registrar_nueva_automatizacion(self, id_auto, condicion, accion):
        """Crear una nueva regla de automatización (placeholder)"""
        pass    
    
    def modificar_datos_automatizacion(self, id_auto, condicion, accion):
        """Actualizar condición o acción de la regla (placeholder)"""
        pass            
    
    def eliminar_automatizacion(self, id_auto):
        """Eliminar regla de automatización del sistema (placeholder)"""
        pass    
    
    def activar(self):
        """Habilitar la regla de automatización (placeholder)"""
        pass    
    
    def desactivar(self):
        """Deshabilitar la regla de automatización (placeholder)"""
        pass
    
    def ver_info_automatizacion(self):
        """Mostrar información completa de la regla de automatización"""
        return (
            f"ID Automatizacion: {self.__id_auto}\n"
            f"Condicion: {self.condicion}\n"
            f"Accion: {self.accion}\n"
            ) 
        
        
        