"""
Clase EventoDispositivo - Sistema SmartHome Simplificado
Registra eventos y actividades de los dispositivos IoT
"""

class EventoDispositivo:
    """
    Clase que representa un evento generado por un dispositivo
    Registra actividades como encendido/apagado, lecturas de sensores, etc.
    """
    
    def __init__(self, id_evento, fecha_hora, detalle, valor):
        """Constructor: crear un nuevo evento con ID, timestamp, descripción y valor"""
        self.fecha_hora = fecha_hora    # Momento exacto del evento          
        self.detalle = detalle          # Descripción del evento                
        self.valor = valor              # Valor numérico o estado   
        self.id_evento = id_evento      # Identificador único del evento
        
    def cargar_detalle_automatizacion(self, id_dispositivo, id_automatizacion, detalle):
        """Cargar detalles de automatización relacionada (placeholder)"""
        pass

   

            