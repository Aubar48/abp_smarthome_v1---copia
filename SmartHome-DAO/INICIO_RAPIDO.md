# ⚡ INICIO RÁPIDO - SmartHome-DAO

## 🎯 Guía de 5 Minutos

---

## 1️⃣ Verificar Instalación

### Requisitos
```bash
# Python 3.8+
python --version

# MySQL
mysql --version

# Dependencias
pip list | findstr mysql
```

---

## 2️⃣ Ejecutar la Aplicación

```bash
# Navegar al directorio
cd "Evidencia 6/SmartHome-DAO"

# Ejecutar
python main.py
```

**Credenciales de prueba:**
```
Email: admin@smarthome.com
Password: admin123
```

---

## 3️⃣ Ejecutar Pruebas

### Opción A: Suite Completa
```bash
python tests/run_all_tests.py
```

### Opción B: PowerShell
```powershell
.\ejecutar_pruebas.ps1
```

### Opción C: Módulo Específico
```bash
# Solo UsuarioDAO
python -m unittest tests.test_usuario_dao -v

# Solo ViviendaDAO
python -m unittest tests.test_vivienda_dao -v
```

---

## 4️⃣ Estructura del Proyecto

```
SmartHome-DAO/
├── main.py                 # ⭐ Punto de entrada
├── app/
│   ├── conn/              # Conexión BD
│   ├── dao/               # Data Access Objects
│   ├── dominio/           # Modelos
│   └── services/          # Lógica de negocio
├── tests/
│   └── run_all_tests.py   # ⭐ Suite de pruebas
└── *.md                   # Documentación
```

---

## 5️⃣ Flujo de Uso

### Usuario Nuevo
1. Ejecutar `python main.py`
2. Seleccionar opción **2** (Registrarse)
3. Ingresar email, nombre y contraseña
4. Iniciar sesión con las credenciales

### Usuario Existente
1. Ejecutar `python main.py`
2. Seleccionar opción **1** (Iniciar sesión)
3. Ingresar credenciales
4. Usar el menú según rol

---

## 6️⃣ Comandos Útiles

### Desarrollo
```bash
# Ver archivos modificados
git status

# Ejecutar un test específico
python -m unittest tests.test_usuario_dao.TestUsuarioDAO.test_crear_usuario -v

# Limpiar caché Python
powershell -Command "Get-ChildItem -Recurse -Filter __pycache__ | Remove-Item -Recurse -Force"
```

### Base de Datos
```sql
-- Ver usuarios
SELECT * FROM Usuario;

-- Ver viviendas
SELECT * FROM Vivienda;

-- Ver dispositivos con vivienda
SELECT d.*, v.nombre_vivienda 
FROM Dispositivo d 
JOIN Vivienda v ON d.id_vivienda = v.id_vivienda;
```

---

## 📚 Documentación Completa

| Archivo | Contenido |
|---------|-----------|
| `README.md` | Documentación principal |
| `RESUMEN_EJECUTIVO.md` | Vista general de correcciones |
| `CORRECCIONES_COMPLETAS.md` | Detalle técnico de correcciones |
| `ESTRUCTURA_TESTS.md` | Guía de pruebas modularizadas |
| `MODULARIZACION_COMPLETADA.md` | Antes/después de modularización |

---

## 🆘 Solución de Problemas

### Error: "No se puede conectar a MySQL"
```python
# Verificar configuración en:
app/conn/db_conn.py

# Ajustar credenciales:
host='localhost'
user='tu_usuario'
password='tu_contraseña'
database='smarthome'
```

### Error: "ModuleNotFoundError: mysql"
```bash
pip install mysql-connector-python
```

### Error: "Table doesn't exist"
```bash
# Ejecutar scripts DDL primero:
cd "Evidencia 5/Bases de Datos/BD-Evidencia-5"
# Ejecutar consultasDDL.sql en MySQL
```

---

## ✅ Checklist de Verificación

Antes de entregar el proyecto, verifica:

- [ ] MySQL corriendo y BD creada
- [ ] Tablas creadas (DDL ejecutado)
- [ ] Datos insertados (DML ejecutado)
- [ ] `python main.py` funciona correctamente
- [ ] Login con admin@smarthome.com funciona
- [ ] Todas las pruebas pasan (26+ tests)
- [ ] Sin errores en consola
- [ ] Documentación revisada

---

## 🎯 Próximos Pasos

1. **Revisar documentación:** `README.md`
2. **Entender correcciones:** `CORRECCIONES_COMPLETAS.md`
3. **Explorar tests:** `ESTRUCTURA_TESTS.md`
4. **Probar aplicación:** `python main.py`
5. **Ejecutar pruebas:** `python tests/run_all_tests.py`

---

## 📞 Ayuda Rápida

### ¿Cómo crear un usuario?
```
Menú Principal → 2 (Registrarse) → Ingresar datos
```

### ¿Cómo agregar un dispositivo?
```
Login como Admin → Gestionar Dispositivos → Agregar Dispositivo
```

### ¿Cómo ejecutar solo un test?
```bash
python -m unittest tests.test_usuario_dao -v
```

### ¿Dónde está la BD?
```
Evidencia 5/Bases de Datos/BD-Evidencia-5/
- consultasDDL.sql (estructura)
- consultasDML.sql (datos)
```

---

**¡Listo para empezar!** 🚀

Para más detalles, consulta los archivos `.md` en el directorio raíz.
