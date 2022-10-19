-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-10-2022 a las 23:13:32
-- Versión del servidor: 10.4.18-MariaDB
-- Versión de PHP: 7.4.16

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `practicasql1b`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `id_cliente` int(10) NOT NULL,
  `nombre_cliente` varchar(40) DEFAULT NULL,
  `fecha_nacimiento` varchar(27) DEFAULT NULL,
  `direccion` varchar(30) DEFAULT NULL,
  `localidad` varchar(20) NOT NULL,
  `telefono` varchar(23) DEFAULT NULL,
  `email` varchar(23) DEFAULT NULL,
  `fecha_alta` varchar(17) DEFAULT NULL,
  `grupo_clientes` varchar(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`id_cliente`, `nombre_cliente`, `fecha_nacimiento`, `direccion`, `localidad`, `telefono`, `email`, `fecha_alta`, `grupo_clientes`) VALUES
(1, 'Pepe Sanchez', '01/01/200', 'Paunero y Almirante Brown', 'Sa Rafael', '4054545', 'pepesanchez@gmail.com', '12/10/22', 'A'),
(2, 'Galver', '01/01/2000', 'San Martin y Mitre', 'San Rafael', '555555', 'galver@gmail.com', '12/10/22', 'B'),
(3, 'Nina', '01/01/2000', 'San Martin y Olascaga', 'San Rafael', '444444', 'nina@gmail.com', '12/10/22', 'A'),
(5, 'A go go', '01/01/98', 'Chile y San Matin', 'San Rafael', '666 666', 'agogo@gmail.com', '19/10/22', 'a'),
(6, 'Galver', '01/01/2001', 'Mitre y San Martin', 'San Rafael', '222 222', 'galver@gmail.com', '19/10/22', 'B');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`id_cliente`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `id_cliente` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
