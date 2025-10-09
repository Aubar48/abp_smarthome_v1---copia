"""
Script de prueba para testear todas las funcionalidades de un ADMINISTRADOR
en el sistema SmartHome
"""
from app.services.usuario_service import UsuarioService
from app.services.vivienda_service import ViviendaService
from app.services.dispositivo_service import DispositivoService
from app.services.evento_dispositivo_service import EventoDispositivoService


def test_login_administrador():
    """Prueba el login de un administrador"""
    print("\n=== PRUEBA 1: Login de Administrador ===")
    usuario_service = UsuarioService()

    # Intentar login con el administrador
    usuario = usuario_service.login("admin@smarthome.com", "admin123")

    if usuario:
        print(f"✓ Login exitoso para: {usuario.nombre}")
        print(f"  - Email: {usuario.email}")
        print(f"  - Rol: {usuario.rol}")
        assert usuario.rol == "administrador", "El rol debería ser 'administrador'"
        return usuario
    else:
        print("✗ Login fallido")
        return None


def test_listar_todos_usuarios():
    """Prueba listar todos los usuarios del sistema"""
    print("\n=== PRUEBA 2: Listar Todos los Usuarios ===")
    usuario_service = UsuarioService()

    usuarios = usuario_service.obtener_todos_los_usuarios()

    print(f"✓ Sistema tiene {len(usuarios)} usuario(s):")
    for usuario in usuarios:
        print(
            f"  - ID: {usuario.id_usuario} | {usuario.nombre} ({usuario.email})")
        print(f"    Rol: {usuario.rol} | Activo: {usuario.activo}")

    return usuarios


def test_crear_usuario():
    """Prueba crear un nuevo usuario"""
    print("\n=== PRUEBA 3: Crear Nuevo Usuario ===")
    usuario_service = UsuarioService()

    # Datos del nuevo usuario de prueba
    nombre_test = "Usuario Test Admin"
    email_test = "test_admin@smarthome.com"
    contraseña_test = "test123"
    rol_test = "usuario"

    print(f"  Creando usuario: {nombre_test}")
    print(f"  Email: {email_test}")
    print(f"  Rol: {rol_test}")

    try:
        # Verificar si ya existe
        usuario_existente = usuario_service.usuario_dao.obtener_por_email(
            email_test)
        if usuario_existente:
            print(
                f"  ℹ Usuario ya existe con ID: {usuario_existente.id_usuario}")
            print(f"  Usando usuario existente para las pruebas")
            return usuario_existente.id_usuario

        id_nuevo = usuario_service.registrar_usuario(
            nombre_test, email_test, contraseña_test, rol_test
        )
        print(f"✓ Usuario creado exitosamente con ID: {id_nuevo}")

        # Verificar que se creó correctamente
        usuario_creado = usuario_service.usuario_dao.obtener_por_id(id_nuevo)
        assert usuario_creado is not None, "El usuario no se encontró después de crearlo"
        assert usuario_creado.email == email_test, "El email no coincide"
        print(f"✓ Verificación: Usuario encontrado en BD")

        return id_nuevo
    except Exception as e:
        print(f"✗ Error al crear usuario: {e}")
        return None


def test_actualizar_usuario(id_usuario):
    """Prueba actualizar un usuario existente"""
    print(f"\n=== PRUEBA 4: Actualizar Usuario ID {id_usuario} ===")
    usuario_service = UsuarioService()

    # Obtener el usuario actual
    usuario = usuario_service.usuario_dao.obtener_por_id(id_usuario)
    if not usuario:
        print(f"✗ Usuario ID {id_usuario} no encontrado")
        return False

    print(f"  Datos actuales:")
    print(f"  - Nombre: {usuario.nombre}")
    print(f"  - Email: {usuario.email}")
    print(f"  - Rol: {usuario.rol}")

    # Actualizar datos
    nuevo_nombre = "Usuario Test Actualizado"
    nuevo_email = usuario.email  # Mantener el mismo email
    nuevo_rol = usuario.rol

    print(f"\n  Actualizando a:")
    print(f"  - Nombre: {nuevo_nombre}")

    usuario_actualizado = usuario_service.actualizar_usuario(
        id_usuario, nuevo_nombre, nuevo_email, nuevo_rol
    )

    if usuario_actualizado:
        print(f"✓ Usuario actualizado exitosamente")

        # Verificar el cambio
        usuario_verificar = usuario_service.usuario_dao.obtener_por_id(
            id_usuario)
        assert usuario_verificar.nombre == nuevo_nombre, "El nombre no se actualizó"
        print(f"✓ Verificación: Cambio aplicado correctamente")
        return True
    else:
        print(f"✗ Error al actualizar usuario")
        return False


def test_crear_vivienda(id_administrador):
    """Prueba crear una nueva vivienda"""
    print(f"\n=== PRUEBA 5: Crear Nueva Vivienda ===")
    vivienda_service = ViviendaService()

    nombre_vivienda = "Casa de Prueba Admin"
    direccion = "Calle Test 123"

    print(f"  Nombre: {nombre_vivienda}")
    print(f"  Dirección: {direccion}")
    print(f"  Administrador ID: {id_administrador}")

    try:
        id_vivienda = vivienda_service.crear_vivienda(
            nombre_vivienda, direccion, id_administrador
        )
        print(f"✓ Vivienda creada con ID: {id_vivienda}")

        # Verificar que se creó
        vivienda = vivienda_service.vivienda_dao.obtener_por_id(id_vivienda)
        assert vivienda is not None, "Vivienda no encontrada después de crearla"
        print(f"✓ Verificación: Vivienda encontrada en BD")

        return id_vivienda
    except Exception as e:
        print(f"✗ Error al crear vivienda: {e}")
        return None


def test_asignar_usuario_a_vivienda(id_usuario, id_vivienda):
    """Prueba asignar un usuario a una vivienda"""
    print(f"\n=== PRUEBA 6: Asignar Usuario a Vivienda ===")
    vivienda_service = ViviendaService()

    print(f"  Usuario ID: {id_usuario}")
    print(f"  Vivienda ID: {id_vivienda}")

    try:
        vivienda_service.asignar_usuario_a_vivienda(id_usuario, id_vivienda)
        print(f"✓ Usuario asignado a vivienda exitosamente")

        # Verificar la asignación
        viviendas_usuario = vivienda_service.obtener_viviendas_por_usuario(
            id_usuario)
        asignado = any(v.id_vivienda == id_vivienda for v in viviendas_usuario)
        assert asignado, "La asignación no se reflejó en la consulta"
        print(f"✓ Verificación: Asignación confirmada")

        return True
    except Exception as e:
        print(f"✗ Error al asignar usuario: {e}")
        return False


def test_crear_dispositivo(id_vivienda):
    """Prueba crear un nuevo dispositivo"""
    print(f"\n=== PRUEBA 7: Crear Nuevo Dispositivo ===")
    dispositivo_service = DispositivoService()

    nombre = "Dispositivo Test Admin"
    tipo = "luz"
    ubicacion = "Sala de Pruebas"

    print(f"  Nombre: {nombre}")
    print(f"  Tipo: {tipo}")
    print(f"  Ubicación: {ubicacion}")
    print(f"  Vivienda ID: {id_vivienda}")

    try:
        id_dispositivo = dispositivo_service.crear_dispositivo_completo(
            nombre, tipo, ubicacion, id_vivienda
        )
        print(f"✓ Dispositivo creado con ID: {id_dispositivo}")

        # Verificar que se creó
        dispositivo = dispositivo_service.obtener_dispositivo_por_id(
            id_dispositivo)
        assert dispositivo is not None, "Dispositivo no encontrado"
        assert dispositivo.estado == 'apagado', "El estado inicial debería ser 'apagado'"
        print(f"✓ Verificación: Dispositivo encontrado con estado 'apagado'")

        return id_dispositivo
    except Exception as e:
        print(f"✗ Error al crear dispositivo: {e}")
        return None


def test_actualizar_dispositivo(id_dispositivo):
    """Prueba actualizar un dispositivo"""
    print(f"\n=== PRUEBA 8: Actualizar Dispositivo ===")
    dispositivo_service = DispositivoService()

    # Obtener dispositivo actual
    dispositivo = dispositivo_service.obtener_dispositivo_por_id(
        id_dispositivo)
    if not dispositivo:
        print(f"✗ Dispositivo ID {id_dispositivo} no encontrado")
        return False

    print(f"  Estado actual: {dispositivo.estado}")

    # Actualizar a encendido
    nuevo_nombre = dispositivo.nombre_dispositivo
    nuevo_tipo = dispositivo.tipo
    nuevo_estado = "encendido"
    nueva_ubicacion = dispositivo.ubicacion

    print(f"  Cambiando estado a: {nuevo_estado}")

    dispositivo_actualizado = dispositivo_service.actualizar_dispositivo_completo(
        id_dispositivo, nuevo_nombre, nuevo_tipo, nuevo_estado, nueva_ubicacion
    )

    if dispositivo_actualizado:
        print(f"✓ Dispositivo actualizado exitosamente")
        assert dispositivo_actualizado.estado == nuevo_estado
        print(f"✓ Verificación: Estado es '{nuevo_estado}'")
        return True
    else:
        print(f"✗ Error al actualizar dispositivo")
        return False


def test_listar_todos_dispositivos():
    """Prueba listar todos los dispositivos del sistema"""
    print(f"\n=== PRUEBA 9: Listar Todos los Dispositivos ===")
    dispositivo_service = DispositivoService()

    dispositivos = dispositivo_service.obtener_todos_los_dispositivos()

    print(f"✓ Sistema tiene {len(dispositivos)} dispositivo(s):")
    for disp in dispositivos[:5]:  # Mostrar solo los primeros 5
        print(f"  - ID: {disp.id_dispositivo} | {disp.nombre_dispositivo}")
        print(
            f"    Tipo: {disp.tipo} | Estado: {disp.estado} | Vivienda: {disp.id_vivienda}")

    if len(dispositivos) > 5:
        print(f"  ... y {len(dispositivos) - 5} más")

    return len(dispositivos) > 0


def test_ver_historial_eventos():
    """Prueba ver el historial completo de eventos del sistema"""
    print(f"\n=== PRUEBA 10: Ver Historial Completo de Eventos ===")
    evento_service = EventoDispositivoService()

    eventos = evento_service.obtener_todos_los_eventos()

    print(f"✓ Sistema tiene {len(eventos)} evento(s) registrado(s)")

    if eventos:
        print(f"\n  Últimos 5 eventos:")
        for evento in eventos[-5:]:
            print(f"  - [{evento.fecha_hora.strftime('%Y-%m-%d %H:%M:%S')}]")
            print(f"    Dispositivo ID: {evento.id_dispositivo}")
            print(f"    Usuario ID: {evento.id_usuario}")
            print(f"    Tipo: {evento.tipo_evento}")
            print(f"    Detalle: {evento.detalle}")

    return len(eventos) > 0


def test_eliminar_dispositivo(id_dispositivo):
    """Prueba eliminar un dispositivo"""
    print(f"\n=== PRUEBA 11: Eliminar Dispositivo ID {id_dispositivo} ===")
    dispositivo_service = DispositivoService()

    # Verificar que existe
    dispositivo = dispositivo_service.obtener_dispositivo_por_id(
        id_dispositivo)
    if not dispositivo:
        print(f"✗ Dispositivo no encontrado")
        return False

    print(f"  Eliminando: {dispositivo.nombre_dispositivo}")

    try:
        dispositivo_service.dispositivo_dao.eliminar(id_dispositivo)
        print(f"✓ Dispositivo eliminado exitosamente")

        # Verificar que ya no existe
        dispositivo_verificar = dispositivo_service.obtener_dispositivo_por_id(
            id_dispositivo)
        assert dispositivo_verificar is None, "El dispositivo aún existe después de eliminarlo"
        print(f"✓ Verificación: Dispositivo eliminado de BD")

        return True
    except Exception as e:
        print(f"✗ Error al eliminar dispositivo: {e}")
        return False


def test_eliminar_usuario(id_usuario):
    """Prueba eliminar un usuario"""
    print(f"\n=== PRUEBA 12: Eliminar Usuario ID {id_usuario} ===")
    usuario_service = UsuarioService()
    vivienda_service = ViviendaService()

    # Verificar que existe
    usuario = usuario_service.usuario_dao.obtener_por_id(id_usuario)
    if not usuario:
        print(f"✗ Usuario no encontrado")
        return False

    print(f"  Eliminando: {usuario.nombre}")

    try:
        # Primero desasignar de todas las viviendas
        print(f"  Desasignando usuario de viviendas...")
        vivienda_service.vivienda_dao.desasignar_todas_viviendas_usuario(
            id_usuario)
        print(f"  ✓ Usuario desasignado de viviendas")

        # Ahora eliminar el usuario
        usuario_service.eliminar_usuario(id_usuario)
        print(f"✓ Usuario eliminado exitosamente")

        # Verificar que ya no existe
        usuario_verificar = usuario_service.usuario_dao.obtener_por_id(
            id_usuario)
        assert usuario_verificar is None, "El usuario aún existe después de eliminarlo"
        print(f"✓ Verificación: Usuario eliminado de BD")

        return True
    except Exception as e:
        print(f"✗ Error al eliminar usuario: {e}")
        print(f"  Nota: El usuario tiene dependencias que impiden su eliminación")
        return False


def ejecutar_todas_las_pruebas():
    """Ejecuta todas las pruebas del administrador"""
    print("\n" + "="*70)
    print("  INICIANDO PRUEBAS DEL SISTEMA SMARTHOME - ADMINISTRADOR")
    print("="*70)

    # Variables para almacenar IDs creados
    id_usuario_test = None
    id_vivienda_test = None
    id_dispositivo_test = None

    try:
        # Prueba 1: Login
        admin = test_login_administrador()
        if not admin:
            print(
                "\n✗ ERROR: No se pudo iniciar sesión como administrador. Abortando pruebas.")
            return False

        # Prueba 2: Listar usuarios
        test_listar_todos_usuarios()

        # Prueba 3: Crear usuario
        id_usuario_test = test_crear_usuario()
        if not id_usuario_test:
            print("\n⚠ ADVERTENCIA: No se pudo crear usuario de prueba")

        # Prueba 4: Actualizar usuario
        if id_usuario_test:
            test_actualizar_usuario(id_usuario_test)

        # Prueba 5: Crear vivienda
        id_vivienda_test = test_crear_vivienda(admin.id_usuario)
        if not id_vivienda_test:
            print("\n⚠ ADVERTENCIA: No se pudo crear vivienda de prueba")

        # Prueba 6: Asignar usuario a vivienda
        if id_usuario_test and id_vivienda_test:
            test_asignar_usuario_a_vivienda(id_usuario_test, id_vivienda_test)

        # Prueba 7: Crear dispositivo
        if id_vivienda_test:
            id_dispositivo_test = test_crear_dispositivo(id_vivienda_test)

        # Prueba 8: Actualizar dispositivo
        if id_dispositivo_test:
            test_actualizar_dispositivo(id_dispositivo_test)

        # Prueba 9: Listar todos los dispositivos
        test_listar_todos_dispositivos()

        # Prueba 10: Ver historial de eventos
        test_ver_historial_eventos()

        # Prueba 11: Eliminar dispositivo de prueba
        if id_dispositivo_test:
            test_eliminar_dispositivo(id_dispositivo_test)

        # Prueba 12: Eliminar usuario de prueba
        if id_usuario_test:
            test_eliminar_usuario(id_usuario_test)

        print("\n" + "="*70)
        print("  ✓ TODAS LAS PRUEBAS DE ADMINISTRADOR COMPLETADAS")
        print("="*70 + "\n")

        print("NOTA: La vivienda de prueba NO fue eliminada para no afectar")
        print("      la integridad referencial si tiene otros datos asociados.")

        return True

    except Exception as e:
        print(f"\n✗ ERROR durante las pruebas: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    ejecutar_todas_las_pruebas()
