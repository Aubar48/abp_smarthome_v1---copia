from abc import ABC, abstractmethod

class IViviendaDAO(ABC):
    @abstractmethod
    def crear(self, vivienda):
        pass

    @abstractmethod
    def obtener_todos(self):
        pass

    @abstractmethod
    def obtener_por_id(self, id):
        pass

    @abstractmethod
    def actualizar(self, vivienda):
        pass

    @abstractmethod
    def eliminar(self, id):
        pass
