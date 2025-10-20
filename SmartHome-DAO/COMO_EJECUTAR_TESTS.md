# 🚀 Cómo Ejecutar Tests - SmartHome-DAO

## ✅ Método Rápido (Igual que POO-SmartHome)

```powershell
# Ejecutar TODOS los tests
python ejecutar_pruebas2_tdd.py all

# Modo interactivo con menú
python ejecutar_pruebas2_tdd.py

# Tests específicos
python ejecutar_pruebas2_tdd.py usuario
python ejecutar_pruebas2_tdd.py vivienda
python ejecutar_pruebas2_tdd.py dispositivo
python ejecutar_pruebas2_tdd.py evento
python ejecutar_pruebas2_tdd.py dominio
```

---

## 📋 Comparación Rápida

| Proyecto | Comando |
|----------|---------|
| **POO-SmartHome** | `python ejecutar_pruebas_tdd.py all` |
| **SmartHome-DAO** | `python ejecutar_pruebas2_tdd.py all` |

Ambos funcionan exactamente igual! 🎯

---

## 📊 Resultado Esperado

```
================================================================================
EJECUTANDO PRUEBAS - SISTEMA SMARTHOME-DAO
================================================================================
- Patrón DAO (Data Access Object)
- Capa de Servicios
- Encapsulación con @property
- Conexión a MySQL
================================================================================

... ejecutando 39 pruebas ...

================================================================================
RESUMEN DE PRUEBAS
================================================================================
Pruebas ejecutadas: 39
Errores: 0
Fallos: 0

✅ TODAS LAS PRUEBAS PASARON EXITOSAMENTE!
El sistema SmartHome-DAO está funcionando correctamente.
================================================================================
```

---

## ⚠️ Requisito

**MySQL debe estar corriendo** para que todos los tests pasen.

Si no tienes MySQL:
- Las pruebas de **dominio** (encapsulación) pasarán ✅
- Las pruebas de **DAOs** fallarán ❌ (requieren conexión a BD)

**Total de tests:** 39 pruebas
- 35 pruebas de DAOs (requieren MySQL)
- 4 pruebas de dominio (NO requieren MySQL)

---

## 🎯 Opciones del Menú Interactivo

```
============================================================
SISTEMA DE PRUEBAS - SMARTHOME-DAO
============================================================
1. Ejecutar todas las pruebas
2. Ejecutar pruebas de UsuarioDAO
3. Ejecutar pruebas de ViviendaDAO
4. Ejecutar pruebas de DispositivoDAO
5. Ejecutar pruebas de EventoDispositivoDAO
6. Ejecutar pruebas de Encapsulación (Dominio)
7. Mostrar información del sistema
0. Salir
============================================================
```

---

## 📝 Notas

- El script `ejecutar_pruebas2_tdd.py` funciona **idéntico** a `ejecutar_pruebas_tdd.py` de POO-SmartHome
- Mismo formato, mismos comandos, misma experiencia de usuario
- La única diferencia es el número: `ejecutar_pruebas2_tdd.py` vs `ejecutar_pruebas_tdd.py`

---

## 🆘 Si hay errores

Revisa `GUIA_TESTS.md` para soluciones detalladas de problemas comunes.
