usuarios = {}

def registrar(email, nombre, apellido, dni, contraseña):
    if email in usuarios:
        return "Ya existe una cuenta con ese email."

    rol = "admin" if len(usuarios) == 0 else "cliente"

    usuarios[email] = {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "contraseña": contraseña,
        "rol": rol
    }
    return f"¡Registro exitoso! Rol asignado: {rol}"

def iniciar_sesion(email ,contraseña):
    usuario = usuarios.get(email)
    if usuario and usuario["contraseña"] == contraseña:
        mensaje = f"Bienvenido, {usuario['nombre']} ({usuario['rol']})"
        return mensaje, usuario["rol"]
    else:
        return "Email o contraseña incorrectos.", None

def ver_datos_personales(email):
    usuario = usuarios.get(email)
    if usuario:
        return (
            f"\n📄 DATOS PERSONALES\n"
            f"Nombre    : {usuario['nombre']}\n"
            f"Apellido  : {usuario['apellido']}\n"
            f"DNI       : {usuario['dni']}\n"
            f"Email     : {email}\n"
            f"Rol       : {usuario['rol']}\n"
        )
    else:
        return "❌ Usuario no encontrado."


def agregar_usuario(email, nombre, apellido, dni, contraseña):
    if email in usuarios:
        return "❌ Ya existe un usuario con ese email."

    usuario  =  {
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "contraseña": contraseña,
        "rol": "cliente"  # Los usuarios agregados por admin son clientes por defecto
    }
    usuarios[email] = usuario
    
    return f"✅ Usuario agregado correctamente: {nombre} ({email})"
