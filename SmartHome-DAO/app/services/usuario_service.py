from ..dao.usuario_dao import UsuarioDAO
from ..dominio.usuario import Usuario


class UsuarioService:
    def __init__(self):
        self.usuario_dao = UsuarioDAO()

    def login(self, email, contraseña):
        usuario = self.usuario_dao.obtener_por_email(email)
        if usuario and usuario.contraseña == contraseña:
            return usuario
        return None

    def registrar_usuario(self, nombre, email, contraseña, rol):
        # El ID se autogenera en la base de datos, pasamos None
        nuevo_usuario = Usuario(None, email, nombre, contraseña, rol)
        return self.usuario_dao.crear(nuevo_usuario)

    def obtener_todos_los_usuarios(self):
        """Obtiene todos los usuarios del sistema"""
        return self.usuario_dao.obtener_todos()

    def actualizar_usuario(self, id_usuario, nombre, email, rol):
        """Actualiza los datos de un usuario sin cambiar la contraseña"""
        usuario = self.usuario_dao.obtener_por_id(id_usuario)
        if usuario:
            usuario.nombre = nombre
            usuario.email = email
            usuario.rol = rol
            self.usuario_dao.actualizar(usuario)
            return usuario
        return None

    def actualizar_usuario_con_contraseña(self, id_usuario, nombre, email, contraseña, rol):
        """Actualiza los datos de un usuario incluyendo la contraseña"""
        usuario = self.usuario_dao.obtener_por_id(id_usuario)
        if usuario:
            usuario.nombre = nombre
            usuario.email = email
            usuario.contraseña = contraseña
            usuario.rol = rol
            self.usuario_dao.actualizar(usuario)
            return usuario
        return None

    def eliminar_usuario(self, id_usuario):
        """Elimina un usuario del sistema"""
        self.usuario_dao.eliminar(id_usuario)
