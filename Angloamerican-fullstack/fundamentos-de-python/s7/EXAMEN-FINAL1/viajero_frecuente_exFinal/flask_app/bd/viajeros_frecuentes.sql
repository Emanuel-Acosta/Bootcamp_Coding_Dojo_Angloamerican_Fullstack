-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema viajeros_frecuentes
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema viajeros_frecuentes
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `viajeros_frecuentes` DEFAULT CHARACTER SET utf8mb3 ;
USE `viajeros_frecuentes` ;

-- -----------------------------------------------------
-- Table `viajeros_frecuentes`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `viajeros_frecuentes`.`usuarios` (
  `id_usuario` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL DEFAULT NULL,
  `apellido` VARCHAR(45) NULL DEFAULT NULL,
  `email` VARCHAR(45) NULL DEFAULT NULL,
  `password` VARCHAR(255) NULL DEFAULT NULL,
  `fecha_creacion` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id_usuario`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `viajeros_frecuentes`.`viajes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `viajeros_frecuentes`.`viajes` (
  `id_viaje` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(100) NULL DEFAULT NULL,
  `fecha_inicio` TIMESTAMP NULL DEFAULT NULL,
  `fecha_de_fin` TIMESTAMP NULL DEFAULT NULL,
  `itinerario` TEXT NULL DEFAULT NULL,
  `fecha_creacion` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
  `fecha_actualizacion` TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `id_organizador` INT NOT NULL,
  PRIMARY KEY (`id_viaje`),
  INDEX `fk_viajes_usuarios1_idx` (`id_organizador` ASC) VISIBLE,
  CONSTRAINT `fk_viajes_usuarios1`
    FOREIGN KEY (`id_organizador`)
    REFERENCES `viajeros_frecuentes`.`usuarios` (`id_usuario`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `viajeros_frecuentes`.`viajeros`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `viajeros_frecuentes`.`viajeros` (
  `usuario_id` INT NOT NULL,
  `viaje_id` INT NOT NULL,
  PRIMARY KEY (`usuario_id`, `viaje_id`),
  INDEX `fk_usuarios_has_viajes_viajes1_idx` (`viaje_id` ASC) VISIBLE,
  INDEX `fk_usuarios_has_viajes_usuarios_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_usuarios_has_viajes_usuarios`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `viajeros_frecuentes`.`usuarios` (`id_usuario`),
  CONSTRAINT `fk_usuarios_has_viajes_viajes1`
    FOREIGN KEY (`viaje_id`)
    REFERENCES `viajeros_frecuentes`.`viajes` (`id_viaje`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
