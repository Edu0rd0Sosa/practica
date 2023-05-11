-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-05-2023 a las 23:30:43
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `escuela`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alumnos`
--

CREATE TABLE `alumnos` (
  `id` int(10) NOT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `edad` int(11) DEFAULT NULL,
  `email` varchar(10) DEFAULT NULL,
  `curp` varchar(255) DEFAULT NULL,
  `matricula` int(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `alumnos`
--

INSERT INTO `alumnos` (`id`, `nombre`, `edad`, `email`, `curp`, `matricula`) VALUES
(16, '', 0, '', '', 0),
(17, 'fd', 0, 'sd', 'd', 0),
(19, 'sdfdsf', 0, 'sdsdf@gmai', 'dsffssdf', 0),
(20, '', 0, '', '', 0),
(21, 'Sosa vera', 14, 'a@gisk.pom', 'cuasbeh323557dsa', 4220054),
(22, '', 0, '', '', 0),
(23, '34', 34, '43', '4334', 4343),
(24, 'sosa', 19, 'mynamesoa@', 'wqdasdc12sd2', 4220054),
(25, 'efc', 12, 'ssaddfcv@h', 'dsfdsf', 90),
(26, 'afsd', 12, 'zvzx', '12fdvs', 123424),
(27, 'asfasf', 21, 'aasasffa@h', 'safsagt4w35efs', 102),
(28, 'soasas', 12222, 'asdasdsa@g', 'asiocoiuassss', 4220054),
(29, 'safasfa', 999, 'sasfaasf@a', '0asidjncnusc', 938830492);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `alumnos`
--
ALTER TABLE `alumnos`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `alumnos`
--
ALTER TABLE `alumnos`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
