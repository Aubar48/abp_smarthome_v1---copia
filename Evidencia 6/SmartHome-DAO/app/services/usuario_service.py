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
