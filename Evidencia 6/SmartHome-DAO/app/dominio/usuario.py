class Usuario:
    def __init__(self, id_usuario, email, nombre, contraseña, rol, fecha_registro=None, activo=True):
        self.id_usuario = id_usuario
        self.email = email
        self.nombre = nombre
        self.contraseña = contraseña
        self.rol = rol
        self.fecha_registro = fecha_registro
        self.activo = activo

    def __str__(self):
        return f"Usuario(ID: {self.id_usuario}, Nombre: {self.nombre}, Email: {self.email}, Rol: {self.rol})"
