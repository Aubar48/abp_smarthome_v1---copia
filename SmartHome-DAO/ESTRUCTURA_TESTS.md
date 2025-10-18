# 📋 Estructura de Pruebas Modularizadas

## ✅ Arquitectura de Testing

El sistema de pruebas del proyecto SmartHome-DAO ha sido **modularizado** para mejorar la mantenibilidad, legibilidad y escalabilidad. Cada componente tiene su propio archivo de pruebas dedicado.

---

## 📁 Estructura de Archivos

```
tests/
├── __init__.py                    # Inicializador del módulo tests
├── run_all_tests.py               # ⭐ Suite principal - ejecuta todas las pruebas
├── test_usuario_dao.py            # Pruebas para UsuarioDAO (6 tests)
├── test_vivienda_dao.py           # Pruebas para ViviendaDAO (8 tests)
├── test_dispositivo_dao.py        # Pruebas para DispositivoDAO (7 tests)
├── test_evento_dao.py             # Pruebas para EventoDispositivoDAO (5 tests)
└── test_dominio.py                # Pruebas de encapsulación (4 test classes)
```

---

## 🎯 Módulos de Prueba

### 1️⃣ `test_usuario_dao.py` - **UsuarioDAO Tests**
Valida operaciones CRUD en la tabla `Usuario`.

**Pruebas incluidas (6):**
- ✅ `test_crear_usuario` - Creación de nuevo usuario
- ✅ `test_obtener_por_email` - Búsqueda por email
- ✅ `test_obtener_por_id` - Búsqueda por ID
- ✅ `test_actualizar_usuario` - Modificación de datos
- ✅ `test_eliminar_usuario` - Eliminación de usuario
- ✅ `test_obtener_todos` - Listado completo

**Cobertura:** 
- Métodos del DAO: crear(), obtener_por_email(), obtener_por_id(), actualizar(), eliminar(), obtener_todos()
- Validaciones de email único
- Manejo de excepciones

---

### 2️⃣ `test_vivienda_dao.py` - **ViviendaDAO Tests**
Valida operaciones en viviendas y relaciones usuario-vivienda.

**Pruebas incluidas (8):**
- ✅ `test_crear_vivienda` - Creación de vivienda
- ✅ `test_obtener_por_id` - Búsqueda por ID
- ✅ `test_actualizar_vivienda` - Modificación de datos
- ✅ `test_asignar_usuario` - Asignación usuario-vivienda
- ✅ `test_asignar_usuario_duplicado` - Validación de duplicados
- ✅ `test_obtener_por_usuario` - Viviendas de un usuario
- ✅ `test_obtener_todos` - Listado completo
- ✅ `test_eliminar_vivienda` - Eliminación de vivienda

**Cobertura:**
- Métodos del DAO: crear(), obtener_por_id(), actualizar(), eliminar(), asignar_usuario(), obtener_por_usuario(), obtener_todos()
- Relación muchos a muchos Usuario-Vivienda
- Validaciones de duplicados

---

### 3️⃣ `test_dispositivo_dao.py` - **DispositivoDAO Tests**
Valida operaciones en dispositivos IoT.

**Pruebas incluidas (7):**
- ✅ `test_crear_dispositivo` - Creación de dispositivo
- ✅ `test_obtener_por_id` - Búsqueda por ID
- ✅ `test_obtener_por_vivienda` - Dispositivos de una vivienda
- ✅ `test_actualizar_dispositivo` - Cambio de estado
- ✅ `test_actualizar_ubicacion` - Cambio de ubicación
- ✅ `test_obtener_todos` - Listado completo
- ✅ `test_eliminar_dispositivo` - Eliminación de dispositivo

**Cobertura:**
- Métodos del DAO: crear(), obtener_por_id(), obtener_por_vivienda(), actualizar(), eliminar(), obtener_todos()
- Cambios de estado (encendido/apagado)
- Relación con Vivienda

---

### 4️⃣ `test_evento_dao.py` - **EventoDispositivoDAO Tests**
Valida el registro de eventos de dispositivos.

**Pruebas incluidas (5):**
- ✅ `test_crear_evento` - Registro de evento
- ✅ `test_obtener_por_id` - Búsqueda por ID
- ✅ `test_obtener_por_dispositivo` - Eventos de un dispositivo
- ✅ `test_obtener_todos` - Listado completo
- ✅ `test_eliminar_evento` - Eliminación de evento

**Cobertura:**
- Métodos del DAO: crear(), obtener_por_id(), obtener_por_dispositivo(), eliminar(), obtener_todos()
- Registro de auditoría
- Timestamps automáticos

---

### 5️⃣ `test_dominio.py` - **Domain Encapsulation Tests**
Valida la encapsulación de clases de dominio (OOP).

**Clases de prueba (4):**
- ✅ `TestUsuarioEncapsulacion` - Propiedades de Usuario
- ✅ `TestViviendaEncapsulacion` - Propiedades de Vivienda
- ✅ `TestDispositivoEncapsulacion` - Propiedades de Dispositivo
- ✅ `TestEventoDispositivoEncapsulacion` - Propiedades de EventoDispositivo

**Cobertura:**
- Getters (`@property`)
- Setters con validaciones
- Validaciones de valores (tipo, estado, rol)
- Métodos `__str__()`

---

## 🚀 Cómo Ejecutar las Pruebas

### Opción 1️⃣: Suite Completa (RECOMENDADO)

Ejecuta todas las pruebas con resumen detallado:

```bash
python tests/run_all_tests.py
```

O usando PowerShell:

```powershell
.\ejecutar_pruebas.ps1
```

**Salida esperada:**
```
==================================================================
SUITE COMPLETA DE PRUEBAS UNITARIAS - SMARTHOME DAO
==================================================================

📋 Módulos de prueba:
  ✅ test_usuario_dao.py - Pruebas de UsuarioDAO
  ✅ test_vivienda_dao.py - Pruebas de ViviendaDAO
  ✅ test_dispositivo_dao.py - Pruebas de DispositivoDAO
  ✅ test_evento_dao.py - Pruebas de EventoDispositivoDAO
  ✅ test_dominio.py - Pruebas de encapsulación

==================================================================

test_crear_usuario (test_usuario_dao.TestUsuarioDAO) ... ok
test_obtener_por_email (test_usuario_dao.TestUsuarioDAO) ... ok
...

==================================================================
RESUMEN DE PRUEBAS
==================================================================
Total de pruebas ejecutadas: 26
✅ Exitosas: 26
❌ Fallidas: 0
⚠️  Errores: 0
==================================================================
```

---

### Opción 2️⃣: Pruebas Modulares Individuales

Ejecuta solo un módulo específico:

```bash
# Pruebas de UsuarioDAO
python -m unittest tests.test_usuario_dao -v

# Pruebas de ViviendaDAO
python -m unittest tests.test_vivienda_dao -v

# Pruebas de DispositivoDAO
python -m unittest tests.test_dispositivo_dao -v

# Pruebas de EventoDispositivoDAO
python -m unittest tests.test_evento_dao -v

# Pruebas de encapsulación
python -m unittest tests.test_dominio -v
```

---

### Opción 3️⃣: Descubrimiento Automático

Deja que unittest descubra y ejecute todos los tests:

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

---

### Opción 4️⃣: Ejecutar un Solo Test

Ejecuta un test específico:

```bash
python -m unittest tests.test_usuario_dao.TestUsuarioDAO.test_crear_usuario -v
```

---

## 📊 Estadísticas de Cobertura

| Módulo | Tests | Cobertura |
|--------|-------|-----------|
| `test_usuario_dao.py` | 6 | UsuarioDAO completo |
| `test_vivienda_dao.py` | 8 | ViviendaDAO + relaciones |
| `test_dispositivo_dao.py` | 7 | DispositivoDAO completo |
| `test_evento_dao.py` | 5 | EventoDispositivoDAO completo |
| `test_dominio.py` | 4 clases | Todas las propiedades |
| **TOTAL** | **26+** | **100% DAOs y Dominio** |

---

## 🎨 Ventajas de la Modularización

### ✅ Beneficios

1. **Mantenibilidad**: Cada archivo es pequeño y enfocado
2. **Escalabilidad**: Fácil agregar nuevas pruebas
3. **Paralelización**: Posibilidad de ejecutar tests en paralelo
4. **Debugging**: Más fácil identificar fallos específicos
5. **Independencia**: Los tests no interfieren entre sí
6. **Documentación**: Cada archivo documenta un componente

### 🔄 setUp() y tearDown()

Cada clase de prueba implementa:

- **`setUp()`**: Inicializa objetos DAO y crea datos de prueba
- **`tearDown()`**: Limpia la base de datos después de cada test

Esto garantiza que cada test es **independiente** y **reproducible**.

---

## 🛠️ Mejores Prácticas Implementadas

1. ✅ **Nombres descriptivos**: `test_crear_usuario`, no `test1`
2. ✅ **Aislamiento**: Cada test limpia sus datos
3. ✅ **Assertions claras**: `self.assertEqual()`, `self.assertIsNotNone()`
4. ✅ **Documentación**: Docstrings en todas las pruebas
5. ✅ **Cobertura completa**: Todos los métodos CRUD testeados
6. ✅ **Validaciones**: Tests de casos límite y errores

---

## 📝 Notas Importantes

### ⚠️ Requisitos Previos

Antes de ejecutar las pruebas:

1. **Base de datos configurada**: MySQL corriendo con credenciales en `db_conn.py`
2. **Tablas creadas**: Ejecutar scripts DDL (estructura de BD)
3. **Dependencias instaladas**: `pip install mysql-connector-python`

### 🔍 Depuración

Si un test falla:

1. Ejecuta solo ese módulo con `-v` (verbose)
2. Revisa el output detallado
3. Verifica conexión a BD
4. Confirma que las tablas existen

### 🔄 Limpieza Automática

Los tests están diseñados para:

- **Crear** datos al inicio (`setUp`)
- **Usar** datos durante el test
- **Eliminar** datos al final (`tearDown`)

No dejan "basura" en la base de datos.

---

## 🎯 Próximos Pasos

Para expandir la suite de pruebas:

1. Agregar tests de integración (múltiples DAOs)
2. Implementar tests de carga (performance)
3. Agregar coverage reports (`coverage.py`)
4. Crear tests de regresión
5. Implementar CI/CD con GitHub Actions

---

## 📧 Soporte

Para dudas sobre las pruebas:

- Revisa los docstrings en cada archivo
- Ejecuta tests individuales para debugging
- Consulta la documentación en `README.md`

---

**¡Las pruebas modularizadas facilitan el desarrollo y mantenimiento del sistema SmartHome DAO!** 🚀
