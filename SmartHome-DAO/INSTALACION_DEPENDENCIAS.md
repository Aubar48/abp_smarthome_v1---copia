# 📦 Guía de Instalación de Dependencias - SmartHome-DAO

## 🎯 Dependencias del Proyecto

El proyecto SmartHome-DAO requiere **Python 3.8 o superior** y las siguientes dependencias:

### Dependencias Principales

| Paquete | Versión | Propósito |
|---------|---------|-----------|
| `mysql-connector-python` | 8.2.0 | Conexión y operaciones con MySQL |

---

## 🚀 Instalación Rápida

### Opción 1: Usando requirements.txt (RECOMENDADO)

```bash
# Navegar al directorio del proyecto
cd "SmartHome-DAO"

# Instalar todas las dependencias
pip install -r requirements.txt
```

### Opción 2: Instalación Manual

```bash
pip install mysql-connector-python==8.2.0
```

---

## 🔍 Verificar Instalación

Después de instalar, verifica que todo esté correcto:

```bash
# Ver paquetes instalados
pip list

# Verificar versión de mysql-connector-python
pip show mysql-connector-python
```

**Salida esperada:**
```
Name: mysql-connector-python
Version: 8.2.0
Summary: MySQL driver written in Python
```

---

## 🐍 Requisitos de Python

### Versión Mínima
```bash
python --version
# Debe mostrar: Python 3.8.0 o superior
```

### Versiones Recomendadas
- ✅ Python 3.8
- ✅ Python 3.9
- ✅ Python 3.10
- ✅ Python 3.11
- ✅ Python 3.12

---

## 🛠️ Instalación en Diferentes Sistemas

### Windows

```powershell
# Verificar Python
python --version

# Actualizar pip
python -m pip install --upgrade pip

# Instalar dependencias
pip install -r requirements.txt
```

### macOS / Linux

```bash
# Verificar Python
python3 --version

# Actualizar pip
python3 -m pip install --upgrade pip

# Instalar dependencias
pip3 install -r requirements.txt
```

---

## 🧪 Dependencias Opcionales (Desarrollo)

Si vas a desarrollar o ejecutar tests:

```bash
# Instalar herramientas de testing
pip install pytest==7.4.3
pip install pytest-cov==4.1.0

# Instalar herramientas de análisis de código
pip install pylint==3.0.3
pip install flake8==6.1.0
```

---

## 🔧 Solución de Problemas

### Problema 1: "pip no se reconoce"

**Windows:**
```powershell
# Agregar Python al PATH
# Configuración del sistema → Variables de entorno → PATH
# Agregar: C:\Python3X\Scripts
```

**Solución alternativa:**
```powershell
python -m pip install -r requirements.txt
```

### Problema 2: "Permission denied" (Linux/macOS)

```bash
# Usar --user para instalar en directorio de usuario
pip install --user -r requirements.txt

# O usar sudo (no recomendado)
sudo pip install -r requirements.txt
```

### Problema 3: "MySQL Connector Error"

Si hay problemas al instalar `mysql-connector-python`:

```bash
# Opción 1: Versión pura Python (más compatible)
pip install mysql-connector-python-pure

# Opción 2: Instalar desde binarios
pip install --only-binary :all: mysql-connector-python
```

### Problema 4: Conflictos de Versión

```bash
# Desinstalar versión antigua
pip uninstall mysql-connector-python

# Instalar versión específica
pip install mysql-connector-python==8.2.0
```

---

## 📋 Verificación Completa

Ejecuta este script para verificar todo:

```python
# verificar_dependencias.py
import sys

print(f"Python version: {sys.version}")
print(f"Python executable: {sys.executable}")
print()

try:
    import mysql.connector
    print(f"✅ mysql-connector-python: {mysql.connector.__version__}")
except ImportError as e:
    print(f"❌ mysql-connector-python: NO INSTALADO")
    print(f"   Error: {e}")

print("\n✨ Verificación completada!")
```

**Ejecutar:**
```bash
python verificar_dependencias.py
```

**Salida esperada:**
```
Python version: 3.10.0 (main, Oct  5 2021, 10:15:23)
Python executable: C:\Python310\python.exe

✅ mysql-connector-python: 8.2.0

✨ Verificación completada!
```

---

## 🌐 Entornos Virtuales (Recomendado)

### Crear Entorno Virtual

**Windows:**
```powershell
# Crear entorno virtual
python -m venv venv

# Activar entorno
.\venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

**macOS / Linux:**
```bash
# Crear entorno virtual
python3 -m venv venv

# Activar entorno
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### Desactivar Entorno Virtual

```bash
deactivate
```

---

## 📊 Estado de Dependencias

### Actualizar requirements.txt

Si instalas nuevas dependencias:

```bash
# Generar requirements.txt actualizado
pip freeze > requirements.txt

# O solo las principales (recomendado)
pip list --format=freeze > requirements.txt
```

### Verificar Actualizaciones Disponibles

```bash
# Ver paquetes desactualizados
pip list --outdated

# Actualizar un paquete específico
pip install --upgrade mysql-connector-python
```

---

## 🔐 Seguridad

### Verificar Vulnerabilidades

```bash
# Instalar herramienta de auditoría
pip install safety

# Verificar vulnerabilidades
safety check

# O verificar requirements.txt
safety check -r requirements.txt
```

---

## 📦 Instalación para Producción

### Instalación sin caché (más limpia)

```bash
pip install --no-cache-dir -r requirements.txt
```

### Instalación con hash (más segura)

```bash
# Generar requirements con hash
pip freeze > requirements.txt

# Instalar verificando hash
pip install --require-hashes -r requirements.txt
```

---

## 🎓 Comandos Útiles

```bash
# Ver información de un paquete
pip show mysql-connector-python

# Listar archivos de un paquete
pip show -f mysql-connector-python

# Desinstalar paquete
pip uninstall mysql-connector-python

# Desinstalar todo de requirements.txt
pip uninstall -r requirements.txt -y

# Reinstalar todo
pip install --force-reinstall -r requirements.txt
```

---

## 📝 Notas Importantes

### ⚠️ Compatibilidad

- **Python 2.x:** ❌ NO soportado (usar Python 3.8+)
- **MySQL 5.7+:** ✅ Compatible
- **MySQL 8.0+:** ✅ Compatible y recomendado

### 🔄 Actualizaciones

El archivo `requirements.txt` se actualiza cuando:
- Se agrega una nueva dependencia al proyecto
- Se actualiza la versión de una dependencia existente
- Se remueve una dependencia obsoleta

### 📚 Documentación

- **mysql-connector-python:** https://dev.mysql.com/doc/connector-python/en/
- **pip:** https://pip.pypa.io/en/stable/
- **venv:** https://docs.python.org/3/library/venv.html

---

## ✅ Checklist de Instalación

Antes de ejecutar el proyecto:

- [ ] Python 3.8+ instalado
- [ ] pip actualizado (`python -m pip install --upgrade pip`)
- [ ] requirements.txt descargado
- [ ] Dependencias instaladas (`pip install -r requirements.txt`)
- [ ] MySQL instalado y corriendo
- [ ] Base de datos creada
- [ ] Configuración de conexión en `app/conn/db_conn.py`

---

## 🚀 Siguiente Paso

Después de instalar las dependencias:

1. **Configurar MySQL:** Ver `README.md` - Sección "Instalación"
2. **Ejecutar scripts DDL:** Crear estructura de base de datos
3. **Ejecutar scripts DML:** Insertar datos de prueba
4. **Ejecutar aplicación:** `python main.py`

---

## 📞 Soporte

Si tienes problemas con la instalación:

1. Verifica la versión de Python: `python --version`
2. Verifica la versión de pip: `pip --version`
3. Consulta la sección "Solución de Problemas" arriba
4. Revisa los logs de error completos
5. Consulta la documentación oficial de pip

---

**¡Instalación exitosa!** 🎉

Una vez instaladas todas las dependencias, el proyecto SmartHome-DAO está listo para ejecutarse.
