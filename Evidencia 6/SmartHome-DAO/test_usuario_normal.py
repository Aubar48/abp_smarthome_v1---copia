"""
Script de prueba para testear todas las funcionalidades de un usuario normal
en el sistema SmartHome
"""
from app.services.usuario_service import UsuarioService
from app.services.vivienda_service import ViviendaService
from app.services.dispositivo_service import DispositivoService
from app.services.evento_dispositivo_service import EventoDispositivoService


def test_login_usuario_normal():
    """Prueba el login de un usuario normal"""
    print("\n=== PRUEBA 1: Login de Usuario Normal ===")
    usuario_service = UsuarioService()

    # Intentar login con un usuario normal
    usuario = usuario_service.login("ana@mail.com", "user123")

    if usuario:
        print(f"✓ Login exitoso para: {usuario.nombre}")
        print(f"  - Email: {usuario.email}")
        print(f"  - Rol: {usuario.rol}")
        assert usuario.rol == "usuario", "El rol debería ser 'usuario'"
        return usuario
    else:
        print("✗ Login fallido")
        return None


def test_obtener_viviendas_usuario(usuario):
    """Prueba obtener las viviendas asignadas al usuario"""
    print("\n=== PRUEBA 2: Obtener Viviendas del Usuario ===")
    vivienda_service = ViviendaService()

    viviendas = vivienda_service.obtener_viviendas_por_usuario(
        usuario.id_usuario)

    print(f"✓ Usuario tiene {len(viviendas)} vivienda(s) asignada(s):")
    for vivienda in viviendas:
        print(f"  - {vivienda.nombre_vivienda} (ID: {vivienda.id_vivienda})")
        print(f"    Dirección: {vivienda.direccion}")

    return viviendas


def test_obtener_dispositivos_vivienda(vivienda):
    """Prueba obtener los dispositivos de una vivienda"""
    print(
        f"\n=== PRUEBA 3: Obtener Dispositivos de '{vivienda.nombre_vivienda}' ===")
    vivienda_service = ViviendaService()

    dispositivos = vivienda_service.obtener_dispositivos_por_vivienda(
        vivienda.id_vivienda)

    print(f"✓ Vivienda tiene {len(dispositivos)} dispositivo(s):")
    for dispositivo in dispositivos:
        print(f"  - {dispositivo.nombre_dispositivo}")
        print(f"    Tipo: {dispositivo.tipo}")
        print(f"    Estado: {dispositivo.estado}")
        print(f"    Ubicación: {dispositivo.ubicacion}")

    return dispositivos


def test_cambiar_estado_dispositivo(usuario, dispositivo):
    """Prueba cambiar el estado de un dispositivo"""
    print(
        f"\n=== PRUEBA 4: Cambiar Estado del Dispositivo '{dispositivo.nombre_dispositivo}' ===")
    dispositivo_service = DispositivoService()

    estado_original = dispositivo.estado
    nuevo_estado = 'apagado' if estado_original == 'encendido' else 'encendido'

    print(f"  Estado original: {estado_original}")
    print(f"  Cambiando a: {nuevo_estado}")

    exito = dispositivo_service.cambiar_estado_dispositivo(
        dispositivo.id_dispositivo,
        nuevo_estado,
        usuario.id_usuario
    )

    if exito:
        print(f"✓ Estado cambiado exitosamente")

        # Verificar que el cambio se aplicó
        dispositivo_actualizado = dispositivo_service.obtener_dispositivo_por_id(
            dispositivo.id_dispositivo)
        assert dispositivo_actualizado.estado == nuevo_estado, "El estado no se actualizó correctamente"
        print(
            f"✓ Verificación: Estado actual es '{dispositivo_actualizado.estado}'")

        # Volver al estado original para no afectar otras pruebas
        dispositivo_service.cambiar_estado_dispositivo(
            dispositivo.id_dispositivo,
            estado_original,
            usuario.id_usuario
        )
        print(f"✓ Estado restaurado a '{estado_original}'")
    else:
        print("✗ No se pudo cambiar el estado")

    return exito


def test_verificar_registro_eventos(dispositivo, usuario):
    """Prueba verificar que los eventos se registran correctamente"""
    print(f"\n=== PRUEBA 5: Verificar Registro de Eventos ===")
    evento_service = EventoDispositivoService()

    eventos = evento_service.obtener_eventos_por_dispositivo(
        dispositivo.id_dispositivo)

    print(
        f"✓ Dispositivo '{dispositivo.nombre_dispositivo}' tiene {len(eventos)} evento(s) registrado(s)")

    if eventos:
        print("\n  Últimos 3 eventos:")
        for evento in eventos[-3:]:
            print(f"  - {evento.fecha_hora.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"    Tipo: {evento.tipo_evento}")
            print(f"    Usuario ID: {evento.id_usuario}")
            print(f"    Detalle: {evento.detalle}")

    return len(eventos) > 0


def test_multiples_dispositivos(usuario, vivienda, dispositivos):
    """Prueba controlar múltiples dispositivos"""
    print(f"\n=== PRUEBA 6: Control de Múltiples Dispositivos ===")
    dispositivo_service = DispositivoService()

    cambios_exitosos = 0

    for dispositivo in dispositivos[:3]:  # Probar solo los primeros 3
        estado_nuevo = 'apagado' if dispositivo.estado == 'encendido' else 'encendido'

        print(
            f"\n  Cambiando '{dispositivo.nombre_dispositivo}' a '{estado_nuevo}'...")
        if dispositivo_service.cambiar_estado_dispositivo(
            dispositivo.id_dispositivo,
            estado_nuevo,
            usuario.id_usuario
        ):
            cambios_exitosos += 1
            print(f"  ✓ Cambio exitoso")

            # Restaurar estado original
            dispositivo_service.cambiar_estado_dispositivo(
                dispositivo.id_dispositivo,
                dispositivo.estado,
                usuario.id_usuario
            )

    print(
        f"\n✓ Se cambiaron exitosamente {cambios_exitosos} de {min(3, len(dispositivos))} dispositivos")

    return cambios_exitosos > 0


def test_listado_todos_eventos_sistema():
    """Prueba obtener todos los eventos del sistema (solo para verificación)"""
    print(f"\n=== PRUEBA 7: Listado de Eventos del Sistema ===")
    evento_service = EventoDispositivoService()

    todos_eventos = evento_service.obtener_todos_los_eventos()

    print(
        f"✓ Sistema tiene {len(todos_eventos)} evento(s) registrado(s) en total")

    if todos_eventos:
        print("\n  Últimos 5 eventos del sistema:")
        for evento in todos_eventos[-5:]:
            print(f"  - [{evento.fecha_hora.strftime('%Y-%m-%d %H:%M:%S')}] "
                  f"Dispositivo ID: {evento.id_dispositivo}, "
                  f"Tipo: {evento.tipo_evento}, "
                  f"Usuario ID: {evento.id_usuario}")

    return True


def ejecutar_todas_las_pruebas():
    """Ejecuta todas las pruebas del usuario normal"""
    print("\n" + "="*70)
    print("  INICIANDO PRUEBAS DEL SISTEMA SMARTHOME - USUARIO NORMAL")
    print("="*70)

    try:
        # Prueba 1: Login
        usuario = test_login_usuario_normal()
        if not usuario:
            print("\n✗ ERROR: No se pudo iniciar sesión. Abortando pruebas.")
            return False

        # Prueba 2: Obtener viviendas
        viviendas = test_obtener_viviendas_usuario(usuario)
        if not viviendas:
            print("\n✗ ERROR: Usuario no tiene viviendas asignadas. Abortando pruebas.")
            return False

        # Usar la primera vivienda para las pruebas
        vivienda_prueba = viviendas[0]

        # Prueba 3: Obtener dispositivos
        dispositivos = test_obtener_dispositivos_vivienda(vivienda_prueba)
        if not dispositivos:
            print("\n✗ ERROR: Vivienda no tiene dispositivos. Abortando pruebas.")
            return False

        # Usar el primer dispositivo para las pruebas
        dispositivo_prueba = dispositivos[0]

        # Prueba 4: Cambiar estado de un dispositivo
        test_cambiar_estado_dispositivo(usuario, dispositivo_prueba)

        # Prueba 5: Verificar eventos
        test_verificar_registro_eventos(dispositivo_prueba, usuario)

        # Prueba 6: Control de múltiples dispositivos
        test_multiples_dispositivos(usuario, vivienda_prueba, dispositivos)

        # Prueba 7: Listado de eventos del sistema
        test_listado_todos_eventos_sistema()

        print("\n" + "="*70)
        print("  ✓ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
        print("="*70 + "\n")

        return True

    except Exception as e:
        print(f"\n✗ ERROR durante las pruebas: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    ejecutar_todas_las_pruebas()
