from dispositivos import (
    listar_dispositivos,
    agregar_dispositivo,
    buscar_dispositivo,
    editar_dispositivo,
    eliminar_dispositivo,
)
from automatizacion import (
    listar_automatizaciones,
    activar_automatizacion,
    consultar_automatizaciones_activas,
)
from usuarios import registrar, iniciar_sesion, ver_datos_personales, agregar_usuario

def menu_inicio():
    while True:
        print("\n--- Inicio ---")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Selecciona una opción (1-2-3): ")

        if opcion == "1":
            email = input("Email: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = input("DNI: ")
            contraseña = input("Contraseña: ")
            resultado = registrar(email, nombre, apellido, dni, contraseña)
            print(resultado)

        elif opcion == "2":
            email = input("Email: ")
            contraseña = input("Contraseña: ")
            resultado, rol = iniciar_sesion(email, contraseña)
            print(resultado)
            if rol:
                menu_principal(email, rol)

        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida.")                        
def menu_principal(email, rol):
    while True:
        print("\n--- Menú Principal ---")
        print("1. Listar dispositivos")
        print("2. Buscar dispositivo")
        print("3. Agregar dispositivo")
        print("4. Ver automatizaciones")
        print("5. Activar automatización")
        print("6. Ver datos personales")
        print("7. Consultar automatizaciones activas")

        if rol == "admin":
            print("8. Editar dispositivo")
            print("9. Eliminar dispositivo")  
            print("10. Agregar usuario")
            print("11. Ver todos los usuarios")
            print("12. Eliminar usuario")
        print("0. Cerrar sesión")

        opcion = input("Selecciona una opción:")

        if opcion == "1":
            dispositivos = listar_dispositivos()
            if not dispositivos:
                print("No hay dispositivos registrados.")
            else:
                print("\nDISPOSITIVOS REGISTRADOS")
                print("-" * 50)
                for d in dispositivos:
                    print(f"   ID: {d['id_dispositivo']}")
                    print(f"   Nombre : {d['nombre']}")
                    print(f"   Tipo   : {d['tipo']}")
                    print(f"   Estado : {d['estado']}")
                    print("-" * 50)

        elif opcion == "2":
            nombre = input("Nombre del dispositivo a buscar:")
            dispositivo = buscar_dispositivo(nombre)
            if dispositivo:
                print(dispositivo)
            else:
                print("No se encontró el dispositivo.")

        elif opcion == "3":
            nombre = input("Nombre del dispositivo:")
            tipo = input("Tipo de dispositivo:")
            nuevo_dispositivo = agregar_dispositivo(nombre, tipo)
            print(nuevo_dispositivo)

        elif opcion == "8":
            nombre_original = input("Nombre del dispositivo que quieres editar:")
            print("Dejar vacíos los campos que no quieras editar.")
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_tipo = input("Nuevo tipo: ")
            nuevo_estado = input("Nuevo estado (encendido/apagado): ")
            dispositivo_actualizado = editar_dispositivo(
                nombre_original, nuevo_nombre, nuevo_tipo, nuevo_estado
            )
            print(dispositivo_actualizado)

        elif opcion == "9":
            nombre = input("Nombre del dispositivo a eliminar: ")
            dispositivo_eliminado = eliminar_dispositivo(nombre)
            if dispositivo_eliminado:
                print(f"Dispositivo eliminado: {dispositivo_eliminado}")
            else:
                print("No se encontró el dispositivo.")

        elif opcion == "4":
            automatizaciones = listar_automatizaciones()
            if not automatizaciones:
                print("No existen automatizaciones.")
            else:
                print("\nAutomatizaciones registradas")
                for a in automatizaciones:
                    print(f"Automatización (ID {a['id_auto']}) - Modo: {a['accion']}")

        elif opcion == "5":
            modo_automatizacion = input("accion a activar (Ej:sonar ):")
            dispositivos_activados = activar_automatizacion(modo_automatizacion)
            if dispositivos_activados:
                for id_ in dispositivos_activados:
                    print(f"✅ Dispositivo activado ID: {id_}")
            else:
                print("⚠️ No se activó ningún dispositivo.")

        elif opcion == "6":
            print(ver_datos_personales(email))

        elif opcion == "7":
            resultado = consultar_automatizaciones_activas()
            print(resultado)

        elif opcion == "10" and rol == "admin":
            email = input("Email del nuevo usuario: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = input("DNI: ")
            contraseña = input("Contraseña: ")
            nuevo_usuario = agregar_usuario(email, nombre, apellido, dni, contraseña)
            print(nuevo_usuario)


        elif opcion == "11" and rol == "admin":
            from usuarios import usuarios  
            print("\n👥 Usuarios registrados:")
            for email, datos in usuarios.items():
                print(f"- {email} ({datos['rol']})")

        elif opcion == "12" and rol == "admin":
            from usuarios import usuarios
            correo_a_eliminar = input("Email del usuario a eliminar: ")
            if correo_a_eliminar in usuarios:
                del usuarios[correo_a_eliminar]
                print(f"✅ Usuario eliminado: {correo_a_eliminar}")
            else:
                print("❌ Usuario no encontrado.")

        elif opcion == "0":
            print("Sesión cerrada.")
            break

        else:
            print("Opción no válida.")
            

if __name__ == "__main__":
    menu_inicio()