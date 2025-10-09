from ..conn.db_conn import obtener_conexion
from ..dominio.usuario import Usuario
from .interfaces.i_usuario_dao import IUsuarioDAO

class UsuarioDAO(IUsuarioDAO):
    def crear(self, usuario):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Usuario (email, nombre, contraseña, rol) VALUES (%s, %s, %s, %s)",
            (usuario.email, usuario.nombre, usuario.contraseña, usuario.rol)
        )
        conn.commit()
        id_usuario = cursor.lastrowid
        conn.close()
        return id_usuario

    def obtener_todos(self):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT id_usuario, email, nombre, contraseña, rol, fecha_registro, activo FROM Usuario")
        rows = cursor.fetchall()
        conn.close()
        return [Usuario(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) for row in rows]

    def obtener_por_id(self, id_usuario):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT id_usuario, email, nombre, contraseña, rol, fecha_registro, activo FROM Usuario WHERE id_usuario = %s", (id_usuario,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Usuario(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        return None
    
    def obtener_por_email(self, email):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("SELECT id_usuario, email, nombre, contraseña, rol, fecha_registro, activo FROM Usuario WHERE email = %s", (email,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Usuario(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        return None

    def actualizar(self, usuario):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Usuario SET email = %s, nombre = %s, contraseña = %s, rol = %s, activo = %s WHERE id_usuario = %s",
            (usuario.email, usuario.nombre, usuario.contraseña, usuario.rol, usuario.activo, usuario.id_usuario)
        )
        conn.commit()
        conn.close()

    def eliminar(self, id_usuario):
        conn = obtener_conexion()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Usuario WHERE id_usuario = %s", (id_usuario,))
        conn.commit()
        conn.close()
