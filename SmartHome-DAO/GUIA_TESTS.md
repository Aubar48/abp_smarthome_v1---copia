# 📋 Guía de Ejecución de Tests - SmartHome-DAO

## 🚀 Cómo ejecutar los tests

### **Método 1: Script simplificado (Recomendado)**

```powershell
# Ejecutar TODOS los tests
python ejecutar_pruebas2_tdd.py all

# Modo interactivo (menú)
python ejecutar_pruebas2_tdd.py

# Ejecutar tests específicos
python ejecutar_pruebas2_tdd.py usuario
python ejecutar_pruebas2_tdd.py vivienda
python ejecutar_pruebas2_tdd.py dispositivo
python ejecutar_pruebas2_tdd.py evento
python ejecutar_pruebas2_tdd.py dominio
```

---

### **Método 2: Script PowerShell (alternativo)**

```powershell
.\ejecutar_pruebas.ps1
```

---

### **Método 3: Comandos directos de unittest**

```powershell
# Suite completa
python tests/run_all_tests.py

# Módulos individuales
python -m unittest tests.test_usuario_dao -v
python -m unittest tests.test_vivienda_dao -v
python -m unittest tests.test_dispositivo_dao -v
python -m unittest tests.test_evento_dao -v
python -m unittest tests.test_dominio -v

# Descubrimiento automático
python -m unittest discover -s tests -p "test_*.py" -v
```

---

## 📦 Estructura de Tests

### **5 Módulos de prueba:**

1. **test_usuario_dao.py** (6 test classes)
   - Pruebas CRUD de usuarios
   - Validaciones de email y rol
   - Búsquedas y actualizaciones

2. **test_vivienda_dao.py** (8 test classes)
   - Pruebas CRUD de viviendas
   - Gestión de usuarios asignados
   - Estados de viviendas

3. **test_dispositivo_dao.py** (7 test classes)
   - Pruebas CRUD de dispositivos
   - Tipos: luz, sensor, camara
   - Estados: encendido, apagado

4. **test_evento_dao.py** (5 test classes)
   - Registro de eventos
   - Tipos: encendido, apagado, configuracion
   - Consultas por dispositivo/vivienda

5. **test_dominio.py** (4 test classes)
   - Encapsulación con @property
   - Validaciones en setters
   - Modelos: Usuario, Vivienda, Dispositivo, Evento

**Total:** 26+ pruebas unitarias

---

## ⚙️ Requisitos Previos

### **1. MySQL Server**
```powershell
# Verificar que MySQL esté corriendo
# Windows: Servicios > MySQL80
# O desde PowerShell:
Get-Service MySQL80
```

### **2. Base de Datos**
```sql
CREATE DATABASE IF NOT EXISTS smarthome_db;
USE smarthome_db;
-- Ejecutar los scripts DDL y DML
```

### **3. Configuración de Conexión**
Archivo: `app/conn/db_conn.py`
```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'tu_usuario',
    'password': 'tu_password',
    'database': 'smarthome_db'
}
```

### **4. Dependencias Python**
```powershell
pip install -r requirements.txt
# o directamente:
pip install mysql-connector-python==8.2.0
```

---

## 🎯 Ejemplos de Uso

### **Ejecución Rápida**
```powershell
# Navegar al directorio
cd "SmartHome-DAO"

# Ejecutar todos los tests
python ejecutar_pruebas2_tdd.py all
```

### **Menú Interactivo**
```powershell
python ejecutar_pruebas2_tdd.py

# Aparecerá el menú:
# ============================================================
# SISTEMA DE PRUEBAS - SMARTHOME-DAO
# ============================================================
# 1. Ejecutar todas las pruebas
# 2. Ejecutar pruebas de UsuarioDAO
# 3. Ejecutar pruebas de ViviendaDAO
# 4. Ejecutar pruebas de DispositivoDAO
# 5. Ejecutar pruebas de EventoDispositivoDAO
# 6. Ejecutar pruebas de Encapsulación (Dominio)
# 7. Mostrar información del sistema
# 0. Salir
# ============================================================
```

### **Tests Específicos**
```powershell
# Solo tests de Usuario
python ejecutar_pruebas2_tdd.py usuario

# Solo tests de Dispositivo
python ejecutar_pruebas2_tdd.py dispositivo

# Solo tests de Encapsulación
python ejecutar_pruebas2_tdd.py dominio
```

---

## 📊 Interpretación de Resultados

### **✅ Ejecución Exitosa**
```
================================================================================
RESUMEN DE PRUEBAS
================================================================================
Pruebas ejecutadas: 26
Errores: 0
Fallos: 0

✅ TODAS LAS PRUEBAS PASARON EXITOSAMENTE!
El sistema SmartHome-DAO está funcionando correctamente.
================================================================================
```

### **❌ Errores Comunes**

#### **Error de Conexión MySQL**
```
Error: Can't connect to MySQL server on 'localhost'
```
**Solución:** Iniciar MySQL Server
```powershell
# Windows
net start MySQL80
# O desde Servicios
```

#### **Base de Datos no existe**
```
Error: Unknown database 'smarthome_db'
```
**Solución:** Crear la base de datos
```sql
CREATE DATABASE smarthome_db;
```

#### **Módulo no encontrado**
```
ModuleNotFoundError: No module named 'mysql'
```
**Solución:** Instalar dependencias
```powershell
pip install mysql-connector-python
```

---

## 🔄 Comparación con POO-SmartHome

| Característica | POO-SmartHome | SmartHome-DAO |
|----------------|---------------|---------------|
| **Ubicación** | `POO-SmartHome/` | `SmartHome-DAO/` |
| **Script** | `ejecutar_pruebas_tdd.py` | `ejecutar_pruebas2_tdd.py` |
| **Tests** | 25 (5 por clase) | 26+ (modularizados) |
| **Patrón** | POO básico | DAO + Servicios |
| **Base de Datos** | No requiere | Requiere MySQL |
| **Comando** | `python ejecutar_pruebas_tdd.py all` | `python ejecutar_pruebas2_tdd.py all` |

---

## 📝 Notas Adicionales

- **Verbosity=2:** Los tests se ejecutan con máximo detalle
- **Límite de errores:** Los mensajes de error se truncan a 200 caracteres para legibilidad
- **Independencia:** Cada módulo puede ejecutarse por separado
- **Cleanup automático:** Los tests limpian datos de prueba después de ejecutarse

---

## 🆘 Verificación de Dependencias

Usa el script de verificación:
```powershell
python verificar_dependencias.py
```

Este script verifica:
- ✅ Versión de Python
- ✅ mysql-connector-python instalado
- ✅ Conexión a MySQL
- ✅ Base de datos configurada

---

## 📞 Soporte

Si los tests fallan:
1. Verificar que MySQL esté corriendo
2. Verificar configuración en `app/conn/db_conn.py`
3. Revisar que la BD `smarthome_db` exista
4. Ejecutar tests individuales para aislar el problema

**Ejemplo de diagnóstico:**
```powershell
# Verificar solo el módulo con problemas
python ejecutar_pruebas2_tdd.py usuario
```
