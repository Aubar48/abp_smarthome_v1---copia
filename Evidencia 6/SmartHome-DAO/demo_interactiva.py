"""
Script de Demostración Interactiva del Sistema SmartHome
Simula el uso completo de un usuario normal
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


def demo_completa():
    """Ejecuta una demostración completa del sistema"""

    separador("DEMOSTRACIÓN DEL SISTEMA SMARTHOME - USUARIO NORMAL")

    print("Este script demuestra todas las funcionalidades disponibles")
    print("para un usuario normal en el Sistema SmartHome.")
    pausa()

    # === 1. LOGIN ===
    separador("1. INICIO DE SESIÓN")
    print("Ingresando al sistema con credenciales de usuario normal...")
    print("Email: ana@mail.com")
    print("Contraseña: user123")
    pausa()

    usuario_service = UsuarioService()
    usuario = usuario_service.login("ana@mail.com", "user123")

    if not usuario:
        print("❌ Error: No se pudo iniciar sesión")
        return

    print(f"✅ ¡Bienvenido/a, {usuario.nombre}!")
    print(f"   Rol: {usuario.rol}")
    pausa()

    # === 2. VISUALIZAR VIVIENDAS ===
    separador("2. VIVIENDAS ASIGNADAS AL USUARIO")
    print(f"Consultando viviendas asignadas a {usuario.nombre}...")
    pausa()

    vivienda_service = ViviendaService()
    viviendas = vivienda_service.obtener_viviendas_por_usuario(
        usuario.id_usuario)

    print(f"📍 Tienes {len(viviendas)} vivienda(s) asignada(s):\n")
    for i, vivienda in enumerate(viviendas, 1):
        print(f"   {i}. 🏠 {vivienda.nombre_vivienda}")
        print(f"      📍 Dirección: {vivienda.direccion}")
        print(f"      🆔 ID: {vivienda.id_vivienda}\n")

    if not viviendas:
        print("❌ No tienes viviendas asignadas")
        return

    vivienda_actual = viviendas[0]
    pausa()

    # === 3. VISUALIZAR DISPOSITIVOS ===
    separador(f"3. DISPOSITIVOS EN '{vivienda_actual.nombre_vivienda}'")
    print("Consultando dispositivos instalados...")
    pausa()

    dispositivos = vivienda_service.obtener_dispositivos_por_vivienda(
        vivienda_actual.id_vivienda)

    print(f"🔌 Dispositivos encontrados: {len(dispositivos)}\n")

    for i, disp in enumerate(dispositivos, 1):
        icono = "💡" if disp.tipo == "luz" else "📹" if disp.tipo == "camara" else "🌡️"
        estado_emoji = "🟢" if disp.estado == "encendido" else "🔴"

        print(f"   {i}. {icono} {disp.nombre_dispositivo}")
        print(f"      Tipo: {disp.tipo}")
        print(f"      Estado: {estado_emoji} {disp.estado.upper()}")
        print(f"      Ubicación: {disp.ubicacion}")
        print(f"      ID: {disp.id_dispositivo}\n")

    if not dispositivos:
        print("❌ No hay dispositivos en esta vivienda")
        return

    pausa()

    # === 4. CONTROLAR DISPOSITIVOS ===
    separador("4. CONTROL DE DISPOSITIVOS")

    dispositivo_service = DispositivoService()

    # Controlar cada dispositivo
    for disp in dispositivos[:2]:  # Controlar los primeros 2 dispositivos
        print(f"\n🎮 Controlando: {disp.nombre_dispositivo}")
        print(f"   Estado actual: {disp.estado}")

        nuevo_estado = 'apagado' if disp.estado == 'encendido' else 'encendido'
        print(f"   ⚡ Cambiando a: {nuevo_estado}...")
        pausa()

        exito = dispositivo_service.cambiar_estado_dispositivo(
            disp.id_dispositivo,
            nuevo_estado,
            usuario.id_usuario
        )

        if exito:
            estado_emoji = "🟢" if nuevo_estado == "encendido" else "🔴"
            print(f"   ✅ {estado_emoji} Dispositivo {nuevo_estado}")
            print(f"   📝 Evento registrado en el historial")
        else:
            print(f"   ❌ Error al cambiar estado")

        pausa()

    # === 5. HISTORIAL DE EVENTOS ===
    separador("5. HISTORIAL DE EVENTOS")

    evento_service = EventoDispositivoService()

    print("📜 Consultando eventos recientes de los dispositivos...\n")
    pausa()

    for disp in dispositivos[:2]:
        eventos = evento_service.obtener_eventos_por_dispositivo(
            disp.id_dispositivo)

        print(f"📱 {disp.nombre_dispositivo}")
        print(f"   Total de eventos: {len(eventos)}")

        if eventos:
            print(f"   Últimos 2 eventos:")
            for evento in eventos[-2:]:
                fecha_str = evento.fecha_hora.strftime('%d/%m/%Y %H:%M:%S')
                tipo_emoji = "🟢" if evento.tipo_evento == "encendido" else "🔴"
                print(f"   • {tipo_emoji} [{fecha_str}] {evento.tipo_evento}")
                print(f"     {evento.detalle}")
        print()
        pausa()

    # === 6. RESUMEN DEL SISTEMA ===
    separador("6. RESUMEN DEL SISTEMA")

    todos_eventos = evento_service.obtener_todos_los_eventos()

    print("📊 Estadísticas del Sistema:\n")
    print(f"   👤 Usuario activo: {usuario.nombre}")
    print(f"   🏠 Viviendas: {len(viviendas)}")
    print(f"   🔌 Dispositivos: {len(dispositivos)}")
    print(f"   📝 Total de eventos: {len(todos_eventos)}")

    # Contar dispositivos por estado
    encendidos = sum(1 for d in dispositivos if d.estado == 'encendido')
    apagados = len(dispositivos) - encendidos

    print(f"\n   Estado de dispositivos:")
    print(f"   🟢 Encendidos: {encendidos}")
    print(f"   🔴 Apagados: {apagados}")

    pausa()

    # === FINALIZACIÓN ===
    separador("DEMOSTRACIÓN COMPLETADA")
    print("✅ Todas las funcionalidades del usuario normal fueron demostradas:")
    print("   • ✅ Inicio de sesión")
    print("   • ✅ Visualización de viviendas")
    print("   • ✅ Listado de dispositivos")
    print("   • ✅ Control de dispositivos")
    print("   • ✅ Registro de eventos")
    print("   • ✅ Consulta de historial")
    print("\n🎉 ¡El sistema funciona correctamente!")
    separador()


if __name__ == "__main__":
    try:
        demo_completa()
    except Exception as e:
        print(f"\n❌ Error durante la demostración: {e}")
        import traceback
        traceback.print_exc()
