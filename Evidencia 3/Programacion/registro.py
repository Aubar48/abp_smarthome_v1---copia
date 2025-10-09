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

def iniciar_sesion(email, contraseña):
    usuario = usuarios.get(email)
    if usuario and usuario["contraseña"] == contraseña:
        mensaje = f"Bienvenido, {usuario['nombre']} ({usuario['rol']})"
        return mensaje, usuario["rol"]
    else:
        return "Email o contraseña incorrectos.", None