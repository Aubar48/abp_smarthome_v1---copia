# 🏠 SmartHome-DAO

Sistema de gestión de hogares inteligentes con arquitectura DAO (Data Access Object) implementado en Python.

## 📋 Descripción

SmartHome-DAO es un sistema que permite gestionar viviendas inteligentes, dispositivos IoT y usuarios con diferentes roles (administradores y usuarios normales). Implementa el patrón DAO para la persistencia de datos en MySQL.

## ✨ Características

### Gestión de Usuarios
- ✅ Registro de nuevos usuarios
- ✅ Inicio de sesión seguro
- ✅ Roles diferenciados (administrador/usuario)
- ✅ Actualización de datos y contraseñas

### Gestión de Viviendas
- ✅ Crear, listar, editar y eliminar viviendas
- ✅ Asignar usuarios a viviendas
- ✅ Validación de duplicados
- ✅ Estado activo/inactivo

### Gestión de Dispositivos IoT
- ✅ Soporte para luces, sensores y cámaras
- ✅ Control de encendido/apagado
- ✅ Ubicación personalizada
- ✅ Historial de eventos

### Seguridad
- ✅ Contraseñas con `getpass`
- ✅ Validación de permisos por rol
- ✅ Manejo de excepciones robusto
- ✅ Transacciones con rollback

## 🏗️ Arquitectura

```
SmartHome-DAO/
├── app/
│   ├── conn/           # Conexión a base de datos
│   ├── dao/            # Data Access Objects
│   │   └── interfaces/ # Interfaces DAO
│   ├── dominio/        # Modelos de dominio (encapsulados)
│   └── services/       # Lógica de negocio
├── tests/              # Pruebas unitarias
├── main.py             # Punto de entrada
├── .gitignore          # Archivos ignorados
└── README.md           # Este archivo
```

## 🚀 Instalación

### Requisitos
- Python 3.8+
- MySQL 5.7+
- pip

### Pasos

1. **Clonar el repositorio**
```bash
git clone <repositorio>
cd SmartHome-DAO
```

2. **Instalar dependencias**

**Opción A: Usando requirements.txt (RECOMENDADO)**
```bash
pip install -r requirements.txt
```

**Opción B: Instalación manual**
```bash
pip install mysql-connector-python==8.2.0
```

**Verificar instalación:**
```bash
python verificar_dependencias.py
```

3. **Configurar base de datos**
- Crear base de datos en MySQL
- Ejecutar scripts SQL de `Evidencia 5/Bases de Datos/BD-Evidencia-5/`
- Configurar conexión en `app/conn/db_conn.py`

4. **Ejecutar aplicación**
```bash
python main.py
```

### 📦 Dependencias

El proyecto utiliza las siguientes dependencias (ver `requirements.txt`):

| Paquete | Versión | Propósito |
|---------|---------|-----------|
| mysql-connector-python | 8.2.0 | Conexión y operaciones con MySQL |

Para más detalles sobre la instalación, consulta: **[INSTALACION_DEPENDENCIAS.md](INSTALACION_DEPENDENCIAS.md)**

## 🧪 Pruebas Unitarias

El sistema cuenta con una **suite modularizada** de pruebas unitarias para facilitar el mantenimiento y la escalabilidad.

### Estructura Modular

```
tests/
├── run_all_tests.py         # ⭐ Suite principal - ejecuta todas las pruebas
├── test_usuario_dao.py      # Pruebas de UsuarioDAO (6 tests)
├── test_vivienda_dao.py     # Pruebas de ViviendaDAO (8 tests)
├── test_dispositivo_dao.py  # Pruebas de DispositivoDAO (7 tests)
├── test_evento_dao.py       # Pruebas de EventoDispositivoDAO (5 tests)
└── test_dominio.py          # Pruebas de encapsulación (4 test classes)
```

### Ejecutar Todas las Pruebas

**Opción 1: Suite completa (RECOMENDADO)**
```bash
python tests/run_all_tests.py
```

**Opción 2: PowerShell con opciones**
```powershell
.\ejecutar_pruebas.ps1
```

**Opción 3: Descubrimiento automático**
```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

### Ejecutar Módulos Individuales

```bash
# Solo UsuarioDAO
python -m unittest tests.test_usuario_dao -v

# Solo ViviendaDAO
python -m unittest tests.test_vivienda_dao -v

# Solo DispositivoDAO
python -m unittest tests.test_dispositivo_dao -v

# Solo EventoDispositivoDAO
python -m unittest tests.test_evento_dao -v

# Solo encapsulación
python -m unittest tests.test_dominio -v
```

### Cobertura de Pruebas
- ✅ **26+ pruebas unitarias** distribuidas en 5 módulos
- ✅ **100% cobertura de DAOs** (create, read, update, delete)
- ✅ **Validación de encapsulación** en todas las clases de dominio
- ✅ **Limpieza automática** de datos de prueba (setUp/tearDown)
- ✅ **Tests independientes** sin dependencias entre sí

### Documentación Detallada

Para más información sobre la arquitectura de pruebas, consulta:
📄 **[ESTRUCTURA_TESTS.md](ESTRUCTURA_TESTS.md)** - Guía completa de testing

## 📖 Uso

### Usuario Administrador por Defecto
```
Email: admin@smarthome.com
Contraseña: admin123
```

### Menú Principal
```
=== MENÚ PRINCIPAL ===
1. Iniciar sesión
2. Registrarse como nuevo usuario
3. Salir
```

### Panel de Administrador
1. Gestionar Usuarios
2. Gestionar Viviendas (crear, listar, editar, eliminar)
3. Gestionar Dispositivos
4. Ver historial de eventos
5. Acceder a mis viviendas (Panel Usuario)
6. Salir

### Panel de Usuario
- Ver y gestionar dispositivos de sus viviendas
- Encender/apagar dispositivos
- Ver historial de acciones

## 🔧 Tecnologías

- **Backend:** Python 3
- **Base de Datos:** MySQL
- **Patrón:** DAO (Data Access Object)
- **Testing:** unittest
- **Seguridad:** getpass

## 📝 Características Técnicas

### Encapsulación
Todas las clases de dominio usan properties:
```python
@property
def nombre(self):
    return self.__nombre

@nombre.setter
def nombre(self, value):
    self.__nombre = value
```

### Manejo de Errores
Try-catch-finally en todos los DAOs:
```python
try:
    # Operación BD
    conn.commit()
except Exception as e:
    conn.rollback()
    raise
finally:
    cursor.close()
    conn.close()
```

### Validaciones
- Tipos de dispositivos: luz, sensor, camara
- Estados: encendido, apagado
- Roles: administrador, usuario

## 🤝 Contribuciones

1. Fork el proyecto
2. Crear rama de feature (`git checkout -b feature/AmazingFeature`)
3. Commit cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir Pull Request

## 📄 Licencia

Proyecto educativo - ABP SmartHome

## 👥 Autores

Estudiantes del programa de desarrollo

## 📚 Documentación Adicional

- `CORRECCIONES_COMPLETAS.md` - Detalle de todas las correcciones implementadas
- `ESTRUCTURA_TESTS.md` - **Guía completa de la suite de pruebas modularizadas**
- `Evidencia 5/Bases de Datos/` - Scripts SQL y modelo de datos
- `tests/` - Módulos de pruebas unitarias con documentación inline

## 🎯 Estado del Proyecto

✅ **Producción** - Todas las correcciones implementadas

### Características Implementadas
- [x] Gestión de usuarios con roles
- [x] CRUD completo de viviendas
- [x] CRUD completo de dispositivos
- [x] Historial de eventos
- [x] Encapsulación de dominio
- [x] Manejo de excepciones
- [x] Pruebas unitarias
- [x] .gitignore configurado
- [x] Menú de registro
- [x] Validaciones de negocio

## 💡 Mejoras Futuras

- [ ] Autenticación con JWT
- [ ] API REST
- [ ] Frontend web
- [ ] Automatizaciones programadas
- [ ] Notificaciones en tiempo real
- [ ] Dashboard de estadísticas

---

**¡Sistema SmartHome-DAO listo para usar!** 🏡✨
