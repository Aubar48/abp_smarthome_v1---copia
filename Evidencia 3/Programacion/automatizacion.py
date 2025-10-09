from dispositivos import listar_dispositivos

automatizaciones = [{
    "id_auto": 1,
    "accion": "moverse a modo noche",
    "hora": "19:00",  #No esta en el modelo relacional de base de datos pero la agregamos porque nos parecio importante como dato
    "condicion": True        
}, {
    "id_auto": 2,
    "accion": "sonar interminentemente",
    "hora": "10:00",  #No esta en el modelo relacional de base de datos pero la agregamos porque nos parecio importante como dato
    "condicion": True
}]

def listar_automatizaciones():
    return automatizaciones

def activar_automatizacion(modo_automatizacion):
    dispositivos_modificados = []
    for a in automatizaciones:
        if a["accion"].lower() == modo_automatizacion.lower():
            dispositivos = listar_dispositivos()
            for d in dispositivos:
                if d["estado"].lower() == "apagado" and d["tipo"].lower() == "luz exterior":
                    d["estado"] = "Encendido"
                    dispositivos_modificados.append(d["id_dispositivo"])
            return dispositivos_modificados
        

def consultar_automatizaciones_activas():
    activas = [a for a in automatizaciones if a.get("condicion")]
    if not activas:
        return"No hay automatizaciones activas."
    else:
        resultado = "\n🔄 Automatizaciones activas:\n"
        for a in activas:
            resultado += f"ID: {a['id_auto']}, hora: {a['hora']}, acción: {a['accion']}\n"
        return resultado 