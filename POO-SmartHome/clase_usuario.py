"""
Clase Usuario - Sistema SmartHome Simplificado
Representa a los usuarios del sistema con dos roles: administrador y usuario normal
"""

class Usuario:
    """
    Clase que representa un usuario del sistema SmartHome
    Maneja autenticación, datos personales y control de sesión
    """
    
    def __init__(self, email, nombre, contraseña, rol):
        """Constructor: crear un nuevo usuario con sus datos básicos"""
        self.__email = email                    # Email único del usuario (privado)
        self._nombre = nombre                   # Nombre completo del usuario
        self.__contraseña = contraseña          # Contraseña encriptada (privado)
        self._rol = rol                        # Rol: 'administrador' o 'usuario'
        self._sesion_activa = False            # Estado de la sesión actual
    
    def get_email(self):
        """Obtener el email del usuario"""
        return self.__email

    def get_contraseña(self):
        """Obtener la contraseña actual del usuario"""
        return self.__contraseña

    def set_contraseña(self, nueva_contraseña):
        """Cambiar la contraseña del usuario"""
        self.__contraseña = nueva_contraseña  

    def iniciar_sesion(self, email, contraseña):
        """Validar credenciales e iniciar sesión en el sistema"""
        if self.__email == email and self.__contraseña == contraseña:
            self._sesion_activa = True
            return "Sesión iniciada correctamente."
        return "Email o contraseña incorrectos."
        
    def ver_datos_personales(self):
        """Mostrar todos los datos personales del usuario"""
        return (
            f"Nombre: {self._nombre}\n"
            f"Email: {self.__email}\n"
            f"Contraseña: {self.__contraseña}\n"
            f"Rol: {self._rol}"
        )

    def registrar_nuevo_usuario(self, email, nombre, contraseña, rol):
        """Crear una nueva instancia de usuario (solo administradores)"""
        return Usuario(email, nombre, contraseña, rol)
    
    def modificar_datos_personales(self, nuevo_email=None, nueva_contraseña=None, nuevo_rol=None):
        """Actualizar datos personales del usuario (opcionales)"""
        if nuevo_email:
            self.__email = nuevo_email
        if nueva_contraseña:
            self.__contraseña = nueva_contraseña
        if nuevo_rol:
            self._rol = nuevo_rol
        return "Datos modificados correctamente"
    
    def eliminar_usuario(self):
        """Eliminar usuario del sistema (placeholder para funcionalidad futura)"""
        pass    
    
    def gestionar_dispositivos(self, accion, id_dispositivo):
        """Controlar dispositivos según permisos del rol (placeholder)"""
        pass 
    
    def cerrar_sesion(self):
        """Finalizar la sesión actual del usuario"""
        self._sesion_activa = False
        return "Sesión cerrada."
    
