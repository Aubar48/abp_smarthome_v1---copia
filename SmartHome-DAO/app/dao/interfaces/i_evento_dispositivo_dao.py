from abc import ABC, abstractmethod

class IEventoDispositivoDAO(ABC):
    @abstractmethod
    def crear(self, evento):
        pass

    @abstractmethod
    def obtener_todos(self):
        pass

    @abstractmethod
    def obtener_por_id(self, id):
        pass

    @abstractmethod
    def obtener_por_dispositivo_id(self, id_dispositivo):
        pass

    @abstractmethod
    def eliminar(self, id):
        pass
