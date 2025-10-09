-- =============================================================================
-- DML SIMPLIFICADO - Sistema SmartHome con 2 Roles
-- Consultas para manipular datos: insertar, consultar, actualizar y eliminar
-- =============================================================================

-- -----------------------------------------------------------------------------
-- INSERT: Insertar datos de prueba en todas las tablas
-- -----------------------------------------------------------------------------

-- 1) Crear usuarios del sistema: un administrador y un usuario normal
INSERT INTO Usuario (id_usuario, email, nombre, contraseña, rol) VALUES 
(1, 'admin@smarthome.com', 'Administrador Principal', 'admin123', 'administrador'),
(2, 'ana@mail.com', 'Ana García Pérez', 'user123', 'usuario');

-- 2) Crear una vivienda en el sistema administrada por el admin
INSERT INTO Vivienda (id_vivienda, nombre_vivienda, direccion, id_administrador) VALUES 
(1, 'Casa de Ana', 'Av. Falsa 123', 1);

-- 3) Asignar la vivienda a la usuaria Ana
INSERT INTO Usuario_Vivienda (id_usuario, id_vivienda) VALUES
(2, 1);

-- 4) Instalar dispositivos IoT en la vivienda de Ana
INSERT INTO Dispositivo (id_dispositivo, nombre_dispositivo, tipo, estado, ubicacion, id_vivienda) VALUES 
-- Dispositivos para Casa de Ana (ID: 1)
(1, 'Luz Sala', 'luz', 'apagado', 'Sala Principal', 1),
(2, 'Sensor Temperatura', 'sensor', 'encendido', 'Cocina', 1),
(3, 'Cámara Entrada', 'camara', 'encendido', 'Puerta Principal', 1);

-- 5) Registrar actividad inicial: eventos de configuración y uso de dispositivos
INSERT INTO EventoDispositivo (id_dispositivo, id_usuario, tipo_evento, detalle) VALUES 
(1, 2, 'encendido', 'Usuario encendió luz de sala'),
(2, 1, 'configuracion', 'Configuración inicial del sensor'),
(3, 1, 'encendido', 'Activación de cámara de seguridad');

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

-- -----------------------------------------------------------------------------
-- UPDATE: Modificar datos existentes en el sistema
-- -----------------------------------------------------------------------------

-- 1) Control de dispositivos: cambiar estado de encendido/apagado (usuarios normales)
UPDATE Dispositivo 
SET estado = 'encendido' 
WHERE id_dispositivo = 1 AND tipo = 'luz';

-- 2) Actualizar información personal de usuarios (solo administradores)
UPDATE Usuario 
SET nombre = 'Ana G. Pérez' 
WHERE email = 'ana@mail.com';

-- 3) Cambiar responsable de una vivienda (solo administradores principales)
-- (Esta lógica ya no aplica directamente, se gestiona por la tabla Usuario_Vivienda)

-- -----------------------------------------------------------------------------
-- DELETE: Eliminar datos del sistema (solo administradores)
-- -----------------------------------------------------------------------------

-- 1) Mantenimiento: eliminar eventos antiguos para liberar espacio
DELETE FROM EventoDispositivo 
WHERE fecha_hora < DATE_SUB(NOW(), INTERVAL 90 DAY);

-- 2) Gestión de usuarios: desactivar cuenta sin eliminar historial
UPDATE Usuario 
SET activo = FALSE 
WHERE email = 'ana@mail.com';

-- 3) Eliminación completa: remover dispositivo y todo su historial
DELETE FROM EventoDispositivo WHERE id_dispositivo = 3; -- Primero el historial
DELETE FROM Dispositivo WHERE id_dispositivo = 3;       -- Luego el dispositivo

-- =============================================================================
-- CONSULTAS ESPECÍFICAS SEGÚN EL ROL DEL USUARIO
-- =============================================================================

-- CONSULTA PARA USUARIO NORMAL (Ana, id_usuario = 2):
-- Ver y controlar dispositivos de viviendas a las que está asignada
SELECT d.nombre_dispositivo, d.tipo, d.estado, d.ubicacion
FROM Dispositivo d
JOIN Usuario_Vivienda uv ON d.id_vivienda = uv.id_vivienda
WHERE uv.id_usuario = 2;


-- CONSULTAS PARA ADMINISTRADOR (Admin, id_usuario = 1):
-- Panel de control: ver todos los dispositivos de las viviendas que administra
SELECT v.nombre_vivienda, d.nombre_dispositivo, d.tipo, d.estado
FROM Vivienda v
JOIN Dispositivo d ON v.id_vivienda = d.id_vivienda
WHERE v.id_administrador = 1;

-- Auditoría completa: historial de todos los eventos en sus viviendas
SELECT v.nombre_vivienda, d.nombre_dispositivo, e.tipo_evento, e.fecha_hora, u.nombre AS usuario
FROM Vivienda v
JOIN Dispositivo d ON v.id_vivienda = d.id_vivienda
JOIN EventoDispositivo e ON d.id_dispositivo = e.id_dispositivo
JOIN Usuario u ON e.id_usuario = u.id_usuario
WHERE v.id_administrador = 1
ORDER BY e.fecha_hora DESC;


