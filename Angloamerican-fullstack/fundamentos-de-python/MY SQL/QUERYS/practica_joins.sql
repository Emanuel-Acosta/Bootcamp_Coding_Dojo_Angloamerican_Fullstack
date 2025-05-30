-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost
-- Tiempo de generación: 25-04-2024 a las 18:17:43
-- Versión del servidor: 10.4.21-MariaDB
-- Versión de PHP: 7.4.27

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `practica_joins`
--
CREATE DATABASE IF NOT EXISTS `practica_joins` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `practica_joins`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `id` int(11) NOT NULL,
  `nombre` varchar(25) NOT NULL,
  `apellido` varchar(25) NOT NULL,
  `email` varchar(50) NOT NULL,
  `created_at` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`id`, `nombre`, `apellido`, `email`, `created_at`) VALUES
(1, 'Michael', 'Choi', 'mchoi@village88.com', '2010-04-05 14:09:08'),
(2, 'Joe', 'Smith', 'joe@village88.com', '2010-04-14 14:10:09'),
(3, 'Ryan', 'Owen', 'rowen@village88.com', '2011-02-09 14:10:29'),
(4, 'Masaki', 'Fujimuto', 'mfujimuto@village88.com', '2011-04-28 18:16:29'),
(5, 'Diana', 'Sue Manlulu', 'dmanlulu@village88.com', '2011-05-23 17:33:20'),
(6, 'John', 'Supsupin', 'jsupsupin@village88.com', '2011-05-29 19:23:33'),
(7, 'Toni Rose', 'Panganiban', 'tpanganiban@village88.com', '2011-06-01 01:02:03'),
(8, 'Maria', 'Gonzales', 'mgonzales@village88.com', '2011-08-09 01:22:33'),
(9, 'Tom', 'Owen', 'towen@village88.com', '2011-08-22 16:33:23'),
(10, 'Roosevelt', 'Sebial', 'rsebial@village88.com', '2011-09-01 17:18:09');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cobranza`
--

CREATE TABLE `cobranza` (
  `id` int(11) NOT NULL,
  `monto` float NOT NULL,
  `fechahora_cobro` datetime NOT NULL,
  `cliente_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `cobranza`
--

INSERT INTO `cobranza` (`id`, `monto`, `fechahora_cobro`, `cliente_id`) VALUES
(1, 300, '2011-01-01 14:50:25', 1),
(2, 500, '2011-01-15 14:50:25', 3),
(3, 500, '2011-02-11 14:50:25', 5),
(4, 1200, '2011-02-22 14:50:25', 7),
(5, 2500, '2011-02-27 14:50:25', 9),
(6, 500, '2011-03-06 14:50:25', 10),
(7, 1000, '2011-03-13 14:50:25', 8),
(8, 200, '2011-04-02 14:50:25', 4),
(9, 5000, '2011-04-06 14:50:25', 1),
(10, 1000, '2011-04-11 14:50:25', 2),
(11, 500, '2011-05-08 15:55:32', 6),
(12, 750, '2011-06-18 13:22:09', 6),
(13, 100, '2011-07-19 13:22:09', 8),
(14, 800, '2011-06-21 13:22:09', 4),
(15, 900, '2011-06-22 13:22:09', 2),
(16, 5200, '2011-07-02 13:22:09', 3),
(17, 650, '2011-08-24 13:22:09', 4),
(18, 450, '2011-09-16 13:22:09', 1),
(19, 2500, '2011-10-18 13:22:09', 1),
(20, 3600, '2012-01-03 13:22:09', 2),
(21, 8000, '2012-02-05 13:22:09', 8),
(22, 640, '2012-03-07 13:22:09', 7),
(23, 150, '2012-04-08 13:22:09', 9),
(24, 680, '2012-04-02 13:22:09', 10),
(25, 1200, '2012-05-09 13:22:09', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prospectos`
--

CREATE TABLE `prospectos` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `fechahora_registro` datetime NOT NULL,
  `email` varchar(50) NOT NULL,
  `sitio_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `prospectos`
--

INSERT INTO `prospectos` (`id`, `nombre`, `apellido`, `fechahora_registro`, `email`, `sitio_id`) VALUES
(1, 'Art', 'Lopez', '2011-01-13 14:22:58', 'artlopez@gmail.com', 1),
(2, 'Arthur', 'Kesh', '2011-01-01 02:03:03', 'arthurkesh@gmail', 3),
(3, 'Alison', 'Follosco', '2011-02-11 02:03:03', 'alison@gmail.com', 5),
(4, 'Joyce', 'Jamon', '2011-03-21 02:03:03', 'joycejamon@gmail.com', 15),
(5, 'Angel', 'Supsupin', '2011-03-22 02:03:03', 'angel999@gmail.com', 16),
(6, 'Dave', 'Supsupin', '2011-04-06 02:03:03', 'dave999@gmail.com', 2),
(7, 'Mark', 'Jaramilla', '2011-05-03 02:03:03', 'markjams@gmail.com', 13),
(8, 'Chris', 'Chun', '2011-05-22 02:03:03', 'chrischun@gmail.com', 12),
(9, 'Ben', 'Lee', '2011-05-27 02:03:03', 'benlee@gmail.com', 22),
(10, 'Jeric', 'Follosco', '2011-06-03 02:03:03', 'jfollosco@gamil.com', 23),
(11, 'James', 'Jones', '2011-07-06 02:03:03', 'jamesjones@gmail.com', 23),
(12, 'Jay', 'Smith', '2011-08-07 02:03:03', 'jsmith@gmail.com', 25),
(13, 'Henry', 'Mendoza', '2011-08-13 02:03:03', 'henrymen@gmail.com', 9),
(14, 'Dian', 'Morales', '2011-09-22 02:03:03', 'dianmorales@gmail.com', 6),
(15, 'Lina', 'Inverse', '2011-10-09 02:03:03', 'linainverse@yahoo.com', 7),
(16, 'May Joy', 'Sagon', '2011-11-14 02:03:03', 'mjsagon@yahoo.com', 1),
(17, 'April', 'Sean', '2011-11-22 02:03:03', 'asean@gmail.com', 1),
(18, 'Philip', 'Morres', '2011-12-19 02:03:03', 'philipm@yahoo.com', 13),
(19, 'Kimemura', 'Lau', '2012-01-04 02:03:03', 'klau@gmail.com', 17),
(20, 'Noname', 'Sabado', '2012-02-01 02:03:03', 'nonamesabado@yahoo.com', 18),
(21, 'Gilbert', 'Hufana', '2012-02-14 02:03:03', 'ghufana@gmail.com', 19),
(22, 'Paulito', 'Nisperos', '2012-03-16 02:03:03', 'pcnisperos@yahoo.com', 20),
(23, 'Joseph', 'Padua', '2012-03-17 02:03:03', 'jpadua@gmail.com', 2),
(24, 'Marylen', 'Rodriguez', '2012-03-18 02:03:03', 'mrodriguez@gmail.com', 3),
(25, 'Bala', 'Nar', '2012-04-27 02:03:03', 'balanar@gmail.com', 4),
(26, 'Steve', 'Nash', '2012-05-16 02:03:03', 'stevenash@nash.com', 5),
(27, 'Lebron', 'James', '2012-06-11 02:03:03', 'lebronjames@nba.com', 6),
(28, 'Alvin', 'Rosorio', '2012-06-22 02:03:03', 'alvinr@gmail.com', 7),
(29, 'Kirk', 'David', '2012-07-19 02:03:03', 'kirkdavid@hotmail.com', 8),
(30, 'Calvin', 'Klein', '2013-07-08 02:03:03', 'ck999@yahoo.com', 9),
(31, 'Albert', 'Martinez', '2013-01-05 02:03:03', 'albretmart@gmail.com', 10),
(32, 'Vhong', 'Navarro', '2013-02-01 02:03:03', 'vhong@showtime.com', 22),
(33, 'Anne', 'Curtiz', '2013-03-07 02:03:03', 'anne@showtime.com', 1),
(34, 'Mark', 'Oceana', '2013-04-21 02:03:03', 'markoceana@gmail.com', 24),
(35, 'Ems', 'Faraj', '2013-05-22 02:03:03', 'emsfaraj@gmail.com', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `sitios`
--

CREATE TABLE `sitios` (
  `id` int(11) NOT NULL,
  `dominio` varchar(100) NOT NULL,
  `created_at` datetime NOT NULL,
  `cliente_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `sitios`
--

INSERT INTO `sitios` (`id`, `dominio`, `created_at`, `cliente_id`) VALUES
(1, 'market.com', '2010-11-05 14:14:26', 1),
(2, 'searchhomes.com', '2011-01-01 14:14:26', 3),
(3, 'ehow.com', '2011-01-05 14:14:45', 5),
(4, 'searchcoronado.com', '2011-01-05 14:14:45', 7),
(5, 'searchphilippines.com', '2011-02-08 14:14:26', 9),
(6, 'fox.com', '2011-02-08 14:14:26', 2),
(7, 'loans.com', '2011-02-15 14:14:45', 4),
(8, 'searchvillage.com', '2011-03-13 14:11:30', 6),
(9, 'homes.com', '2011-03-15 14:14:45', 8),
(10, 'searchcomputers.com', '2011-04-20 14:11:49', 10),
(11, 'youtube.com', '2011-04-28 11:12:33', 1),
(12, 'help.com', '2011-05-01 12:16:33', 4),
(13, 'timespace.com', '2011-06-03 08:05:33', 7),
(14, 'flipfly.com', '2011-06-23 11:12:33', 2),
(15, 'uptownzone.com', '2011-05-29 12:12:33', 6),
(16, 'olx.com', '2011-06-01 07:22:16', 5),
(17, 'cryshinjohn.com', '2011-06-06 04:03:16', 4),
(18, 'family.com', '2011-06-15 05:10:11', 3),
(19, 'connectme.com', '2011-07-29 10:03:21', 2),
(20, 'yestogod.com', '2011-07-06 04:03:16', 9),
(21, 'warcraft.com', '2011-08-06 14:03:16', 8),
(22, 'keepvid.com', '2011-08-13 16:03:16', 6),
(23, 'atech.com', '2011-09-01 03:06:17', 7),
(24, 'assignmentworld.com', '2011-09-05 02:02:12', 1),
(25, 'finalsite.com', '2011-09-07 11:02:16', 3);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `cobranza`
--
ALTER TABLE `cobranza`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_billing_clients1_idx` (`cliente_id`);

--
-- Indices de la tabla `prospectos`
--
ALTER TABLE `prospectos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_leads_sites1_idx` (`sitio_id`);

--
-- Indices de la tabla `sitios`
--
ALTER TABLE `sitios`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_sites_clients_idx` (`cliente_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `cobranza`
--
ALTER TABLE `cobranza`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT de la tabla `prospectos`
--
ALTER TABLE `prospectos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT de la tabla `sitios`
--
ALTER TABLE `sitios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `cobranza`
--
ALTER TABLE `cobranza`
  ADD CONSTRAINT `fk_billing_clients1` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `prospectos`
--
ALTER TABLE `prospectos`
  ADD CONSTRAINT `fk_leads_sites1` FOREIGN KEY (`sitio_id`) REFERENCES `sitios` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `sitios`
--
ALTER TABLE `sitios`
  ADD CONSTRAINT `fk_sites_clients` FOREIGN KEY (`cliente_id`) REFERENCES `clientes` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
