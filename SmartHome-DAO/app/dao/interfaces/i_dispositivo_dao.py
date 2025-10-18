from abc import ABC, abstractmethod

class IDispositivoDAO(ABC):
    @abstractmethod
    def crear(self, dispositivo):
        pass

    @abstractmethod
    def obtener_todos(self):
        pass

    @abstractmethod
    def obtener_por_id(self, id):
        pass

    @abstractmethod
    def actualizar(self, dispositivo):
        pass

    @abstractmethod
    def eliminar(self, id):
        pass
