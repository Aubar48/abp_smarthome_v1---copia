# ✅ Correcciones Realizadas en consultasDML.sql

## 📋 Resumen de Mejoras

Se ha corregido completamente el archivo `consultasDML.sql` para cumplir con **todos los requisitos** de la actividad.

---

## 🔢 1. INSERTs Completos (Mínimo 10 por tabla)

### ✅ Tabla Usuario
- **Cantidad anterior:** 2 registros
- **Cantidad actual:** 12 registros
- **Contenido:** 3 administradores y 9 usuarios normales con diferentes perfiles

### ✅ Tabla Vivienda
- **Cantidad anterior:** 1 registro
- **Cantidad actual:** 12 registros
- **Contenido:** Viviendas variadas (casas, departamentos, lofts, chalets) administradas por diferentes admins

### ✅ Tabla Usuario_Vivienda
- **Cantidad anterior:** 1 registro
- **Cantidad actual:** 12 registros
- **Contenido:** Múltiples asignaciones, algunos usuarios con más de una vivienda

### ✅ Tabla Dispositivo
- **Cantidad anterior:** 3 registros
- **Cantidad actual:** 17 registros
- **Contenido:** Dispositivos variados (luces, sensores, cámaras) distribuidos en múltiples viviendas

### ✅ Tabla EventoDispositivo
- **Cantidad anterior:** 3 registros
- **Cantidad actual:** 15 registros
- **Contenido:** Eventos de encendido, apagado y configuración de diversos dispositivos

---

## 🔍 2. Subconsultas Agregadas (Mínimo 2 requeridas)

### ✅ SUBCONSULTA 1: Viviendas con más dispositivos que el promedio
```sql
-- Obtener viviendas que tienen más dispositivos que el promedio
-- Esta consulta muestra las viviendas "smart" que están por encima del promedio
SELECT v.nombre_vivienda, v.direccion, COUNT(d.id_dispositivo) AS total_dispositivos
FROM Vivienda v
LEFT JOIN Dispositivo d ON v.id_vivienda = d.id_vivienda
GROUP BY v.id_vivienda, v.nombre_vivienda, v.direccion
HAVING COUNT(d.id_dispositivo) > (
    SELECT AVG(cantidad_dispositivos)
    FROM (
        SELECT COUNT(id_dispositivo) AS cantidad_dispositivos
        FROM Dispositivo
        GROUP BY id_vivienda
    ) AS subconsulta_promedio
)
ORDER BY total_dispositivos DESC;
```
**Utilidad:** Identifica viviendas altamente automatizadas

### ✅ SUBCONSULTA 2: Usuarios activos en los últimos 7 días
```sql
-- Usuarios que han generado eventos en los últimos 7 días
-- Útil para identificar usuarios activos vs inactivos
SELECT u.nombre, u.email, u.rol,
    (SELECT COUNT(*) 
     FROM EventoDispositivo e 
     WHERE e.id_usuario = u.id_usuario 
     AND e.fecha_hora >= DATE_SUB(NOW(), INTERVAL 7 DAY)
    ) AS eventos_recientes
FROM Usuario u
WHERE u.id_usuario IN (
    SELECT DISTINCT e2.id_usuario
    FROM EventoDispositivo e2
    WHERE e2.fecha_hora >= DATE_SUB(NOW(), INTERVAL 7 DAY)
)
ORDER BY eventos_recientes DESC;
```
**Utilidad:** Analiza actividad reciente de usuarios

### 🎁 BONUS: Subconsultas adicionales

**SUBCONSULTA 3:** Dispositivos nunca utilizados
- Identifica dispositivos configurados pero sin eventos registrados

**SUBCONSULTA 4:** Viviendas del administrador más activo
- Encuentra el admin con más viviendas y lista sus propiedades

---

## 📊 3. Consultas SELECT Mejoradas

Se agregaron consultas adicionales para análisis completo:

1. ✅ Resumen de usuarios con cantidad de viviendas
2. ✅ Viviendas sin dispositivos (requieren atención)
3. ✅ Top 10 dispositivos más utilizados
4. ✅ Historial de actividad por usuario
5. ✅ Reporte de consumo energético
6. ✅ Carga de trabajo de administradores
7. ✅ Estado de seguridad (cámaras)

---

## 🔄 4. Operaciones UPDATE y DELETE Mejoradas

### UPDATE (8 operaciones diferentes):
- Control de dispositivos (encendido/apagado)
- Actualización de datos de usuarios
- Activación/desactivación de viviendas
- Cambio de ubicación de dispositivos
- Operaciones masivas (apagar todas las luces)
- Cambio de contraseña
- Cambio de roles

### DELETE (5 operaciones diferentes):
- Limpieza de eventos antiguos
- Desactivación de usuarios (UPDATE, no DELETE)
- Eliminación de dispositivos con su historial
- Desasignación de viviendas
- Eliminación completa de usuarios

---

## 📈 5. Consultas por Roles

### Para USUARIOS:
- Ver dispositivos de sus viviendas
- Ver su historial de actividad

### Para ADMINISTRADORES:
- Panel de control de todas sus viviendas
- Auditoría completa de eventos
- Gestión de usuarios asignados

---

## 🎯 Cumplimiento de Requisitos

| Requisito | Solicitado | Entregado | Estado |
|-----------|------------|-----------|--------|
| INSERTs por tabla | Mínimo 10 | 12-17 | ✅ COMPLETO |
| Subconsultas | Mínimo 2 | 4 | ✅ COMPLETO |
| SELECT variados | Varios | 15+ | ✅ COMPLETO |
| UPDATE | Varios | 8 | ✅ COMPLETO |
| DELETE | Varios | 5 | ✅ COMPLETO |

---

## 📝 Notas Técnicas

1. **Integridad Referencial:** Todas las operaciones respetan las claves foráneas
2. **Orden de Eliminación:** Los DELETE siguen el orden correcto para evitar errores
3. **Datos Realistas:** Los INSERTs contienen datos variados y realistas
4. **Subconsultas Complejas:** Incluyen agregación, filtrado temporal y comparaciones
5. **Documentación:** Cada consulta incluye comentarios explicativos

---

## 🚀 Archivo Listo para Evaluación

El archivo `consultasDML.sql` ahora cumple **completamente** con todos los requisitos de la consigna y está listo para ser evaluado.
