-- ==========================================================
-- CONFIGURACIÓN DEL ESQUEMA DE BASE DE DATOS
-- ==========================================================
DROP SCHEMA IF EXISTS `esquema_usuarios`;
CREATE SCHEMA IF NOT EXISTS `esquema_usuarios`
    DEFAULT CHARACTER SET utf8;

USE `esquema_usuarios`;

-- ==========================================================
-- DEFINICIÓN DE ESTRUCTURA: TABLA DE USUARIOS
-- ==========================================================
CREATE TABLE IF NOT EXISTS `usuarios` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `nombre` VARCHAR(45) NOT NULL,
    `apellido` VARCHAR(45) NOT NULL,
    `email` VARCHAR(45) NOT NULL UNIQUE,
    `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
    `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) ENGINE = InnoDB;

-- ==========================================================
-- INSERCIÓN DE REGISTROS INICIALES DE PRUEBA
-- ==========================================================
INSERT INTO usuarios (nombre, apellido, email) VALUES
("Carlos", "Mendoza", "carlos.mendoza@gmail.com"),
("María", "Gómez", "maria.gomez@gmail.com"),
("Juan", "Pérez", "juan.perez@gmail.com"),
("Ana", "Martínez", "ana.martinez@gmail.com"),
("Luis", "Hernández", "luis.hernandez@gmail.com");