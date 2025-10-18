-- =============================================================================
-- DDL SIMPLIFICADO - Sistema SmartHome con 2 Roles
-- Base de datos para sistema domótico con usuarios y dispositivos básicos
-- =============================================================================

-- Crear la base de datos principal
CREATE DATABASE IF NOT EXISTS smarthome;
USE smarthome;

-- Tabla de usuarios: almacena información de administradores y usuarios normales
CREATE TABLE Usuario (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,      -- ID numérico como clave primaria
    email VARCHAR(100) NOT NULL UNIQUE,       -- Email como identificador único de login
    nombre VARCHAR(100) NOT NULL,             -- Nombre completo del usuario
    contraseña VARCHAR(100) NOT NULL,         -- Contraseña encriptada
    rol ENUM('administrador', 'usuario') DEFAULT 'usuario', -- Solo 2 roles
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP,      -- Fecha de creación
    activo BOOLEAN DEFAULT TRUE               -- Estado del usuario
);

-- Tabla de viviendas: representa las casas/apartamentos en el sistema
CREATE TABLE Vivienda (
    id_vivienda INT AUTO_INCREMENT PRIMARY KEY, -- ID único de la vivienda
    nombre_vivienda VARCHAR(100) NOT NULL,       -- Nombre descriptivo
    direccion VARCHAR(200),                      -- Dirección física
    id_administrador INT NOT NULL,               -- Quien administra la vivienda
    activa BOOLEAN DEFAULT TRUE,                 -- Estado de la vivienda
    FOREIGN KEY (id_administrador) REFERENCES Usuario(id_usuario)
);

-- Tabla de dispositivos: almacena todos los dispositivos IoT de las viviendas
CREATE TABLE Dispositivo (
    id_dispositivo INT AUTO_INCREMENT PRIMARY KEY, -- ID único del dispositivo
    nombre_dispositivo VARCHAR(100) NOT NULL,       -- Nombre descriptivo
    tipo ENUM('luz', 'sensor', 'camara') NOT NULL, -- Solo 3 tipos básicos
    estado ENUM('encendido', 'apagado') DEFAULT 'apagado', -- Estado actual
    ubicacion VARCHAR(100),                         -- Ubicación en la vivienda
    id_vivienda INT NOT NULL,                       -- A qué vivienda pertenece
    FOREIGN KEY (id_vivienda) REFERENCES Vivienda(id_vivienda)
);

-- Tabla de eventos: registra todas las acciones realizadas en los dispositivos
CREATE TABLE EventoDispositivo (
    id_evento INT AUTO_INCREMENT PRIMARY KEY,      -- ID único del evento
    id_dispositivo INT NOT NULL,                   -- Qué dispositivo fue afectado
    id_usuario INT NOT NULL,                       -- Quién realizó la acción
    tipo_evento ENUM('encendido', 'apagado', 'configuracion') NOT NULL, -- Tipo de acción
    fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP, -- Cuándo ocurrió
    detalle VARCHAR(200),                          -- Descripción adicional
    FOREIGN KEY (id_dispositivo) REFERENCES Dispositivo(id_dispositivo),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario)
);

-- Tabla de asignación: permite asignar usuarios normales a viviendas (relación N:M)
CREATE TABLE Usuario_Vivienda (
    id_usuario INT NOT NULL,
    id_vivienda INT NOT NULL,
    PRIMARY KEY (id_usuario, id_vivienda),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (id_vivienda) REFERENCES Vivienda(id_vivienda)
);

-- Índices para mejorar el rendimiento de las consultas más frecuentes
CREATE INDEX idx_dispositivo_vivienda ON Dispositivo(id_vivienda);  -- Buscar por vivienda
CREATE INDEX idx_dispositivo_tipo ON Dispositivo(tipo);             -- Buscar por tipo
CREATE INDEX idx_evento_dispositivo ON EventoDispositivo(id_dispositivo); -- Historial
CREATE INDEX idx_usuario_rol ON Usuario(rol);                       -- Filtrar por rol

-- =============================================================================
-- PERMISOS POR ROL
-- =============================================================================

-- ADMINISTRADOR puede:
-- - Crear, modificar y eliminar viviendas
-- - Gestionar todos los dispositivos de sus viviendas
-- - Ver todos los eventos de sus viviendas
-- - Agregar/quitar usuarios a sus viviendas

-- USUARIO puede:
-- - Ver dispositivos de sus viviendas asignadas
-- - Controlar dispositivos (encender/apagar)
-- - Ver historial de sus propias acciones
