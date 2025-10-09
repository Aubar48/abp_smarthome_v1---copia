from app.services.usuario_service import UsuarioService
from app.services.vivienda_service import ViviendaService
from app.services.dispositivo_service import DispositivoService
from app.services.evento_dispositivo_service import EventoDispositivoService
import getpass


def panel_administrador(usuario):
    print(f"\n--- Panel de Administrador: ¡Bienvenido, {usuario.nombre}! ---")

    while True:
        print("\nOpciones de Administrador:")
        print("1. Gestionar Usuarios")
        print("2. Gestionar Viviendas")
        print("3. Gestionar Dispositivos")
        print("4. Ver historial de eventos")
        print("5. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            gestionar_usuarios_admin()
        elif opcion == '2':
            gestionar_viviendas_admin(usuario)
        elif opcion == '3':
            gestionar_dispositivos_admin()
        elif opcion == '4':
            ver_historial_eventos_admin()
        elif opcion == '5':
            break
        else:
            print("Opción no válida.")


def gestionar_usuarios_admin():
    usuario_service = UsuarioService()
    print("\n--- Gestión de Usuarios ---")
    while True:
        print("1. Listar todos los usuarios")
        print("2. Registrar nuevo usuario")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("0. Volver al panel principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            usuarios = usuario_service.obtener_todos_los_usuarios()
            print("\n--- Lista de todos los usuarios ---")
            for u in usuarios:
                print(
                    f"ID: {u.id_usuario}, Nombre: {u.nombre}, Email: {u.email}, Rol: {u.rol}")

        elif opcion == '2':
            nombre = input("Nombre del nuevo usuario: ")
            email = input("Email del nuevo usuario: ")
            contraseña = getpass.getpass("Contraseña del nuevo usuario: ")
            rol = input("Rol (administrador/usuario): ")
            usuario_service.registrar_usuario(nombre, email, contraseña, rol)
            print("¡Usuario registrado exitosamente!")

        elif opcion == '3':
            id_usuario = int(input("ID del usuario a actualizar: "))
            usuario = usuario_service.usuario_dao.obtener_por_id(id_usuario)
            if usuario:
                nombre = input(
                    f"Nuevo nombre ({usuario.nombre}): ") or usuario.nombre
                email = input(
                    f"Nuevo email ({usuario.email}): ") or usuario.email
                rol = input(f"Nuevo rol ({usuario.rol}): ") or usuario.rol

                usuario_actualizado = usuario_service.actualizar_usuario(
                    id_usuario, nombre, email, rol)
                if usuario_actualizado:
                    print("¡Usuario actualizado exitosamente!")
            else:
                print("Usuario no encontrado.")

        elif opcion == '4':
            id_usuario = int(input("ID del usuario a eliminar: "))
            if usuario_service.usuario_dao.obtener_por_id(id_usuario):
                confirmacion = input(
                    f"¿Seguro que desea eliminar el usuario con ID {id_usuario}? (s/n): ")
                if confirmacion.lower() == 's':
                    usuario_service.eliminar_usuario(id_usuario)
                    print("¡Usuario eliminado exitosamente!")
            else:
                print("Usuario no encontrado.")

        elif opcion == '0':
            break
        else:
            print("Opción no válida.")


def gestionar_viviendas_admin(usuario):
    vivienda_service = ViviendaService()
    print("\n--- Gestión de Viviendas ---")
    while True:
        print("1. Crear nueva vivienda")
        print("2. Asignar usuario a vivienda")
        print("0. Volver al panel principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            nombre_vivienda = input("Nombre de la nueva vivienda: ")
            direccion = input("Dirección de la nueva vivienda: ")
            vivienda_service.crear_vivienda(
                nombre_vivienda, direccion, usuario.id_usuario)
            print("¡Vivienda creada exitosamente!")
        elif opcion == '2':
            id_usuario_asignar = int(input("ID del usuario a asignar: "))
            id_vivienda = int(input("ID de la vivienda a asignar: "))
            vivienda_service.asignar_usuario_a_vivienda(
                id_usuario_asignar, id_vivienda)
            print("¡Usuario asignado a la vivienda!")
        elif opcion == '0':
            break
        else:
            print("Opción no válida.")


def gestionar_dispositivos_admin():
    dispositivo_service = DispositivoService()
    print("\n--- Gestión de Dispositivos ---")
    while True:
        print("1. Listar todos los dispositivos")
        print("2. Agregar nuevo dispositivo")
        print("3. Actualizar dispositivo")
        print("4. Eliminar dispositivo")
        print("0. Volver al panel principal")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == '1':
            dispositivos = dispositivo_service.dispositivo_dao.obtener_todos()
            print("\n--- Lista de todos los dispositivos ---")
            for d in dispositivos:
                print(f"ID: {d.id_dispositivo}, Nombre: {d.nombre_dispositivo}, Tipo: {d.tipo}, Estado: {d.estado}, Ubicación: {d.ubicacion}, Vivienda ID: {d.id_vivienda}")

        elif opcion == '2':
            nombre = input("Nombre del nuevo dispositivo: ")
            tipo = input("Tipo de dispositivo (luz, sensor, camara): ")
            ubicacion = input("Ubicación del dispositivo: ")
            id_vivienda = int(input("ID de la vivienda donde se instalará: "))
            dispositivo_service.crear_dispositivo_completo(
                nombre, tipo, ubicacion, id_vivienda)
            print("¡Dispositivo agregado a la vivienda!")

        elif opcion == '3':
            id_dispositivo = int(input("ID del dispositivo a actualizar: "))
            dispositivo = dispositivo_service.dispositivo_dao.obtener_por_id(
                id_dispositivo)
            if dispositivo:
                nombre = input(
                    f"Nuevo nombre ({dispositivo.nombre_dispositivo}): ") or dispositivo.nombre_dispositivo
                tipo = input(
                    f"Nuevo tipo ({dispositivo.tipo}): ") or dispositivo.tipo
                estado = input(
                    f"Nuevo estado ({dispositivo.estado}): ") or dispositivo.estado
                ubicacion = input(
                    f"Nueva ubicación ({dispositivo.ubicacion}): ") or dispositivo.ubicacion

                dispositivo_actualizado = dispositivo_service.actualizar_dispositivo_completo(
                    id_dispositivo, nombre, tipo, estado, ubicacion)
                if dispositivo_actualizado:
                    print("¡Dispositivo actualizado exitosamente!")
            else:
                print("Dispositivo no encontrado.")

        elif opcion == '4':
            id_dispositivo = int(input("ID del dispositivo a eliminar: "))
            if dispositivo_service.dispositivo_dao.obtener_por_id(id_dispositivo):
                confirmacion = input(
                    f"¿Seguro que desea eliminar el dispositivo con ID {id_dispositivo}? (s/n): ")
                if confirmacion.lower() == 's':
                    dispositivo_service.dispositivo_dao.eliminar(
                        id_dispositivo)
                    print("¡Dispositivo eliminado exitosamente!")
            else:
                print("Dispositivo no encontrado.")

        elif opcion == '0':
            break
        else:
            print("Opción no válida.")


def ver_historial_eventos_admin():
    evento_service = EventoDispositivoService()
    print("\n--- Historial de Eventos del Sistema ---")
    eventos = evento_service.obtener_todos_los_eventos()

    if not eventos:
        print("No hay eventos registrados en el sistema.")
        return

    for evento in eventos:
        print(f"ID: {evento.id_evento}, Fecha: {evento.fecha_hora.strftime('%Y-%m-%d %H:%M:%S')}, "
              f"Dispositivo ID: {evento.id_dispositivo}, Usuario ID: {evento.id_usuario}, "
              f"Tipo: {evento.tipo_evento}, Detalle: {evento.detalle}")
    print("-" * 20)


def gestionar_dispositivos_usuario(usuario, vivienda):
    dispositivo_service = DispositivoService()
    vivienda_service = ViviendaService()

    while True:
        dispositivos = vivienda_service.obtener_dispositivos_por_vivienda(
            vivienda.id_vivienda)
        print(f"\n--- Dispositivos en {vivienda.nombre_vivienda} ---")
        if not dispositivos:
            print("No hay dispositivos en esta vivienda.")
            break

        for i, d in enumerate(dispositivos):
            print(f"{i + 1}. {d.nombre_dispositivo} ({d.tipo}): {d.estado}")

        print("0. Volver al menú de viviendas")
        opcion = input(
            "Seleccione un dispositivo para cambiar su estado o '0' para volver: ").strip()

        # Extraer solo el primer número si el usuario escribe algo como "0. Volver"
        opcion_num = opcion.split('.')[0].split()[0].strip()

        if opcion_num == '0':
            break

        try:
            idx = int(opcion_num) - 1
            if 0 <= idx < len(dispositivos):
                dispositivo_seleccionado = dispositivos[idx]
                nuevo_estado = 'encendido' if dispositivo_seleccionado.estado == 'apagado' else 'apagado'

                if dispositivo_service.cambiar_estado_dispositivo(dispositivo_seleccionado.id_dispositivo, nuevo_estado, usuario.id_usuario):
                    print(
                        f"El dispositivo '{dispositivo_seleccionado.nombre_dispositivo}' se ha {nuevo_estado}.")
                    print("¡Acción registrada en el historial de eventos!")
                else:
                    print("No se pudo cambiar el estado del dispositivo.")
            else:
                print("Selección no válida.")
        except ValueError:
            print("Entrada no válida.")


def panel_usuario(usuario):
    print(f"\n--- Panel de Usuario: ¡Bienvenido, {usuario.nombre}! ---")
    vivienda_service = ViviendaService()

    while True:
        print("\nTus Viviendas:")
        viviendas = vivienda_service.obtener_viviendas_por_usuario(
            usuario.id_usuario)
        if not viviendas:
            print("No tienes viviendas asignadas.")
            break

        for i, vivienda in enumerate(viviendas):
            print(f"{i + 1}. {vivienda.nombre_vivienda} ({vivienda.direccion})")

        print("0. Salir")
        opcion = input(
            "Seleccione una vivienda para gestionar sus dispositivos o '0' para salir: ").strip()

        # Extraer solo el primer número si el usuario escribe algo como "0. Salir"
        opcion_num = opcion.split('.')[0].split()[0].strip()

        if opcion_num == '0':
            break

        try:
            idx = int(opcion_num) - 1
            if 0 <= idx < len(viviendas):
                vivienda_seleccionada = viviendas[idx]
                gestionar_dispositivos_usuario(usuario, vivienda_seleccionada)
            else:
                print("Selección no válida.")
        except ValueError:
            print("Entrada no válida.")


def main():
    # ... (código existente sin cambios)
    usuario_service = UsuarioService()

    print("--- ¡Bienvenido al Sistema SmartHome! ---")

    admin = usuario_service.usuario_dao.obtener_por_email(
        "admin@smarthome.com")
    if not admin:
        print("Creando usuario administrador por defecto...")
        usuario_service.registrar_usuario(
            "Administrador Principal", "admin@smarthome.com", "admin123", "administrador")
        print("Usuario 'admin@smarthome.com' con contraseña 'admin123' creado.")

    while True:
        email = input("Email: ")
        contraseña = getpass.getpass("Contraseña: ")

        usuario = usuario_service.login(email, contraseña)

        if usuario:
            if usuario.rol == 'administrador':
                panel_administrador(usuario)
            else:
                panel_usuario(usuario)
            break
        else:
            print("Email o contraseña incorrectos. Intente de nuevo.")


if __name__ == "__main__":
    main()
