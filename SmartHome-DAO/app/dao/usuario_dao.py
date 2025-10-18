from ..conn.db_conn import obtener_conexion
from ..dominio.usuario import Usuario
from .interfaces.i_usuario_dao import IUsuarioDAO


class UsuarioDAO(IUsuarioDAO):
    def crear(self, usuario):
        conn = None
        cursor = None
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Usuario (email, nombre, contraseña, rol) VALUES (%s, %s, %s, %s)",
                (usuario.email, usuario.nombre, usuario.contraseña, usuario.rol)
            )
            conn.commit()
            id_usuario = cursor.lastrowid
            return id_usuario
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Error al crear usuario: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def obtener_todos(self):
        conn = None
        cursor = None
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id_usuario, email, nombre, contraseña, rol, fecha_registro, activo FROM Usuario")
            rows = cursor.fetchall()
            return [Usuario(row[0], row[1], row[2], row[3], row[4], row[5], row[6]) for row in rows]
        except Exception as e:
            print(f"Error al obtener todos los usuarios: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def obtener_por_id(self, id_usuario):
        conn = None
        cursor = None
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id_usuario, email, nombre, contraseña, rol, fecha_registro, activo FROM Usuario WHERE id_usuario = %s", (id_usuario,))
            row = cursor.fetchone()
            if row:
                return Usuario(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            return None
        except Exception as e:
            print(f"Error al obtener usuario por ID: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def obtener_por_email(self, email):
        conn = None
        cursor = None
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT id_usuario, email, nombre, contraseña, rol, fecha_registro, activo FROM Usuario WHERE email = %s", (email,))
            row = cursor.fetchone()
            if row:
                return Usuario(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            return None
        except Exception as e:
            print(f"Error al obtener usuario por email: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def actualizar(self, usuario):
        conn = None
        cursor = None
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE Usuario SET email = %s, nombre = %s, contraseña = %s, rol = %s, activo = %s WHERE id_usuario = %s",
                (usuario.email, usuario.nombre, usuario.contraseña,
                 usuario.rol, usuario.activo, usuario.id_usuario)
            )
            conn.commit()
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Error al actualizar usuario: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def eliminar(self, id_usuario):
        conn = None
        cursor = None
        try:
            conn = obtener_conexion()
            cursor = conn.cursor()
            cursor.execute(
                "DELETE FROM Usuario WHERE id_usuario = %s", (id_usuario,))
            conn.commit()
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Error al eliminar usuario: {e}")
            raise
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()
