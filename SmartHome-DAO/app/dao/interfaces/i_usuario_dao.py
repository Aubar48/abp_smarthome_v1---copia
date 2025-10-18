from abc import ABC, abstractmethod

class IUsuarioDAO(ABC):
    @abstractmethod
    def crear(self, usuario):
        pass

    @abstractmethod
    def obtener_todos(self):
        pass

    @abstractmethod
    def obtener_por_id(self, id):
        pass

    @abstractmethod
    def actualizar(self, usuario):
        pass

    @abstractmethod
    def eliminar(self, id):
        pass
