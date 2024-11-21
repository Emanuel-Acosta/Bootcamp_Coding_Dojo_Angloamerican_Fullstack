CREATE DATABASE  IF NOT EXISTS `x` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `x`;
-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: x
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `favoritos`
--

DROP TABLE IF EXISTS `favoritos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `favoritos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuario_id` int NOT NULL,
  `tweet_id` int NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_faves_users1_idx` (`usuario_id`),
  KEY `fk_faves_tweets1_idx` (`tweet_id`),
  CONSTRAINT `fk_faves_tweets1` FOREIGN KEY (`tweet_id`) REFERENCES `tweets` (`id`),
  CONSTRAINT `fk_faves_users1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favoritos`
--

LOCK TABLES `favoritos` WRITE;
/*!40000 ALTER TABLE `favoritos` DISABLE KEYS */;
INSERT INTO `favoritos` VALUES (1,2,1,'2010-02-01 00:00:01','2010-02-01 00:00:01'),(2,2,2,'2010-02-01 00:00:01','2010-02-01 00:00:01'),(3,3,4,'2010-02-01 00:00:01','2010-02-01 00:00:01'),(4,4,3,'2010-02-01 00:00:01','2010-02-01 00:00:01'),(5,1,9,'2010-02-01 00:00:01','2010-02-01 00:00:01'),(6,1,10,'2010-02-01 00:00:01','2010-02-01 00:00:01'),(7,1,11,'2010-02-01 00:00:01','2010-02-01 00:00:01');
/*!40000 ALTER TABLE `favoritos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `seguidores`
--

DROP TABLE IF EXISTS `seguidores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `seguidores` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuario_id` int NOT NULL,
  `seguidor_id` int DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_follows_users_idx` (`usuario_id`),
  CONSTRAINT `fk_follows_users` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `seguidores`
--

LOCK TABLES `seguidores` WRITE;
/*!40000 ALTER TABLE `seguidores` DISABLE KEYS */;
INSERT INTO `seguidores` VALUES (1,1,2,'2010-02-01 00:00:01','2010-02-01 00:00:01'),(2,1,3,'2010-02-01 00:00:01','2010-02-01 00:00:01'),(3,1,4,'2010-02-01 00:00:01','2010-02-01 00:00:01'),(4,1,5,'2010-02-01 00:00:01','2010-02-01 00:00:01'),(5,3,4,'2010-02-01 00:00:01','2010-02-01 00:00:01'),(6,3,5,'2010-02-01 00:00:01','2010-02-01 00:00:01'),(7,2,4,'2010-02-01 00:00:01','2010-02-01 00:00:01');
/*!40000 ALTER TABLE `seguidores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tweets`
--

DROP TABLE IF EXISTS `tweets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tweets` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tweet` varchar(140) DEFAULT NULL,
  `usuario_id` int NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_tweets_users1_idx` (`usuario_id`),
  CONSTRAINT `fk_tweets_users1` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tweets`
--

LOCK TABLES `tweets` WRITE;
/*!40000 ALTER TABLE `tweets` DISABLE KEYS */;
INSERT INTO `tweets` VALUES (1,'Hay poder en comprender el viaje de los demás para ayudar a crear el propio.',1,'2002-02-01 00:00:01','2002-02-01 00:00:01'),(2,'¡Felicidades, Coach K! Logro increíble #1KparaCoachK #Duke',1,'2005-02-01 00:00:01','2005-02-01 00:00:01'),(3,'Esto es lo que sucede cuando paso demasiado. #HombroEnShock Gracias a todos por sus oraciones. #equipo @DrinkBODYARMOR @Lakers #oneluv',1,'2004-02-01 00:00:01','2004-02-01 00:00:01'),(4,'Siento una mezcla de emociones que no he sentido en 18 años como profesional. #viaje #19a',1,'2012-02-01 00:00:01','2012-02-01 00:00:01'),(5,'Gracias a todos por los buenos deseos de cumpleaños. Los aprecio mucho.',2,'2011-02-01 00:00:01','2011-02-01 00:00:01'),(6,'Me gustaría desear a todos una muy Feliz Navidad. Mucho amor para todos. Cuídense.',2,'2009-02-01 00:00:01','2009-02-01 00:00:01'),(7,'Gracias a todos los que ayudaron con las canastas de comida de Navidad hoy. Su tiempo es muy apreciado. ¡Amor y respeto!',2,'2008-02-01 00:00:01','2008-02-01 00:00:01'),(8,'Acepté el desafío ALS de Monta Ellis. Desafío a @coolkesh42 Jameer Nelson, Dionne Calhoun ...',2,'2003-02-01 00:00:01','2003-02-01 00:00:01'),(9,'¡Bien hecho, hermanito, te lo mereces! @KingJames',3,'2006-02-01 00:00:01','2006-02-01 00:00:01'),(10,'Para la clínica de baloncesto con @manilacone el 4/11/14, aún hay algunos lugares para el juego. Nos vemos el 5/11/14 en Filipinas.',3,'2001-02-01 00:00:01','2001-02-01 00:00:01'),(11,'Siempre la paso genial con mi hermanito mayor.',4,'2011-02-01 00:00:01','2011-02-01 00:00:01'),(12,'¡Feliz Día del Trabajo!',4,'2014-02-01 00:00:01','2014-02-01 00:00:01'),(13,'hola este es un nuevo tweets',1,NULL,NULL);
/*!40000 ALTER TABLE `tweets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) DEFAULT NULL,
  `apellido` varchar(255) DEFAULT NULL,
  `nombre_usuario` varchar(255) DEFAULT NULL,
  `fecha_nacimiento` date DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Kobe','Bryant','kobebryant','1978-08-23','2010-02-01 00:00:01','2011-07-01 00:00:01'),(2,'Vince','Carter','mrvincecarter15','1977-01-26','2007-08-11 00:00:01','2010-01-01 00:00:01'),(3,'Allen','Iverson','alleniverson','1975-06-07','2005-09-01 00:00:01','2011-04-21 00:00:01'),(4,'Tracy','McGrady','Real_T_Mac','1979-05-24','2002-12-01 00:00:01','2005-11-21 00:00:01'),(5,'Rajon','Rondo','RajonRondo','1986-02-22','2001-02-01 00:00:01','2002-01-01 00:00:01');
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-15 12:50:47
