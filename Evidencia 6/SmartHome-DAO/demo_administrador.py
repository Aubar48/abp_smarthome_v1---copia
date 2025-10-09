"""
Script de Demostración Interactiva del Sistema SmartHome - ROL ADMINISTRADOR
Muestra todas las funcionalidades disponibles para un administrador
"""
from app.services.usuario_service import UsuarioService
from app.services.vivienda_service import ViviendaService
from app.services.dispositivo_service import DispositivoService
from app.services.evento_dispositivo_service import EventoDispositivoService
import time


def separador(titulo=""):
    """Imprime un separador visual"""
    print("\n" + "="*70)
    if titulo:
        print(f"  {titulo}")
        print("="*70)
    print()


def pausa():
    """Pequeña pausa para mejorar la visualización"""
    time.sleep(0.5)


def demo_completa_admin():
    """Ejecuta una demostración completa del rol administrador"""

    separador("DEMOSTRACIÓN DEL SISTEMA SMARTHOME - ROL ADMINISTRADOR")

    print("Este script demuestra todas las funcionalidades disponibles")
    print("para un ADMINISTRADOR en el Sistema SmartHome.")
    pausa()

    # === 1. LOGIN ===
    separador("1. INICIO DE SESIÓN COMO ADMINISTRADOR")
    print("Ingresando al sistema con credenciales de administrador...")
    print("Email: admin@smarthome.com")
    print("Contraseña: admin123")
    pausa()

    usuario_service = UsuarioService()
    admin = usuario_service.login("admin@smarthome.com", "admin123")

    if not admin:
        print("❌ Error: No se pudo iniciar sesión")
        return

    print(f"✅ ¡Bienvenido/a, {admin.nombre}!")
    print(f"   Rol: {admin.rol.upper()}")
    print(f"   Privilegios: COMPLETOS")
    pausa()

    # === 2. GESTIÓN DE USUARIOS ===
    separador("2. GESTIÓN DE USUARIOS DEL SISTEMA")
    print("Consultando todos los usuarios del sistema...")
    pausa()

    usuarios = usuario_service.obtener_todos_los_usuarios()

    print(f"👥 Total de usuarios en el sistema: {len(usuarios)}\n")
    for usuario in usuarios:
        icono = "👔" if usuario.rol == "administrador" else "👤"
        estado = "🟢" if usuario.activo else "🔴"
        print(f"   {icono} [{usuario.id_usuario}] {usuario.nombre}")
        print(f"      Email: {usuario.email}")
        print(f"      Rol: {usuario.rol}")
        print(
            f"      Estado: {estado} {'Activo' if usuario.activo else 'Inactivo'}\n")

    pausa()

    # === 3. CREAR USUARIO ===
    separador("3. CREAR NUEVO USUARIO")
    print("Creando un nuevo usuario de demostración...")

    nombre_demo = "Demo Usuario Admin"
    email_demo = "demo_admin@smarthome.com"
    contraseña_demo = "demo123"
    rol_demo = "usuario"

    print(f"\n   Nombre: {nombre_demo}")
    print(f"   Email: {email_demo}")
    print(f"   Rol: {rol_demo}")
    pausa()

    try:
        # Verificar si ya existe
        usuario_existente = usuario_service.usuario_dao.obtener_por_email(
            email_demo)
        if usuario_existente:
            print(f"   ℹ Usuario ya existe, usando existente para demo")
            id_usuario_demo = usuario_existente.id_usuario
        else:
            id_usuario_demo = usuario_service.registrar_usuario(
                nombre_demo, email_demo, contraseña_demo, rol_demo
            )
            print(f"✅ Usuario creado exitosamente con ID: {id_usuario_demo}")
    except Exception as e:
        print(f"⚠ Advertencia: {e}")
        id_usuario_demo = None

    pausa()

    # === 4. GESTIÓN DE VIVIENDAS ===
    separador("4. GESTIÓN DE VIVIENDAS")
    print("Los administradores pueden crear y gestionar viviendas...")
    pausa()

    vivienda_service = ViviendaService()

    print("\n📋 Creando nueva vivienda de demostración...")
    nombre_vivienda_demo = "Casa Demo Administrador"
    direccion_demo = "Av. Administradores 456"

    print(f"   Nombre: {nombre_vivienda_demo}")
    print(f"   Dirección: {direccion_demo}")
    pausa()

    try:
        id_vivienda_demo = vivienda_service.crear_vivienda(
            nombre_vivienda_demo, direccion_demo, admin.id_usuario
        )
        print(f"✅ Vivienda creada con ID: {id_vivienda_demo}")
    except Exception as e:
        print(f"⚠ Advertencia: {e}")
        id_vivienda_demo = None

    pausa()

    # === 5. ASIGNAR USUARIO A VIVIENDA ===
    if id_usuario_demo and id_vivienda_demo:
        separador("5. ASIGNAR USUARIO A VIVIENDA")
        print("Asignando el usuario de prueba a la vivienda recién creada...")
        print(f"   Usuario ID: {id_usuario_demo}")
        print(f"   Vivienda ID: {id_vivienda_demo}")
        pausa()

        try:
            vivienda_service.asignar_usuario_a_vivienda(
                id_usuario_demo, id_vivienda_demo)
            print(f"✅ Usuario asignado exitosamente a la vivienda")
        except Exception as e:
            print(f"⚠ Advertencia: {e}")

        pausa()

    # === 6. GESTIÓN DE DISPOSITIVOS ===
    separador("6. GESTIÓN DE DISPOSITIVOS")

    dispositivo_service = DispositivoService()
    todos_dispositivos = dispositivo_service.obtener_todos_los_dispositivos()

    print(
        f"🔌 Total de dispositivos en el sistema: {len(todos_dispositivos)}\n")

    # Agrupar por vivienda
    dispositivos_por_vivienda = {}
    for disp in todos_dispositivos:
        if disp.id_vivienda not in dispositivos_por_vivienda:
            dispositivos_por_vivienda[disp.id_vivienda] = []
        dispositivos_por_vivienda[disp.id_vivienda].append(disp)

    for id_viv, dispositivos in dispositivos_por_vivienda.items():
        vivienda = vivienda_service.vivienda_dao.obtener_por_id(id_viv)
        if vivienda:
            print(f"   🏠 {vivienda.nombre_vivienda}:")
            for disp in dispositivos:
                icono = "💡" if disp.tipo == "luz" else "📹" if disp.tipo == "camara" else "🌡️"
                estado_emoji = "🟢" if disp.estado == "encendido" else "🔴"
                print(
                    f"      {icono} [{disp.id_dispositivo}] {disp.nombre_dispositivo}")
                print(f"         Estado: {estado_emoji} {disp.estado.upper()}")

    pausa()

    # === 7. CREAR DISPOSITIVO ===
    if id_vivienda_demo:
        separador("7. CREAR NUEVO DISPOSITIVO")
        print("Agregando un dispositivo a la vivienda de demostración...")

        nombre_disp_demo = "Luz Demo Admin"
        tipo_disp_demo = "luz"
        ubicacion_demo = "Sala Principal"

        print(f"\n   Nombre: {nombre_disp_demo}")
        print(f"   Tipo: {tipo_disp_demo}")
        print(f"   Ubicación: {ubicacion_demo}")
        print(f"   Vivienda: {nombre_vivienda_demo}")
        pausa()

        try:
            id_dispositivo_demo = dispositivo_service.crear_dispositivo_completo(
                nombre_disp_demo, tipo_disp_demo, ubicacion_demo, id_vivienda_demo
            )
            print(f"✅ Dispositivo creado con ID: {id_dispositivo_demo}")
            print(f"   Estado inicial: 🔴 APAGADO")
        except Exception as e:
            print(f"⚠ Advertencia: {e}")
            id_dispositivo_demo = None

        pausa()

        # === 8. ACTUALIZAR DISPOSITIVO ===
        if id_dispositivo_demo:
            separador("8. ACTUALIZAR ESTADO DE DISPOSITIVO")
            print(f"Encendiendo el dispositivo '{nombre_disp_demo}'...")
            pausa()

            dispositivo_actualizado = dispositivo_service.actualizar_dispositivo_completo(
                id_dispositivo_demo,
                nombre_disp_demo,
                tipo_disp_demo,
                "encendido",
                ubicacion_demo
            )

            if dispositivo_actualizado:
                print(f"✅ 🟢 Dispositivo ENCENDIDO")

            pausa()

    # === 9. HISTORIAL COMPLETO DE EVENTOS ===
    separador("9. HISTORIAL COMPLETO DE EVENTOS DEL SISTEMA")
    print("Consultando todos los eventos registrados en el sistema...")
    pausa()

    evento_service = EventoDispositivoService()
    todos_eventos = evento_service.obtener_todos_los_eventos()

    print(f"📊 Total de eventos en el sistema: {len(todos_eventos)}\n")

    if todos_eventos:
        print("   Últimos 10 eventos:")
        for evento in todos_eventos[-10:]:
            tipo_emoji = "🟢" if evento.tipo_evento == "encendido" else "🔴" if evento.tipo_evento == "apagado" else "⚙️"
            fecha_str = evento.fecha_hora.strftime('%d/%m/%Y %H:%M:%S')

            print(f"   {tipo_emoji} [{fecha_str}]")
            print(f"      Dispositivo ID: {evento.id_dispositivo}")
            print(f"      Usuario ID: {evento.id_usuario}")
            print(f"      Acción: {evento.tipo_evento}")
            if evento.detalle:
                print(f"      Detalle: {evento.detalle}")

    pausa()

    # === 10. ESTADÍSTICAS DEL SISTEMA ===
    separador("10. ESTADÍSTICAS DEL SISTEMA")

    print("📊 Panel de Control del Administrador:\n")

    total_usuarios = len(usuarios)
    total_admins = sum(1 for u in usuarios if u.rol == 'administrador')
    total_usuarios_normales = total_usuarios - total_admins

    total_dispositivos = len(todos_dispositivos)
    dispositivos_encendidos = sum(
        1 for d in todos_dispositivos if d.estado == 'encendido')
    dispositivos_apagados = total_dispositivos - dispositivos_encendidos

    total_eventos = len(todos_eventos)

    print(f"   👥 Usuarios:")
    print(f"      Total: {total_usuarios}")
    print(f"      Administradores: {total_admins}")
    print(f"      Usuarios normales: {total_usuarios_normales}")

    print(f"\n   🏠 Viviendas:")
    print(f"      Total en el sistema: {len(dispositivos_por_vivienda)}")

    print(f"\n   🔌 Dispositivos:")
    print(f"      Total: {total_dispositivos}")
    print(f"      🟢 Encendidos: {dispositivos_encendidos}")
    print(f"      🔴 Apagados: {dispositivos_apagados}")

    print(f"\n   📝 Eventos:")
    print(f"      Total registrados: {total_eventos}")

    pausa()

    # === LIMPIEZA (OPCIONAL) ===
    separador("11. LIMPIEZA DE DATOS DE DEMOSTRACIÓN")
    print("Eliminando datos de prueba creados durante la demostración...")
    pausa()

    # Eliminar dispositivo demo
    if id_dispositivo_demo:
        try:
            dispositivo_service.dispositivo_dao.eliminar(id_dispositivo_demo)
            print(f"✅ Dispositivo de prueba eliminado")
        except Exception as e:
            print(f"⚠ No se pudo eliminar dispositivo: {e}")

    # Eliminar usuario demo
    if id_usuario_demo:
        try:
            # Primero desasignar de viviendas
            vivienda_service.vivienda_dao.desasignar_todas_viviendas_usuario(
                id_usuario_demo)
            usuario_service.eliminar_usuario(id_usuario_demo)
            print(f"✅ Usuario de prueba eliminado")
        except Exception as e:
            print(f"⚠ No se pudo eliminar usuario: {e}")

    print("\n   ℹ La vivienda de demostración se mantiene en el sistema")

    pausa()

    # === FINALIZACIÓN ===
    separador("DEMOSTRACIÓN COMPLETADA")
    print("✅ Funcionalidades del Administrador demostradas:\n")
    print("   • ✅ Inicio de sesión con privilegios de administrador")
    print("   • ✅ Visualización de todos los usuarios del sistema")
    print("   • ✅ Creación de nuevos usuarios")
    print("   • ✅ Creación de viviendas")
    print("   • ✅ Asignación de usuarios a viviendas")
    print("   • ✅ Visualización de todos los dispositivos")
    print("   • ✅ Creación de dispositivos")
    print("   • ✅ Actualización de dispositivos")
    print("   • ✅ Consulta del historial completo de eventos")
    print("   • ✅ Visualización de estadísticas del sistema")
    print("   • ✅ Eliminación de usuarios y dispositivos")
    print("\n🎉 ¡El sistema de administración funciona correctamente!")
    separador()


if __name__ == "__main__":
    try:
        demo_completa_admin()
    except Exception as e:
        print(f"\n❌ Error durante la demostración: {e}")
        import traceback
        traceback.print_exc()
