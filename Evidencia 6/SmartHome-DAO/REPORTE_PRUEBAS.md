# 📋 REPORTE DE PRUEBAS Y CORRECCIONES - SMARTHOME (Evidencia 6)

**Fecha:** 9 de octubre de 2025  
**Proyecto:** Sistema SmartHome - DAO  
**Usuario de Prueba:** Ana G. Pérez (ana@mail.com)

---

## ✅ RESUMEN EJECUTIVO

Se ha ejecutado y testeado exitosamente el proyecto SmartHome ubicado en `Evidencia 6/SmartHome-DAO`. 
El sistema fue probado con un **usuario normal** y todas las funcionalidades están operativas.

---

## 🔧 PROBLEMAS ENCONTRADOS Y CORRECCIONES APLICADAS

### 1. **Validación de Entrada de Usuario**
**Problema:** Cuando el usuario escribía "0. Salir" o "1. Opción" en lugar de solo el número, 
el sistema mostraba "Entrada no válida" porque no podía convertir el texto completo a entero.

**Solución Aplicada:**
- Se agregó `.strip()` a todas las entradas de usuario
- Se implementó extracción del primer número usando `opcion.split('.')[0].split()[0].strip()`
- Archivos modificados: `main.py` (funciones `panel_usuario` y `gestionar_dispositivos_usuario`)

**Código agregado:**
```python
# Extraer solo el primer número si el usuario escribe algo como "0. Salir"
opcion_num = opcion.split('.')[0].split()[0].strip()
```

---

### 2. **Tipo de Evento Incorrecto en Base de Datos**
**Problema:** El servicio de dispositivos registraba eventos con tipo 'cambio_estado', 
pero el esquema de base de datos solo permite: 'encendido', 'apagado', 'configuracion'.

**Solución Aplicada:**
- Se modificó `dispositivo_service.py` para usar el nuevo estado como tipo de evento
- Ahora registra correctamente 'encendido' o 'apagado' según el cambio

**Código corregido:**
```python
# Registrar el evento con el tipo correcto según el nuevo estado
tipo_evento = nuevo_estado  # 'encendido' o 'apagado'
```

**Archivo modificado:** `app/services/dispositivo_service.py`

---

### 3. **Métodos Faltantes en UsuarioService**
**Problema:** El `main.py` llamaba a métodos que no existían en `UsuarioService`:
- `obtener_todos_los_usuarios()`
- `actualizar_usuario()`
- `eliminar_usuario()`

**Solución Aplicada:**
- Se implementaron los tres métodos faltantes en `usuario_service.py`

**Archivo modificado:** `app/services/usuario_service.py`

---

## 🧪 PRUEBAS REALIZADAS

### Script de Pruebas Automatizadas
Se creó el archivo `test_usuario_normal.py` que ejecuta 7 pruebas completas:

1. ✅ **Login de Usuario Normal**
   - Usuario: ana@mail.com
   - Contraseña: user123
   - Resultado: Login exitoso

2. ✅ **Obtener Viviendas del Usuario**
   - Viviendas encontradas: 1
   - Casa de Ana (Av. Falsa 123)

3. ✅ **Obtener Dispositivos de Vivienda**
   - Dispositivos encontrados: 4
   - Luz Sala (luz, encendido)
   - Sensor Temperatura (sensor, encendido)
   - Cámara Entrada (camara, encendido)
   - smartv (sensor, apagado)

4. ✅ **Cambiar Estado de Dispositivo**
   - Dispositivo: Luz Sala
   - Estado original: encendido → apagado
   - Estado restaurado: apagado → encendido
   - Resultado: Exitoso

5. ✅ **Verificar Registro de Eventos**
   - Eventos registrados para 'Luz Sala': 3
   - Los eventos incluyen tipo, usuario, fecha y detalle

6. ✅ **Control de Múltiples Dispositivos**
   - Dispositivos controlados: 3 de 3
   - Todos los cambios de estado exitosos
   - Estados restaurados correctamente

7. ✅ **Listado de Eventos del Sistema**
   - Total de eventos en el sistema: 11+
   - Formato correcto con fecha, dispositivo, tipo y usuario

---

## 📊 FUNCIONALIDADES TESTEADAS (Usuario Normal)

### Panel de Usuario
- ✅ Login con credenciales
- ✅ Visualización de viviendas asignadas
- ✅ Navegación entre menús
- ✅ Salir del sistema

### Gestión de Dispositivos
- ✅ Listar dispositivos de una vivienda
- ✅ Ver estado actual de cada dispositivo
- ✅ Cambiar estado (encendido/apagado)
- ✅ Registro automático de eventos

### Sistema de Eventos
- ✅ Registro automático al cambiar estado
- ✅ Almacenamiento de fecha/hora
- ✅ Registro de usuario que realizó la acción
- ✅ Detalle de cambio de estado

---

## 🗄️ ESTADO DE LA BASE DE DATOS

**Motor:** MySQL  
**Base de datos:** smarthome  
**Conexión:** ✅ Exitosa

**Usuarios en el sistema:**
1. admin@smarthome.com (Administrador Principal) - admin123
2. ana@mail.com (Ana G. Pérez) - user123

**Viviendas:**
- Casa de Ana (ID: 1)

**Dispositivos:**
- 4 dispositivos activos en Casa de Ana

**Eventos:**
- Sistema registrando eventos correctamente

---

## 📁 ARCHIVOS CREADOS/MODIFICADOS

### Archivos Modificados
1. `main.py` - Corrección de validación de entrada
2. `app/services/dispositivo_service.py` - Corrección de tipo de evento
3. `app/services/usuario_service.py` - Métodos faltantes agregados

### Archivos Creados
1. `test_usuario_normal.py` - Script de pruebas automatizadas
2. `verificar_usuarios.py` - Utilidad para verificar usuarios en BD

---

## 🎯 CONCLUSIONES

✅ **Todas las funcionalidades del usuario normal están operativas**
✅ **Sistema maneja correctamente los dispositivos y eventos**
✅ **Validación de entrada mejorada**
✅ **Base de datos funcionando correctamente**
✅ **Todas las pruebas automatizadas pasaron exitosamente**

### Recomendaciones para Mejoras Futuras
1. Implementar encriptación de contraseñas (actualmente en texto plano)
2. Agregar validación de formato de email
3. Implementar paginación para listas largas de dispositivos
4. Agregar confirmación antes de cambiar estados críticos
5. Implementar sistema de roles más granular
6. Agregar logs del sistema para debugging

---

## 🚀 CÓMO EJECUTAR EL PROYECTO

### Ejecutar Sistema Interactivo
```powershell
cd "c:\Users\rocii\Desktop\barbosa\abp_smarthome_v1 - copia\Evidencia 6\SmartHome-DAO"
python main.py
```

**Credenciales de Usuario Normal:**
- Email: ana@mail.com
- Contraseña: user123

**Credenciales de Administrador:**
- Email: admin@smarthome.com
- Contraseña: admin123

### Ejecutar Pruebas Automatizadas
```powershell
cd "c:\Users\rocii\Desktop\barbosa\abp_smarthome_v1 - copia\Evidencia 6\SmartHome-DAO"
python test_usuario_normal.py
```

---

**Reporte generado por:** GitHub Copilot  
**Última actualización:** 9 de octubre de 2025
