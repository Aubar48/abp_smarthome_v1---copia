"""
Script para verificar usuarios en la base de datos
"""
from app.services.usuario_service import UsuarioService

usuario_service = UsuarioService()

print("\n=== USUARIOS EN LA BASE DE DATOS ===\n")

try:
    usuarios = usuario_service.obtener_todos_los_usuarios()

    if usuarios:
        for usuario in usuarios:
            print(f"ID: {usuario.id_usuario}")
            print(f"Nombre: {usuario.nombre}")
            print(f"Email: {usuario.email}")
            print(f"Contraseña: {usuario.contraseña}")
            print(f"Rol: {usuario.rol}")
            print(f"Activo: {usuario.activo}")
            print("-" * 40)
    else:
        print("No hay usuarios en la base de datos")

except Exception as e:
    print(f"Error al obtener usuarios: {e}")
    import traceback
    traceback.print_exc()
