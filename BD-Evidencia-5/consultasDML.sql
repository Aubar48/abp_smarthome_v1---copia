-- =============================================================================
-- DML COMPLETO - Sistema SmartHome con 2 Roles
-- Consultas para manipular datos: insertar, consultar, actualizar y eliminar
-- =============================================================================

-- -----------------------------------------------------------------------------
-- INSERT: Insertar datos de prueba en todas las tablas (MÍNIMO 10 POR TABLA)
-- -----------------------------------------------------------------------------

-- 1) Crear usuarios del sistema (10+ usuarios con diferentes roles)
INSERT INTO Usuario (id_usuario, email, nombre, contraseña, rol) VALUES 
(1, 'admin@smarthome.com', 'Administrador Principal', 'admin123', 'administrador'),
(2, 'ana@mail.com', 'Ana García Pérez', 'user123', 'usuario'),
(3, 'carlos@mail.com', 'Carlos López Martínez', 'pass456', 'usuario'),
(4, 'maria@mail.com', 'María Rodríguez Silva', 'maria789', 'usuario'),
(5, 'admin2@smarthome.com', 'Juan Administrador', 'admin456', 'administrador'),
(6, 'pedro@mail.com', 'Pedro Sánchez Torres', 'pedro123', 'usuario'),
(7, 'laura@mail.com', 'Laura Fernández Ruiz', 'laura456', 'usuario'),
(8, 'jorge@mail.com', 'Jorge Ramírez Castro', 'jorge789', 'usuario'),
(9, 'sofia@mail.com', 'Sofía Morales Vega', 'sofia123', 'usuario'),
(10, 'diego@mail.com', 'Diego Herrera Luna', 'diego456', 'usuario'),
(11, 'elena@mail.com', 'Elena Castro Díaz', 'elena789', 'usuario'),
(12, 'admin3@smarthome.com', 'Roberto Admin', 'admin789', 'administrador');

-- 2) Crear viviendas en el sistema (10+ viviendas administradas por diferentes admins)
INSERT INTO Vivienda (id_vivienda, nombre_vivienda, direccion, id_administrador) VALUES 
(1, 'Casa de Ana', 'Av. Falsa 123', 1),
(2, 'Departamento Centro', 'Calle Mayor 456', 1),
(3, 'Casa Familiar López', 'Calle del Sol 789', 5),
(4, 'Apartamento Moderno', 'Av. Libertad 321', 5),
(5, 'Casa de Playa', 'Paseo Marítimo 654', 12),
(6, 'Casa Suburbana', 'Calle Primavera 987', 1),
(7, 'Loft Urbano', 'Av. Moderna 147', 5),
(8, 'Chalet Montaña', 'Camino Alto 258', 12),
(9, 'Piso Estudiantes', 'Calle Universidad 369', 1),
(10, 'Casa Residencial', 'Barrio Norte 741', 5),
(11, 'Apartamento Premium', 'Torre Central Piso 15', 12),
(12, 'Casa Jardín', 'Av. Bosques 852', 1);

-- 3) Asignar viviendas a los usuarios (10+ asignaciones)
INSERT INTO Usuario_Vivienda (id_usuario, id_vivienda) VALUES
(2, 1),   -- Ana en Casa de Ana
(3, 2),   -- Carlos en Departamento Centro
(4, 3),   -- María en Casa Familiar López
(6, 4),   -- Pedro en Apartamento Moderno
(7, 5),   -- Laura en Casa de Playa
(8, 6),   -- Jorge en Casa Suburbana
(9, 7),   -- Sofía en Loft Urbano
(10, 8),  -- Diego en Chalet Montaña
(11, 9),  -- Elena en Piso Estudiantes
(2, 10),  -- Ana también en Casa Residencial
(3, 11),  -- Carlos también en Apartamento Premium
(4, 12);  -- María también en Casa Jardín

-- 4) Instalar dispositivos IoT en las viviendas (10+ dispositivos variados)
INSERT INTO Dispositivo (id_dispositivo, nombre_dispositivo, tipo, estado, ubicacion, id_vivienda) VALUES 
-- Dispositivos para Casa de Ana (ID: 1)
(1, 'Luz Sala', 'luz', 'apagado', 'Sala Principal', 1),
(2, 'Sensor Temperatura Cocina', 'sensor', 'encendido', 'Cocina', 1),
(3, 'Cámara Entrada Principal', 'camara', 'encendido', 'Puerta Principal', 1),
(4, 'Luz Dormitorio', 'luz', 'apagado', 'Dormitorio Principal', 1),
-- Dispositivos para Departamento Centro (ID: 2)
(5, 'Sensor Movimiento', 'sensor', 'encendido', 'Pasillo', 2),
(6, 'Luz Comedor', 'luz', 'encendido', 'Comedor', 2),
(7, 'Cámara Garaje', 'camara', 'encendido', 'Garaje', 2),
-- Dispositivos para Casa Familiar López (ID: 3)
(8, 'Sensor Humedad', 'sensor', 'encendido', 'Baño Principal', 3),
(9, 'Luz Exterior', 'luz', 'encendido', 'Jardín Frontal', 3),
(10, 'Cámara Patio', 'camara', 'apagado', 'Patio Trasero', 3),
(11, 'Luz Cocina', 'luz', 'apagado', 'Cocina', 3),
-- Dispositivos para Apartamento Moderno (ID: 4)
(12, 'Sensor Temperatura Sala', 'sensor', 'encendido', 'Sala', 4),
(13, 'Luz Balcón', 'luz', 'apagado', 'Balcón', 4),
(14, 'Cámara Entrada', 'camara', 'encendido', 'Hall Entrada', 4),
-- Dispositivos para Casa de Playa (ID: 5)
(15, 'Sensor Puerta', 'sensor', 'encendido', 'Puerta Principal', 5),
(16, 'Luz Terraza', 'luz', 'encendido', 'Terraza', 5),
(17, 'Cámara Playa', 'camara', 'encendido', 'Vista Playa', 5);

-- 5) Registrar actividad: eventos de configuración y uso de dispositivos (10+ eventos)
INSERT INTO EventoDispositivo (id_dispositivo, id_usuario, tipo_evento, detalle) VALUES 
(1, 2, 'encendido', 'Usuario encendió luz de sala'),
(2, 1, 'configuracion', 'Configuración inicial del sensor'),
(3, 1, 'encendido', 'Activación de cámara de seguridad'),
(4, 2, 'apagado', 'Usuario apagó luz de dormitorio'),
(5, 3, 'configuracion', 'Configuración sensor de movimiento'),
(6, 3, 'encendido', 'Encendido de luz de comedor'),
(7, 1, 'configuracion', 'Instalación de cámara en garaje'),
(8, 4, 'encendido', 'Activación sensor de humedad'),
(9, 4, 'encendido', 'Encendido de luz exterior'),
(10, 5, 'apagado', 'Desactivación temporal cámara patio'),
(11, 4, 'apagado', 'Apagado luz cocina'),
(12, 6, 'configuracion', 'Configuración sensor temperatura'),
(13, 6, 'apagado', 'Apagado luz balcón'),
(14, 5, 'encendido', 'Activación cámara entrada'),
(15, 7, 'encendido', 'Activación sensor puerta');

-- -----------------------------------------------------------------------------
-- SELECT: Consultas para visualizar información del sistema
-- -----------------------------------------------------------------------------

-- 1) Listar todos los usuarios organizados por tipo de rol
SELECT nombre, email, rol, fecha_registro
FROM Usuario
ORDER BY rol, nombre;

-- 2) Mostrar viviendas activas con información de sus administradores
SELECT v.nombre_vivienda, v.direccion, u.nombre AS administrador
FROM Vivienda v
JOIN Usuario u ON v.id_administrador = u.id_usuario
WHERE v.activa = TRUE;

-- 3) Inventario completo: todos los dispositivos organizados por vivienda y tipo
SELECT d.nombre_dispositivo, d.tipo, d.estado, d.ubicacion, v.nombre_vivienda
FROM Dispositivo d
JOIN Vivienda v ON d.id_vivienda = v.id_vivienda
ORDER BY v.nombre_vivienda, d.tipo;

-- 4) Historial de actividad: eventos más recientes de todos los dispositivos
SELECT e.fecha_hora, d.nombre_dispositivo, e.tipo_evento, e.detalle, u.nombre AS usuario
FROM EventoDispositivo e
JOIN Dispositivo d ON e.id_dispositivo = d.id_dispositivo
JOIN Usuario u ON e.id_usuario = u.id_usuario
ORDER BY e.fecha_hora DESC;

-- 5) Estadísticas del sistema: cantidad de dispositivos por tipo y estado
SELECT tipo, estado, COUNT(*) as cantidad
FROM Dispositivo
GROUP BY tipo, estado
ORDER BY tipo;

-- =============================================================================
-- SUBCONSULTAS (2 REQUERIDAS)
-- =============================================================================

-- SUBCONSULTA 1: Obtener viviendas que tienen más dispositivos que el promedio
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

-- SUBCONSULTA 2: Usuarios que han generado eventos en los últimos 7 días
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

-- SUBCONSULTA 3 (BONUS): Dispositivos que nunca han sido utilizados
-- Identifica dispositivos configurados pero sin uso
SELECT d.nombre_dispositivo, d.tipo, v.nombre_vivienda
FROM Dispositivo d
JOIN Vivienda v ON d.id_vivienda = v.id_vivienda
WHERE d.id_dispositivo NOT IN (
    SELECT DISTINCT id_dispositivo
    FROM EventoDispositivo
)
ORDER BY v.nombre_vivienda;

-- SUBCONSULTA 4 (BONUS): Viviendas administradas por el admin más activo
-- Encuentra el administrador con más viviendas y lista sus propiedades
SELECT v.nombre_vivienda, v.direccion, u.nombre AS administrador
FROM Vivienda v
JOIN Usuario u ON v.id_administrador = u.id_usuario
WHERE v.id_administrador = (
    SELECT id_administrador
    FROM Vivienda
    GROUP BY id_administrador
    ORDER BY COUNT(*) DESC
    LIMIT 1
)
ORDER BY v.nombre_vivienda;

-- -----------------------------------------------------------------------------
-- SELECT: Consultas adicionales con información agregada
-- -----------------------------------------------------------------------------

-- 6) Resumen de usuarios: cantidad de viviendas asignadas a cada usuario
SELECT u.nombre, u.email, COUNT(uv.id_vivienda) AS total_viviendas
FROM Usuario u
LEFT JOIN Usuario_Vivienda uv ON u.id_usuario = uv.id_usuario
WHERE u.rol = 'usuario'
GROUP BY u.id_usuario, u.nombre, u.email
ORDER BY total_viviendas DESC;

-- 7) Viviendas sin dispositivos instalados (requieren atención)
SELECT v.nombre_vivienda, v.direccion, u.nombre AS administrador
FROM Vivienda v
JOIN Usuario u ON v.id_administrador = u.id_usuario
LEFT JOIN Dispositivo d ON v.id_vivienda = d.id_vivienda
WHERE d.id_dispositivo IS NULL;

-- 8) Dispositivos más utilizados (ordenados por cantidad de eventos)
SELECT d.nombre_dispositivo, d.tipo, v.nombre_vivienda, COUNT(e.id_evento) AS total_eventos
FROM Dispositivo d
JOIN Vivienda v ON d.id_vivienda = v.id_vivienda
LEFT JOIN EventoDispositivo e ON d.id_dispositivo = e.id_dispositivo
GROUP BY d.id_dispositivo, d.nombre_dispositivo, d.tipo, v.nombre_vivienda
ORDER BY total_eventos DESC
LIMIT 10;

-- -----------------------------------------------------------------------------
-- UPDATE: Modificar datos existentes en el sistema
-- -----------------------------------------------------------------------------

-- 1) Control de dispositivos: cambiar estado de encendido/apagado (usuarios normales)
UPDATE Dispositivo 
SET estado = 'encendido' 
WHERE id_dispositivo = 1 AND tipo = 'luz';

-- 2) Actualizar información personal de usuarios
UPDATE Usuario 
SET nombre = 'Ana G. Pérez' 
WHERE email = 'ana@mail.com';

-- 3) Desactivar una vivienda temporalmente (mantenimiento o remodelación)
UPDATE Vivienda
SET activa = FALSE
WHERE id_vivienda = 9;

-- 4) Reactivar vivienda después del mantenimiento
UPDATE Vivienda
SET activa = TRUE
WHERE id_vivienda = 9;

-- 5) Cambiar ubicación de un dispositivo dentro de la vivienda
UPDATE Dispositivo
SET ubicacion = 'Sala de Estar'
WHERE id_dispositivo = 2;

-- 6) Actualizar múltiples dispositivos: apagar todas las luces de una vivienda
UPDATE Dispositivo
SET estado = 'apagado'
WHERE tipo = 'luz' AND id_vivienda = 1;

-- 7) Cambiar contraseña de usuario (simulación de cambio de contraseña)
UPDATE Usuario
SET contraseña = 'nuevapass123'
WHERE id_usuario = 2;

-- 8) Cambiar rol de usuario (promoción o cambio de privilegios)
UPDATE Usuario
SET rol = 'administrador'
WHERE id_usuario = 11 AND email = 'elena@mail.com';

-- -----------------------------------------------------------------------------
-- DELETE: Eliminar datos del sistema (solo administradores)
-- -----------------------------------------------------------------------------

-- 1) Mantenimiento: eliminar eventos antiguos para liberar espacio (mayores a 90 días)
DELETE FROM EventoDispositivo 
WHERE fecha_hora < DATE_SUB(NOW(), INTERVAL 90 DAY);

-- 2) Gestión de usuarios: desactivar cuenta sin eliminar historial (UPDATE, no DELETE)
UPDATE Usuario 
SET activo = FALSE 
WHERE email = 'jorge@mail.com';

-- 3) Eliminación completa: remover dispositivo y todo su historial
-- NOTA: Se debe eliminar primero los eventos asociados por la restricción de clave foránea
DELETE FROM EventoDispositivo WHERE id_dispositivo = 10; -- Primero el historial
DELETE FROM Dispositivo WHERE id_dispositivo = 10;       -- Luego el dispositivo

-- 4) Desasignar usuario de una vivienda específica
DELETE FROM Usuario_Vivienda
WHERE id_usuario = 11 AND id_vivienda = 9;

-- 5) Eliminar usuario completamente del sistema (con todas sus relaciones)
-- NOTA: Orden importante para respetar las claves foráneas
DELETE FROM Usuario_Vivienda WHERE id_usuario = 8;     -- Primero desasignar viviendas
DELETE FROM EventoDispositivo WHERE id_usuario = 8;    -- Eliminar eventos generados
DELETE FROM Usuario WHERE id_usuario = 8;              -- Finalmente eliminar usuario

-- =============================================================================
-- CONSULTAS ESPECÍFICAS SEGÚN EL ROL DEL USUARIO
-- =============================================================================

-- CONSULTA PARA USUARIO NORMAL (Ej: Ana, id_usuario = 2):
-- Ver y controlar dispositivos de viviendas a las que está asignada
SELECT d.id_dispositivo, d.nombre_dispositivo, d.tipo, d.estado, d.ubicacion, v.nombre_vivienda
FROM Dispositivo d
JOIN Usuario_Vivienda uv ON d.id_vivienda = uv.id_vivienda
JOIN Vivienda v ON uv.id_vivienda = v.id_vivienda
WHERE uv.id_usuario = 2
ORDER BY v.nombre_vivienda, d.tipo;

-- CONSULTA PARA USUARIO: Ver su propio historial de actividad
SELECT e.fecha_hora, d.nombre_dispositivo, v.nombre_vivienda, e.tipo_evento, e.detalle
FROM EventoDispositivo e
JOIN Dispositivo d ON e.id_dispositivo = d.id_dispositivo
JOIN Vivienda v ON d.id_vivienda = v.id_vivienda
WHERE e.id_usuario = 2
ORDER BY e.fecha_hora DESC
LIMIT 20;

-- CONSULTAS PARA ADMINISTRADOR (Ej: Admin, id_usuario = 1):
-- Panel de control: ver todos los dispositivos de las viviendas que administra
SELECT v.nombre_vivienda, v.direccion, d.nombre_dispositivo, d.tipo, d.estado, d.ubicacion
FROM Vivienda v
JOIN Dispositivo d ON v.id_vivienda = d.id_vivienda
WHERE v.id_administrador = 1
ORDER BY v.nombre_vivienda, d.tipo;

-- Auditoría completa: historial de todos los eventos en sus viviendas
SELECT v.nombre_vivienda, d.nombre_dispositivo, e.tipo_evento, e.fecha_hora, u.nombre AS usuario, e.detalle
FROM Vivienda v
JOIN Dispositivo d ON v.id_vivienda = d.id_vivienda
JOIN EventoDispositivo e ON d.id_dispositivo = e.id_dispositivo
JOIN Usuario u ON e.id_usuario = u.id_usuario
WHERE v.id_administrador = 1
ORDER BY e.fecha_hora DESC;

-- CONSULTA ADMINISTRADOR: Ver usuarios asignados a cada vivienda
SELECT v.nombre_vivienda, u.nombre AS usuario, u.email
FROM Vivienda v
JOIN Usuario_Vivienda uv ON v.id_vivienda = uv.id_vivienda
JOIN Usuario u ON uv.id_usuario = u.id_usuario
WHERE v.id_administrador = 1
ORDER BY v.nombre_vivienda, u.nombre;

-- =============================================================================
-- CONSULTAS ADICIONALES DE ANÁLISIS Y REPORTES
-- =============================================================================

-- Reporte: Consumo energético aproximado (dispositivos encendidos)
SELECT v.nombre_vivienda, 
       COUNT(CASE WHEN d.estado = 'encendido' THEN 1 END) AS dispositivos_encendidos,
       COUNT(CASE WHEN d.estado = 'apagado' THEN 1 END) AS dispositivos_apagados,
       COUNT(d.id_dispositivo) AS total_dispositivos
FROM Vivienda v
LEFT JOIN Dispositivo d ON v.id_vivienda = d.id_vivienda
GROUP BY v.id_vivienda, v.nombre_vivienda
ORDER BY dispositivos_encendidos DESC;

-- Reporte: Administradores y su carga de trabajo
SELECT u.nombre AS administrador, u.email,
       COUNT(DISTINCT v.id_vivienda) AS total_viviendas,
       COUNT(DISTINCT d.id_dispositivo) AS total_dispositivos,
       COUNT(DISTINCT uv.id_usuario) AS total_usuarios_asignados
FROM Usuario u
LEFT JOIN Vivienda v ON u.id_usuario = v.id_administrador
LEFT JOIN Dispositivo d ON v.id_vivienda = d.id_vivienda
LEFT JOIN Usuario_Vivienda uv ON v.id_vivienda = uv.id_vivienda
WHERE u.rol = 'administrador'
GROUP BY u.id_usuario, u.nombre, u.email
ORDER BY total_viviendas DESC;

-- Reporte de seguridad: Estado de cámaras por vivienda
SELECT v.nombre_vivienda, d.nombre_dispositivo, d.ubicacion, d.estado
FROM Vivienda v
JOIN Dispositivo d ON v.id_vivienda = d.id_vivienda
WHERE d.tipo = 'camara'
ORDER BY v.nombre_vivienda;

-- =============================================================================
-- FIN DEL ARCHIVO DML
-- =============================================================================
