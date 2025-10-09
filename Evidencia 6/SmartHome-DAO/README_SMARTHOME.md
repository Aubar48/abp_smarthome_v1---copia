# 🏠 Sistema SmartHome - Evidencia 6

Sistema de gestión domótica con arquitectura DAO (Data Access Object) que permite controlar dispositivos inteligentes en viviendas.

## 📋 Características

- ✅ **Autenticación de usuarios** (Administrador y Usuario normal)
- ✅ **Gestión de viviendas** múltiples
- ✅ **Control de dispositivos** IoT (luces, sensores, cámaras)
- ✅ **Historial de eventos** con registro automático
- ✅ **Base de datos MySQL** con arquitectura DAO
- ✅ **Interfaz de línea de comandos** interactiva

## 🏗️ Arquitectura del Proyecto

```
SmartHome-DAO/
├── app/
│   ├── conn/
│   │   └── db_conn.py          # Conexión a base de datos
│   ├── dao/                     # Data Access Objects
│   │   ├── dispositivo_dao.py
│   │   ├── evento_dispositivo_dao.py
│   │   ├── usuario_dao.py
│   │   └── vivienda_dao.py
│   ├── dominio/                 # Modelos de dominio
│   │   ├── dispositivo.py
│   │   ├── evento_dispositivo.py
│   │   ├── usuario.py
│   │   └── vivienda.py
│   └── services/                # Lógica de negocio
│       ├── dispositivo_service.py
│       ├── evento_dispositivo_service.py
│       ├── usuario_service.py
│       └── vivienda_service.py
├── main.py                      # Aplicación principal
├── test_usuario_normal.py       # Tests automatizados
├── demo_interactiva.py          # Demostración del sistema
├── verificar_usuarios.py        # Utilidad de verificación
└── requirements.txt             # Dependencias
```

## 🚀 Instalación y Configuración

### Prerequisitos

- Python 3.x
- MySQL Server
- pip (gestor de paquetes de Python)

### Paso 1: Instalar dependencias

```powershell
cd "Evidencia 6\SmartHome-DAO"
pip install -r requirements.txt
```

### Paso 2: Configurar la base de datos

1. Asegúrate de que MySQL esté ejecutándose
2. Configura las credenciales en `app/conn/db_conn.py`:

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',  # Tu contraseña de MySQL
    'database': 'smarthome'
}
```

3. Ejecuta el script SQL para crear las tablas:
   - Se encuentra en `Evidencia 5/Bases de Datos/BD-Evidencia-5/consultasDDL.sql`

### Paso 3: Ejecutar el sistema

```powershell
python main.py
```

## 👤 Credenciales de Acceso

### Usuario Administrador
- **Email:** admin@smarthome.com
- **Contraseña:** admin123

### Usuario Normal (para pruebas)
- **Email:** ana@mail.com
- **Contraseña:** user123

## 🧪 Ejecutar Pruebas

### Pruebas Automatizadas
```powershell
python test_usuario_normal.py
```

Este script ejecuta 7 pruebas completas:
1. Login de usuario normal
2. Obtención de viviendas
3. Listado de dispositivos
4. Cambio de estado de dispositivo
5. Verificación de eventos
6. Control de múltiples dispositivos
7. Consulta de historial del sistema

### Demostración Interactiva
```powershell
python demo_interactiva.py
```

Muestra una demostración completa de todas las funcionalidades con emojis y formateo visual.

### Verificar Usuarios en BD
```powershell
python verificar_usuarios.py
```

Muestra todos los usuarios registrados en el sistema.

## 🎯 Funcionalidades por Rol

### 👔 Administrador
- Gestionar usuarios (crear, actualizar, eliminar)
- Gestionar viviendas (crear, asignar usuarios)
- Gestionar dispositivos de todas las viviendas
- Ver historial completo de eventos del sistema

### 👤 Usuario Normal
- Ver sus viviendas asignadas
- Listar dispositivos de sus viviendas
- Controlar dispositivos (encender/apagar)
- Los eventos se registran automáticamente

## 📊 Tipos de Dispositivos

| Tipo | Icono | Estados |
|------|-------|---------|
| Luz | 💡 | Encendido / Apagado |
| Sensor | 🌡️ | Encendido / Apagado |
| Cámara | 📹 | Encendido / Apagado |

## 🔧 Correcciones Aplicadas

### 1. Validación de Entrada Mejorada
- Se implementó extracción automática de números
- Ahora acepta "0. Salir" además de solo "0"

### 2. Registro de Eventos Corregido
- El tipo de evento ahora coincide con el esquema de BD
- Usa 'encendido' o 'apagado' en lugar de 'cambio_estado'

### 3. Métodos de Servicio Completados
- Se agregaron métodos faltantes en `UsuarioService`
- Sistema completamente funcional

## 📝 Base de Datos

### Tablas Principales
- **Usuario**: Almacena administradores y usuarios
- **Vivienda**: Casas/apartamentos del sistema
- **Dispositivo**: Dispositivos IoT instalados
- **EventoDispositivo**: Historial de acciones
- **Usuario_Vivienda**: Asignación usuarios-viviendas (N:M)

### Esquema ER
Consulta el diagrama ER en:
`Evidencia 5/Bases de Datos/BD-Evidencia-5/diagrama-er-foto.png`

## 🛠️ Tecnologías Utilizadas

- **Python 3.x** - Lenguaje de programación
- **MySQL** - Sistema de base de datos
- **mysql-connector-python** - Conector MySQL para Python
- **Patrón DAO** - Arquitectura de acceso a datos

## 📚 Recursos Adicionales

- **Reporte de Pruebas:** `REPORTE_PRUEBAS.md`
- **Diagrama de Clases:** `../DIAGRAMA_CLASES_ACTUALIZADO.md`
- **Scripts SQL:** `../../Evidencia 5/Bases de Datos/BD-Evidencia-5/`

## ⚠️ Notas Importantes

1. Las contraseñas se almacenan en texto plano (para desarrollo)
2. En producción se recomienda usar bcrypt o similar
3. La base de datos se crea automáticamente si no existe
4. Los IDs se autogeneran (AUTO_INCREMENT)

## 🐛 Solución de Problemas

### Error: "Base de datos 'smarthome' no existe"
- Ejecuta primero el script SQL de la Evidencia 5
- O el sistema intentará crearla automáticamente

### Error: "No module named 'mysql'"
```powershell
pip install mysql-connector-python
```

### Error: "Access denied for user"
- Verifica las credenciales en `db_conn.py`
- Asegúrate de que MySQL esté ejecutándose

## 👥 Créditos

**Proyecto:** Sistema SmartHome  
**Evidencia:** 6 (Patrón DAO)  
**Fecha:** Octubre 2025  

---

**¿Necesitas ayuda?** Ejecuta `python demo_interactiva.py` para ver cómo funciona el sistema.
