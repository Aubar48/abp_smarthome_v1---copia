class Usuario:
    def __init__(self, id_usuario, email, nombre, contraseña, rol, fecha_registro=None, activo=True):
        self.__id_usuario = id_usuario
        self.__email = email
        self.__nombre = nombre
        self.__contraseña = contraseña
        self.__rol = rol
        self.__fecha_registro = fecha_registro
        self.__activo = activo

    # Getters
    @property
    def id_usuario(self):
        return self.__id_usuario

    @property
    def email(self):
        return self.__email

    @property
    def nombre(self):
        return self.__nombre

    @property
    def contraseña(self):
        return self.__contraseña

    @property
    def rol(self):
        return self.__rol

    @property
    def fecha_registro(self):
        return self.__fecha_registro

    @property
    def activo(self):
        return self.__activo

    # Setters
    @id_usuario.setter
    def id_usuario(self, value):
        self.__id_usuario = value

    @email.setter
    def email(self, value):
        self.__email = value

    @nombre.setter
    def nombre(self, value):
        self.__nombre = value

    @contraseña.setter
    def contraseña(self, value):
        self.__contraseña = value

    @rol.setter
    def rol(self, value):
        if value not in ['administrador', 'usuario']:
            raise ValueError("El rol debe ser 'administrador' o 'usuario'")
        self.__rol = value

    @fecha_registro.setter
    def fecha_registro(self, value):
        self.__fecha_registro = value

    @activo.setter
    def activo(self, value):
        self.__activo = value

    def __str__(self):
        return f"Usuario(ID: {self.__id_usuario}, Nombre: {self.__nombre}, Email: {self.__email}, Rol: {self.__rol})"
