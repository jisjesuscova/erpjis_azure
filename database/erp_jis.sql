-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 21-11-2022 a las 19:48:38
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
-- Base de datos: `erp_jis`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `abandon_day_documents`
--

CREATE TABLE `abandon_day_documents` (
  `id` int(11) NOT NULL,
  `document_employee_id` int(255) NOT NULL,
  `abandon_date` datetime NOT NULL,
  `added_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `abandon_day_documents`
--

INSERT INTO `abandon_day_documents` (`id`, `document_employee_id`, `abandon_date`, `added_date`) VALUES
(1, 17, '2022-11-15 00:00:00', '2022-11-15 15:43:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('f327aaed7a02');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `audits`
--

CREATE TABLE `audits` (
  `id` int(11) NOT NULL,
  `affected_rut` varchar(255) DEFAULT NULL,
  `model` varchar(255) DEFAULT NULL,
  `rut` varchar(150) DEFAULT NULL,
  `added_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `audits`
--

INSERT INTO `audits` (`id`, `affected_rut`, `model`, `rut`, `added_date`) VALUES
(22, '18456789', 'personal_data/store', '123456', '2022-11-17 11:46:11'),
(23, '18456789', 'personal_data/store', '123456', '2022-11-17 11:52:06'),
(24, '18456789', 'personal_data/store', '123456', '2022-11-21 07:53:57'),
(25, '18456789', 'personal_data/store', '123456', '2022-11-21 07:54:13'),
(26, '18456789', 'personal_data/store', '123456', '2022-11-21 08:05:02'),
(27, '18456789', 'personal_data/store', '123456', '2022-11-21 08:05:28'),
(28, '18456789', 'personal_data/store', '123456', '2022-11-21 08:06:16'),
(29, '18456789', 'personal_data/store', '123456', '2022-11-21 08:06:50'),
(30, '18456789', 'personal_data/store', '123456', '2022-11-21 08:07:36');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `branch_offices`
--

CREATE TABLE `branch_offices` (
  `id` int(11) NOT NULL,
  `branch_office` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `region_id` int(11) DEFAULT NULL,
  `commune_id` int(11) DEFAULT NULL,
  `segment_id` int(11) DEFAULT NULL,
  `zone_id` int(11) DEFAULT NULL,
  `principal_id` int(11) DEFAULT NULL,
  `supervisor_id` int(11) DEFAULT NULL,
  `status_id` int(11) DEFAULT NULL,
  `visibility_id` int(11) DEFAULT NULL,
  `opening_date` int(11) DEFAULT NULL,
  `dte_code` int(11) DEFAULT NULL,
  `added_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `branch_offices`
--

INSERT INTO `branch_offices` (`id`, `branch_office`, `address`, `region_id`, `commune_id`, `segment_id`, `zone_id`, `principal_id`, `supervisor_id`, `status_id`, `visibility_id`, `opening_date`, `dte_code`, `added_date`, `updated_date`) VALUES
(1, 'UNIMARC EL PAMPINO', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(2, 'UNIMARC EL PARQUE', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(3, 'BALMACEDA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(4, 'COPIAPO', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(5, 'UNIMARC LA SERENA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(6, 'UNIMARC OVALLE', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(7, 'UNIMARC QUILLOTA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(8, 'STA ISABEL REÑACA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(9, 'STA ISABEL LOS CARRERAS', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(10, 'STA ISABEL VALPARAISO', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(11, 'STA ISABEL CLAUDIO VICUÑA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(13, 'VALPARAISO', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(14, 'MALL PASEO DEL VALLE', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(15, 'UNIMARC VIÑA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(16, 'ALVI MAIPU', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(17, 'UNIMARC FCO. BILBAO', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(18, 'HITES PUENTE', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(19, 'UNIMARC LOS MILITARES', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(20, 'MEDS MAIPU', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(21, 'SODIMAC ÑUBLE', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(22, 'TOTTUS NATANIEL', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(23, 'TOTTUS SAN BERNARDO', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(24, 'TOTTUS VICUÑA MACKENNA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(25, 'UNIMARC VICENTE VALDES', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(26, 'UNIMARC CHILLAN', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(27, 'UNIMARC OSORNO', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(29, 'UNIMARC CONCEPCION', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(30, 'UNIMARC BORIES', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(31, 'UNIMARC LAUTARO', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(32, 'UNIMARC LINARES', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(33, 'EL MUSEO', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(34, 'MALL CENTRO', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(35, 'MALL MELIPILLA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(36, 'MALL QUILIN', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(37, 'MALL RANCAGUA\r\n', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(38, 'MALL SAN BERNARDO', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(39, 'MALL SAN FERNANDO', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(40, 'TOTTUS QUILLOTA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(41, 'TOTTUS CATEDRAL', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(42, 'UNIV AUTONOMA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(43, 'M10 VILLA ALEMANA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(44, 'SODIMAC IQUIQUE', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(45, 'STRIP RECOLETA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(46, 'CLINICA AUTONOMA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(48, 'TOTTUS VIVACETA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(49, 'TOTTUS RENGO', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(50, 'TOTTUS TALAGANTE', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(51, 'SODIMAC LA FLORIDA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(52, 'HITES TALCA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(53, 'COPIAPO HENRIQUEZ', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(54, 'STA ISABEL VILLA ALEMANA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(55, 'TOTTUS SAN BERNARDO ESTACION', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(56, 'STRIP IRARRAZAVAL', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(57, 'STA ISABEL HUERFANOS', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(58, 'TOTTUS SAN FERNARDO', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(60, 'PAJARITOS 3030', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(61, 'STRIP REÑACA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(62, 'UNIMARC VICUÑA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(65, 'LIDER OSORNO', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(68, 'TOTTUS LA CISTERNA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(69, 'LIDER PUERTO MONTT', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(70, 'LIDER PUERTO VARAS', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(71, 'MORANDE 801', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(72, 'MALL COQUIMBO', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(74, 'STA ISABEL LOS ANGELES', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(75, 'SITIO ESPAÑA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(76, 'LIDER TALAGANTE', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(78, 'EDIFICIO BANCOESTADO', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(79, 'LIDER VALDIVIA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(80, 'OFICINA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(81, 'STA ISABEL VIÑA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(83, 'STA ISABEL CONCEPCION', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(84, 'STA ISABEL VICUÃ‘A MACKENNA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(85, 'LIDER ARTIGAS', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(86, 'UNIMARC TANGUE', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(87, 'Almacen', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL),
(88, 'CASABLANCA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(89, 'LIDER GRAN AVENIDA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(90, 'LIDER RANCAGUA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(91, 'Venta de Insumos', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL),
(92, 'LIDER LIMACHE', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(93, 'LIDER OVALLE', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(94, 'TRANSPORTE INZUNZA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(95, 'Ajuste COQUIMBO', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, NULL, NULL, NULL, NULL),
(96, 'LIDER TOBALABA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(97, 'UNIV BERNARDO OHIGGINS', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(99, 'LIDER COPIAPO', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(100, 'STRIP TALCA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(101, 'LIDER QUILIN', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(102, 'STA ISABEL VILLANELO', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(103, 'TOTTUS LOS ANGELES', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(104, 'STRIP OLMUE', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(105, 'LIDER LOS ANGELES', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(106, 'LIDER ALAMEDA', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(107, 'EDIFICIO BAHULER', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL),
(108, 'LIDER CURICO', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `branch_office_transbanks`
--

CREATE TABLE `branch_office_transbanks` (
  `branch_office_transbank_id` int(11) NOT NULL,
  `branch_office_id` varchar(255) DEFAULT NULL,
  `transbank_code` varchar(255) DEFAULT NULL,
  `added_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `civil_states`
--

CREATE TABLE `civil_states` (
  `id` int(11) NOT NULL,
  `civil_state` varchar(255) NOT NULL,
  `added_date` datetime NOT NULL,
  `updated_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `civil_states`
--

INSERT INTO `civil_states` (`id`, `civil_state`, `added_date`, `updated_date`) VALUES
(1, 'Soltero', '2022-11-16 15:22:05', '2022-11-16 15:22:05'),
(2, 'Casado', '2022-11-16 15:22:05', '2022-11-16 15:22:05'),
(3, 'Viudo', '2022-11-16 16:08:15', '2022-11-16 16:08:15');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `communes`
--

CREATE TABLE `communes` (
  `commune_id` int(11) NOT NULL,
  `commune` varchar(255) DEFAULT NULL,
  `added_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contract_type`
--

CREATE TABLE `contract_type` (
  `id` int(11) NOT NULL,
  `contract_type` varchar(255) DEFAULT NULL,
  `added_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `contract_type`
--

INSERT INTO `contract_type` (`id`, `contract_type`, `added_date`, `updated_date`) VALUES
(1, '1 Mes', '2022-11-16 15:32:37', '2022-11-16 15:32:37'),
(2, '2 Meses', '2022-11-16 15:32:37', '2022-11-16 15:32:37'),
(3, 'Indefinido', '2022-11-16 15:32:37', '2022-11-16 15:32:37');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `contract_update_documents`
--

CREATE TABLE `contract_update_documents` (
  `id` int(11) NOT NULL,
  `document_employee_id` int(255) NOT NULL,
  `job_position_id` int(255) NOT NULL,
  `branch_office_id` int(255) NOT NULL,
  `gross_monthly_salary` varchar(255) NOT NULL,
  `start_date` date NOT NULL,
  `added_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `contract_update_documents`
--

INSERT INTO `contract_update_documents` (`id`, `document_employee_id`, `job_position_id`, `branch_office_id`, `gross_monthly_salary`, `start_date`, `added_date`) VALUES
(1, 24, 11, 16, '500000', '2022-11-15', '2022-11-15 15:53:21');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `documents_employees`
--

CREATE TABLE `documents_employees` (
  `id` int(11) NOT NULL,
  `status_id` int(255) NOT NULL,
  `rut` varchar(20) DEFAULT NULL,
  `document_type_id` int(11) DEFAULT NULL,
  `support` varchar(255) DEFAULT NULL,
  `added_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `documents_employees`
--

INSERT INTO `documents_employees` (`id`, `status_id`, `rut`, `document_type_id`, `support`, `added_date`, `updated_date`) VALUES
(25, 0, '18456789', 10, 'logo (1).jpg', '2022-11-21 15:34:42', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `documents_group`
--

CREATE TABLE `documents_group` (
  `documents_group_id` int(11) NOT NULL,
  `documents_group` varchar(255) DEFAULT NULL,
  `added_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `documents_group`
--

INSERT INTO `documents_group` (`documents_group_id`, `documents_group`, `added_date`, `updated_date`) VALUES
(1, 'Kardex', '2022-11-15 14:47:06', '2022-11-15 14:47:06'),
(2, 'Solicitudes', '2022-11-15 14:47:06', '2022-11-15 14:47:06'),
(3, 'Calculados', '2022-11-15 14:47:35', '2022-11-15 14:47:35');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `document_types`
--

CREATE TABLE `document_types` (
  `id` int(11) NOT NULL,
  `document_type` varchar(255) DEFAULT NULL,
  `document_group_id` int(11) DEFAULT NULL,
  `added_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `document_types`
--

INSERT INTO `document_types` (`id`, `document_type`, `document_group_id`, `added_date`, `updated_date`) VALUES
(1, 'Carta de Amonestación', 2, '2022-11-14 18:23:29', NULL),
(2, 'Certificado de Antigüedad', 2, '2022-11-14 18:23:32', NULL),
(3, 'Liquidaciones de Sueldo', 1, '2022-11-14 18:23:34', NULL),
(4, 'Papeleta de Vacaciones', 2, '2022-11-14 18:23:36', NULL),
(5, 'Falta de Atraso', 2, '2022-11-14 18:23:39', NULL),
(6, 'Abandono de Trabajo', 2, '2022-11-14 18:23:42', NULL),
(7, 'Falta Injustificada', 2, '2022-11-14 18:23:44', NULL),
(8, 'Permiso', 2, '2022-11-14 18:23:47', NULL),
(9, 'Cambio de Sucursal', 3, '2022-11-14 18:23:51', NULL),
(10, 'Actualización de Contrato', 1, '2022-11-14 18:23:53', NULL),
(11, 'Anexo de Puntualidad', 2, '2022-11-14 18:24:26', NULL),
(12, 'Carta de Compromiso', 1, '2022-11-14 18:24:23', NULL),
(13, 'Carta de Felicitación', 2, '2022-11-14 18:24:21', NULL),
(14, 'Carta de Término (Necesidades de la Empresa)', 2, '2022-11-14 18:24:19', NULL),
(15, 'Carta de Término (No Concurrencia)', 2, '2022-11-14 18:24:15', NULL),
(16, 'Carta de Término (Vencimiento de Plazo)', 2, '2022-11-14 18:24:17', NULL),
(17, 'RIOHS', 0, '2022-11-14 18:24:13', NULL),
(18, 'ODI', 0, '2022-11-14 18:24:11', NULL),
(19, 'Contrato', 0, '2022-11-14 18:24:07', NULL),
(20, 'Finiquito', 0, '2022-11-14 18:24:09', NULL),
(21, 'Horario Laboral', 2, '2022-11-14 18:24:05', NULL),
(22, 'Anexos Protección al Empleo', 1, '2022-11-14 18:24:03', NULL),
(23, 'Certificado de Antecedentes', 1, '2022-11-14 18:24:01', NULL),
(24, 'Curriculum Vitae', 1, '2022-11-14 18:23:59', NULL),
(25, 'Carnet', 1, '2022-11-14 18:23:56', NULL),
(28, 'Certificado de Fonasa o Isapre', 0, NULL, NULL),
(29, 'Certificado de AFP', 0, NULL, NULL),
(30, 'Certificado de Estudios', 1, NULL, NULL),
(31, 'ODI del Covid', 0, NULL, NULL),
(32, 'Equipo de Protección Personal', 0, NULL, NULL),
(33, 'Documento Vacaciones Progresivas', 1, NULL, NULL),
(34, 'Anexo de Contrato', 1, NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `employees`
--

CREATE TABLE `employees` (
  `id` int(11) NOT NULL,
  `rut` int(150) DEFAULT NULL,
  `visual_rut` varchar(150) NOT NULL,
  `names` varchar(255) DEFAULT NULL,
  `father_lastname` varchar(255) DEFAULT NULL,
  `mother_lastname` varchar(255) DEFAULT NULL,
  `nickname` varchar(255) DEFAULT NULL,
  `gender_id` int(11) DEFAULT NULL,
  `nationality_id` int(11) DEFAULT NULL,
  `cellphone` varchar(100) DEFAULT NULL,
  `born_date` date DEFAULT NULL,
  `picture` varchar(255) DEFAULT NULL,
  `added_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `employees`
--

INSERT INTO `employees` (`id`, `rut`, `visual_rut`, `names`, `father_lastname`, `mother_lastname`, `nickname`, `gender_id`, `nationality_id`, `cellphone`, `born_date`, `picture`, `added_date`, `updated_date`) VALUES
(1, 6152617, '06152617-8', 'Mirna Eugenia5', 'Gonzalez', 'Ahumada', 'Mirna Eugenia5 Gonzalez', 1, 1, '966158151', '1951-05-28', '22-06-20221655925636_foto.jpg', '2021-09-20 01:40:07', '2022-11-17 09:49:01'),
(2, 26913967, '', 'Kelida Del Valle', 'Cazorla', 'Rangel', 'Kelida Cazorla', 1, 5, '944608935', '1981-09-05', NULL, '2021-09-20 01:40:07', '2022-11-02 15:19:50'),
(3, 6802969, '', 'Margarita Del Carmen', 'Gonzalez', 'Ahumada', 'Margarita Gonzalez', 1, 1, '940959537', '1955-07-15', NULL, '2021-09-20 01:40:07', '2022-11-02 15:04:41'),
(4, 6974036, '', 'Ruben Osvaldo', 'Saavedra', 'Muñoz', 'Ruben Saavedra', 2, 1, '996452477', '1959-04-17', NULL, '2021-09-20 01:40:07', '2022-11-02 15:04:44'),
(5, 7066149, '', 'Juan Francisco', 'Zamorano', 'Beas', 'Juan Zamorano', 2, 1, '935640890', '1958-11-30', NULL, '2021-09-20 01:40:07', '2022-11-02 15:04:46'),
(6, 7174172, '', 'Luis Gregorio', 'Miranda', 'Montero', 'Luis Miranda', 2, 1, '993343689', '1956-10-08', NULL, '2021-09-20 01:40:07', '2022-11-02 15:04:49'),
(7, 7274753, '', 'Pedro Zozimo', 'Pereira', 'Contreras', 'Pedro Pereira', 2, 1, '990865042', '1953-08-15', NULL, '2021-09-20 01:40:07', '2022-11-02 15:04:51'),
(8, 7835227, '', 'Rita Elsa', 'Guzmán', 'Gomez', 'Rita Guzmán', 1, 1, '984205125', '1960-10-14', '12-09-20221662997319_foto.jpg', '2021-09-20 01:40:07', '2022-11-02 15:04:53'),
(9, 8068401, '', 'Estrella Del Carmen', 'Torres', 'Zuñiga', 'Estrella Torres', 1, 1, '952331373', '1957-11-24', NULL, '2021-09-20 01:40:07', '2022-11-02 15:04:55'),
(10, 8820315, '', 'Benjamin Leonardo', 'Bruyer', 'Gonzalez', 'Benjamin Leonardo Bruyer', 2, 1, '942547662', '1963-05-23', NULL, '2021-09-20 01:40:07', '2022-11-02 15:05:07'),
(11, 8883533, '', 'Patricia Marcela', 'Mancilla', 'Mayorga', 'Patricia Mancilla', 1, 1, '993633205', '1960-05-20', NULL, '2021-09-20 01:40:07', '2022-11-02 15:05:09'),
(12, 9134412, '', 'Gladys Antonia', 'Villegas', 'Alvarez', 'Gladys Villegas', 1, 1, '954263344', '1964-04-12', NULL, '2021-09-20 01:40:07', '2022-11-02 15:13:26'),
(13, 9360615, '', 'Carlos Roberto', 'Hidalgo', 'Miranda', 'Carlos Hidalgo', 2, 1, '965601796', '1961-03-20', NULL, '2021-09-20 01:40:07', '2022-11-02 15:05:14'),
(14, 9426000, '', 'Gabriel Ivan', 'Arriagada', 'Fuentes', 'Gabriel Arriagada', 2, 1, '937282522', '1963-01-01', NULL, '2021-09-20 01:40:07', '2022-11-02 15:05:16'),
(15, 9482390, '', 'Hernando Jose', 'Gonzalez', 'Pinilla', 'Hernando Gonzalez', 2, 1, '930623942', '1966-04-12', NULL, '2021-09-20 01:40:07', '2022-11-02 15:05:19'),
(16, 9874855, '', 'Gema Geraldina', 'Galdamez', 'Galdamez', 'Gema Galdamez', 1, 1, '985954915', '1963-06-03', NULL, '2021-09-20 01:40:07', '2022-11-02 15:06:14'),
(17, 10033721, '', 'Cristian Andres', 'Inzunza', 'Gonzalez', 'Cristian Andres Inzunza', 2, 1, '996423773', '1978-08-31', '07-08-20221659894356_foto.jpg', '2021-09-20 01:40:07', '2022-10-19 15:47:06'),
(18, 10033741, '', 'Marcelo Alejandro', 'Inzunza', 'Gonzalez', 'Marcelo Alejandro Inzunza', 2, 1, '968454900', '1978-08-31', NULL, '2021-09-20 01:40:07', '2022-10-19 15:47:50'),
(19, 10137545, '', 'Margarita Del Carmen', 'Contreras', 'Paredes', 'Margarita Contreras', 1, 1, '972498288', '1966-10-05', NULL, '2021-09-20 01:40:07', '2022-11-02 15:06:23'),
(20, 10431151, '', 'Judith Carolina', 'Baeza', 'Gonzalez', 'Judith Baeza', 1, 1, '976485201', '1976-08-22', NULL, '2021-09-20 01:40:07', '2022-11-02 15:06:28'),
(21, 10626085, '', 'Eliana De Jesus', 'Romero', 'Espinosa', 'Eliana De Jesus Romero', 1, 1, '988185795', '1969-05-05', NULL, '2021-09-20 01:40:07', '2022-11-02 15:06:30'),
(22, 10628514, '', 'Maria Soledad', 'Nuñez', 'Torrecilla', 'Maria Nuñez', 1, 1, '968051808', '1966-11-09', NULL, '2021-09-20 01:40:07', '2022-11-02 15:06:32'),
(23, 10725575, '', 'Jorge Ricardo', 'Flores', 'Pasten', 'Jorge Flores', 2, 1, '985096413', '1967-07-10', NULL, '2021-09-20 01:40:07', '2022-11-02 15:06:37'),
(24, 10750262, '', 'Roxana Del Carmen', 'Navarro', 'Oyarce', 'Roxana Navarro', 1, 1, '937710462', '1962-01-09', NULL, '2021-09-20 01:40:07', '2022-11-02 15:06:40'),
(25, 10790603, '', 'Patricio Marcelo', 'Gomez', 'Gonzalez', 'Patricio Marcelo Gomez', 2, 1, '985493836', '1973-05-29', NULL, '2021-09-20 01:40:07', '2022-10-19 15:50:33'),
(26, 10923452, '', 'Fidelia Del Carmen', 'Contreras', 'Gonzalez', 'Fidelia Contreras', 1, 1, '944320968', '1966-09-28', NULL, '2021-09-20 01:40:07', '2022-10-18 13:36:31'),
(27, 10963260, '', 'Maria Adelaida', 'Velasquez', 'Gallardo', 'Maria Velasquez', 1, 1, '996107873', '1970-05-04', NULL, '2021-09-20 01:40:07', '2022-11-02 15:06:50'),
(28, 11166398, '', 'Iris Gricelda', 'Cordova', 'Figueroa', 'Iris Cordova', 1, 1, '994615223', '1967-03-28', NULL, '2021-09-20 01:40:07', '2022-11-02 15:06:55'),
(29, 11243121, '', 'Artemio Alfonso', 'Barra', 'Panes', 'Artemio Barra', 2, 1, '962110950', '1968-08-27', NULL, '2021-09-20 01:40:07', '2022-11-02 15:06:57'),
(30, 11694645, '', 'Ana Maria', 'Estolaza', 'Peralta', 'Ana Estolaza', 1, 1, '963413639', '1970-11-21', NULL, '2021-09-20 01:40:07', '2022-11-02 15:12:14'),
(31, 11756501, '', 'Richard Antonio', 'Aranda', 'Puja', 'Richard Antonio Aranda', 2, 1, '958281269', '1971-04-20', NULL, '2021-09-20 01:40:07', '2022-11-02 15:07:40'),
(32, 11813180, '', 'Elba Genoveva', 'Ticona', 'Mamani', 'Elba Ticona', 1, 1, '945922929', '1971-01-02', NULL, '2021-09-20 01:40:07', '2022-11-02 15:07:42'),
(33, 11831400, '', 'Miryam Paula', 'Araya', 'Mora', 'Miryam Araya', 1, 1, '933358762', '1971-04-08', NULL, '2021-09-20 01:40:07', '2022-11-02 15:07:47'),
(34, 11849551, '', 'Ivonne Alejandra', 'Morales', 'Morales', 'Ivonne Morales', 1, 1, '979802150', '1971-01-27', NULL, '2021-09-20 01:40:07', '2022-11-02 15:07:49'),
(35, 12025353, '', 'Amora Cecilia', 'Almuna', 'Medel', 'Amora Almuna', 1, 1, '941823603', '1964-01-18', NULL, '2021-09-20 01:40:07', '2022-11-02 15:07:53'),
(36, 12233298, '', 'Elizabeth Patricia', 'Gonzalez', 'Carrasco', 'Elizabeth Gonzalez', 1, 1, '984744916', '1971-12-26', NULL, '2021-09-20 01:40:07', '2022-10-18 13:36:33'),
(37, 12252924, '', 'Margarita Nora', 'Herrera', 'Arriagada', 'Margarita Herrera', 1, 1, '956220343', '1971-11-07', NULL, '2021-09-20 01:40:07', '2022-11-02 15:08:00'),
(38, 12297111, '', 'Sandra Del Carmen', 'Salazar', 'Salazar', 'Sandra Salazar', 1, 1, '976542838', '1971-12-28', NULL, '2021-09-20 01:40:07', '2022-11-02 15:08:02'),
(39, 12642557, '', 'Marco Antonio', 'Figueroa', 'Diaz', 'Marco Figueroa', 2, 1, '944487497', '1974-11-14', NULL, '2021-09-20 01:40:07', '2022-10-18 13:36:35'),
(40, 12791259, '', 'Ruth Maribel', 'Norambuena', 'Cofre', 'Ruth Norambuena', 1, 1, '985633614', '1975-11-12', NULL, '2021-09-20 01:40:07', '2022-11-02 15:08:18'),
(41, 12793546, '', 'Guadalupe Del Carmen', 'Gonzalez', 'Toro', 'Guadalupe Gonzalez', 1, 1, '940560000', '1975-06-03', NULL, '2021-09-20 01:40:07', '2022-11-02 15:08:20'),
(42, 12885196, '', 'Jessica Del Carmen', 'Valenzuela', 'Hueraman', 'Jessica Valenzuela', 1, 1, '968751448', '1968-05-30', NULL, '2021-09-20 01:40:07', '2022-11-02 15:08:23'),
(43, 12996111, '', 'Viviana Del Carmen', 'Navarro', 'Gonzalez', 'Viviana Navarro', 1, 1, '961005025', '1976-07-22', NULL, '2021-09-20 01:40:07', '2022-11-02 15:08:59'),
(44, 13042688, '', 'Jose Antonio', 'Inzunza', 'Toledo', 'Jose Antonio Inzunza', 2, 1, '981363243', '1975-09-14', NULL, '2021-09-20 01:40:07', '2022-10-19 15:43:51'),
(45, 13175573, '', 'Yenny Karina', 'Escobar', 'Quezada', 'Yenny Escobar', 1, 1, '981302064', '1977-04-14', NULL, '2021-09-20 01:40:07', '2022-11-02 15:09:05'),
(46, 13252171, '', 'Carolina Soledad', 'Flores', 'Aedo', 'Carolina Soledad Flores', 1, 1, '999999999', '1977-12-17', NULL, '2021-09-20 01:40:07', '2022-11-02 15:09:14'),
(47, 13405296, '', 'Olga Magaly', 'Carrion', 'Sanhueza', 'Olga Magaly Carrion', 1, 1, '942933181', '1977-10-25', NULL, '2021-09-20 01:40:07', '2022-11-02 15:09:16'),
(48, 13492547, '', 'Angelica Loreto', 'Aballay', 'Sanchez', 'Angelica Aballay', 1, 1, '940906403', '1977-12-31', NULL, '2021-09-20 01:40:07', '2022-11-02 15:09:19'),
(49, 13764500, '', 'Alicia Andrea', 'Suarez', 'Tapia', 'Alicia Suarez', 1, 1, '979292569', '1980-10-04', '22-07-20221658452095_foto.png', '2021-09-20 01:40:07', '2022-11-02 15:23:57'),
(50, 13917718, '', 'Cristian Ruben', 'Adriazola', 'Sandoval', 'Cristian Adriazola', 2, 1, '944472993', '1980-08-12', NULL, '2021-09-20 01:40:08', '2022-10-18 13:36:42'),
(51, 14481738, '', 'Evelyn Damarys', 'Molina', 'Saavedra', 'Evelyn Molina', 1, 1, '996468885', '1974-05-15', NULL, '2021-09-20 01:40:08', '2022-11-02 15:13:20'),
(52, 15081798, '', 'Andrea Alejandra', 'Mena', 'Olivares', 'Andrea Mena', 1, 1, '942714858', '1982-07-15', '29-07-20221659122940_foto.jpg', '2021-09-20 01:40:08', '2022-11-02 15:11:37'),
(53, 15538007, '', 'Rodrigo Esteban', 'Cabezas', 'Zuñiga', 'Rodrigo Esteban Cabezas', 2, 1, '990202757', '1983-07-20', '06-07-20221657115042_foto.jpg', '2021-09-20 01:40:08', '2022-11-02 15:11:45'),
(54, 15757306, '', 'Dario De Jesus', 'Contreras', 'Martinez', 'Dario Contreras', 2, 1, '997184924', '1984-04-04', NULL, '2021-09-20 01:40:08', '2022-11-02 15:11:53'),
(55, 15808735, '', 'Adriana Paulina', 'Castillo', 'Aguirre', 'Adriana Castillo', 1, 1, '946201725', '1984-05-26', '12-07-20221657600056_foto.jpg', '2021-09-20 01:40:08', '2022-11-02 15:11:55'),
(56, 15910256, '', 'Jose Raul', 'Segura', 'Paz', 'Jose Segura', 2, 1, '953746433', '1985-06-17', NULL, '2021-09-20 01:40:08', '2022-11-02 15:11:57'),
(57, 15918421, '', 'Sandra Jimena', 'Sandoval', 'Vega', 'Sandra Jimena Sandoval', 1, 1, '942302858', '1984-11-16', NULL, '2021-09-20 01:40:08', '2022-11-02 15:11:59'),
(58, 15947022, '', 'Jessica Alejandra', 'Gomez', 'Nahuelhuen', 'Jessica Gomez', 1, 1, '981727139', '1984-12-31', NULL, '2021-09-20 01:40:08', '2022-11-02 15:12:01'),
(59, 16404869, '', 'Fabiola Yamilet', 'Fuentealba', 'Viveros', 'Fabiola Fuentealba', 1, 1, '984606050', '1986-11-25', NULL, '2021-09-20 01:40:08', '2022-11-02 15:13:18'),
(60, 16543379, '', 'Manuel Alejandro', 'Esparza', 'Medina', 'Manuel Esparza', 2, 1, '957864393', '1987-01-23', NULL, '2021-09-20 01:40:08', '2022-11-02 15:13:20'),
(61, 16727358, '', 'Gloria Eliana', 'Nahuelhueique', 'Vera', 'Gloria Nahuelhueique', 1, 1, '959496174', '1987-09-13', NULL, '2021-09-20 01:40:08', '2022-11-02 15:13:25'),
(62, 16787383, '', 'Juan Emilio', 'Caroca', 'Rojas', 'Juan Emilio Caroca', 2, 1, '986843524', '1987-12-30', NULL, '2021-09-20 01:40:08', '2022-11-02 15:13:28'),
(63, 16849126, '', 'Sofia Alejandra', 'Mundaca', 'Mundaca', 'Sofia Mundaca', 1, 1, '968712671', '1988-04-13', NULL, '2021-09-20 01:40:08', '2022-11-02 15:13:35'),
(64, 17113779, '', 'Johanna Andrea Del Carmen', 'Andrades', 'Andrades', 'Johanna Andrades', 1, 1, '954888068', '1988-11-05', NULL, '2021-09-20 01:40:08', '2022-11-02 15:13:37'),
(65, 17125113, '', 'Debora Eunice', 'Filun', 'Filun', 'Debora Eunice Filun', 1, 1, '984365326', '1988-11-24', '30-08-20221661871939_foto.jpeg', '2021-09-20 01:40:08', '2022-10-18 13:36:53'),
(66, 17128461, '', 'Katherine Andrea', 'Pavez', 'Rubio', 'Katherine Pavez', 1, 1, '957514130', '1989-07-03', NULL, '2021-09-20 01:40:08', '2022-11-02 15:14:58'),
(67, 17200607, '', 'Magdianita Andrea', 'Saez', 'Duran', 'Magdianita Saez', 1, 1, '962973574', '1989-03-15', '17-08-20221660697586_foto.jpg', '2021-09-20 01:40:08', '2022-11-02 15:13:46'),
(68, 17292825, '', 'Patrick Guillermo', 'Orellana', 'Miranda', 'Patrick Orellana', 2, 1, '935172879', '1989-09-09', '22-06-20221655940160_foto.jpg', '2021-09-20 01:40:08', '2022-11-02 15:42:11'),
(69, 17390237, '', 'Nicole Andrea', 'Reitter', 'Cordova', 'Nicole Reitter', 1, 1, '935314781', '1990-01-14', NULL, '2021-09-20 01:40:08', '2022-11-02 15:13:55'),
(70, 17707004, '', 'Tania Andrea', 'Mallea', 'Zamorano', 'Tania Mallea', 1, 1, '954681747', '1991-02-11', NULL, '2021-09-20 01:40:08', '2022-11-02 15:13:57'),
(71, 17927553, '', 'Soledad De Las Mercedes', 'Burboa', 'Aguilera', 'Soledad Burboa', 1, 1, '968355917', '1991-05-07', NULL, '2021-09-20 01:40:08', '2022-11-03 19:02:52'),
(72, 18202568, '', 'Diana Victoria', 'Luna', 'Yañez', 'Diana Luna', 1, 1, '959984483', '1992-08-02', NULL, '2021-09-20 01:40:08', '2022-11-02 15:15:02'),
(73, 18273096, '', 'Max Henry', 'Henning', 'Escarate', 'Max Henning', 2, 1, '944851367', '1993-05-17', NULL, '2021-09-20 01:40:08', '2022-11-02 15:15:10'),
(74, 18566961, '', 'Belen Lorena', 'Cerro', 'Saldias', 'Belen Cerro', 1, 1, '931172034', '1994-01-30', NULL, '2021-09-20 01:40:08', '2022-11-02 15:15:14'),
(75, 18579236, '', 'Carolina Alicia', 'Muñoz', 'Angulo', 'Carolina Muñoz', 1, 1, '948638770', '1994-03-26', NULL, '2021-09-20 01:40:08', '2022-11-02 15:15:16'),
(76, 18842465, '', 'Yessenia Del Carmen', 'Arriaza', 'Brito', 'Yessenia Arriaza', 1, 1, '936585902', '1994-10-15', NULL, '2021-09-20 01:40:08', '2022-11-02 15:15:24'),
(77, 19390553, '', 'Rodolfo Andres', 'Espinoza', 'Vega', 'Rodolfo Espinoza', 2, 1, NULL, '1997-01-24', NULL, '2021-09-20 01:40:08', '2022-11-02 15:15:35'),
(78, 19844084, '', 'Karla Nicole', 'Cabezas', 'Zuñiga', 'Karla Cabezas', 1, 1, '948736819', '1998-03-05', NULL, '2021-09-20 01:40:08', '2022-11-02 15:18:20'),
(79, 19966543, '', 'Cristina Jael', 'Godoy', 'Contreras', 'Cristina Godoy', 1, 1, '934328754', '1998-05-16', NULL, '2021-09-20 01:40:08', '2022-11-02 15:16:42'),
(80, 20060059, '', 'Constanza Alejandra', 'Orrego', 'Sandoval', 'Constanza Alejandra Orrego', 1, 1, '936221564', '1999-06-24', NULL, '2021-09-20 01:40:08', '2022-11-02 15:16:55'),
(81, 20227575, '', 'Diana Alexandra', 'Burboa', 'Aguilera', 'Diana Burboa', 1, 1, '941070463', '2000-01-12', NULL, '2021-09-20 01:40:08', '2022-11-02 15:17:04'),
(82, 21828453, '', 'Elena Tomasa', 'Ruiz Diaz', 'De Mujica', 'Elena Ruiz Diaz', 1, 1, '991076593', '1957-10-13', '24-06-20221656114512_foto.jpg', '2021-09-20 01:40:08', '2022-11-02 15:18:06'),
(83, 21902443, '', 'David Wilder', 'Gomez', 'Figueroa', 'David Gomez', 2, 8, '942998970', '1987-04-03', NULL, '2021-09-20 01:40:08', '2022-10-18 13:36:57'),
(84, 22588139, '', 'Homar', 'Sanchez', 'Alvarado', 'Homar Sanchez', 2, 8, '993605555', '1980-08-17', NULL, '2021-09-20 01:40:08', '2022-11-02 15:18:11'),
(85, 23881022, '', 'Winger Enrique', 'Ricaldi', 'Calderon', 'Winger Ricaldi', 2, 8, '932241979', '1987-04-26', NULL, '2021-09-20 01:40:08', '2022-11-02 15:18:24'),
(86, 24773648, '', 'Delvy Zamira', 'Hernandez', 'Arias', 'Delvy Hernandez', 1, 2, '986020991', '1989-07-03', NULL, '2021-09-20 01:40:08', '2022-11-02 15:18:30'),
(87, 24811238, '', 'Sinthya Karina', 'Palomino', 'Echegaray', 'Sinthya Palomino', 1, 8, '930387680', '1980-03-07', '26-07-20221658874828_foto.jpg', '2021-09-20 01:40:08', '2022-11-02 15:18:32'),
(88, 25259612, '', 'Odalis', 'Chambilla', 'Roque', 'Odalis Chambilla', 1, 7, '941194181', '1990-12-28', NULL, '2021-09-20 01:40:08', '2022-11-02 15:18:34'),
(89, 25310541, '', 'Nurvys Yasnair', 'Toro', '-', 'Nurvys Toro', 1, 5, '967529072', '1982-08-20', NULL, '2021-09-20 01:40:08', '2022-11-02 15:18:37'),
(90, 25310683, '', 'Edwin Alexander', 'Arteaga', 'Barrios', 'Edwin Arteaga', 2, 5, '962581133', '1981-10-24', NULL, '2021-09-20 01:40:08', '2022-11-02 15:18:39'),
(91, 25383726, '', 'Marielena Del Valle', 'Cazorla', 'Rangel', 'Marielena Cazorla', 1, 5, '946479719', '1991-01-31', NULL, '2021-09-20 01:40:08', '2022-11-02 15:19:20'),
(92, 25486922, '', 'Mirian Marlene', 'Zambrano', 'Loor', 'Mirian Zambrano', 1, 9, '986245433', '1985-04-18', NULL, '2021-09-20 01:40:08', '2022-11-02 15:19:22'),
(93, 25705970, '', 'Cesar Javier', 'Botello', 'Pacheco', 'Cesar Botello', 2, 5, '940711070', '1980-01-11', NULL, '2021-09-20 01:40:08', '2022-10-18 13:36:59'),
(94, 25939855, '', 'Katherine Veronica', 'Chiquito', 'Valiente', 'Katherine Chiquito', 1, 9, '964455060', '1984-08-14', NULL, '2021-09-20 01:40:08', '2022-11-02 15:19:28'),
(95, 26299443, '', 'Eva Johana', 'Letzguss', 'Coruma', 'Eva Letzguss', 1, 5, '986186611', '1977-02-12', NULL, '2021-09-20 01:40:08', '2022-11-02 15:19:33'),
(96, 23645227, '', 'Maria Martha', 'Cabanillas', 'Flores', 'Maria Cabanillas', 1, 8, '932512120', '1973-10-23', NULL, '2021-09-20 01:40:08', '2022-11-02 15:18:21'),
(97, 12921934, '', 'Yessica Alejandra', 'Sanhueza', 'Valenzuela', 'Yessica Sanhueza', 1, 1, '987651711', '1975-07-26', NULL, '2021-09-20 01:40:08', '2022-10-18 13:36:37'),
(98, 12069398, '', 'Juan Manuel', 'Calderon', 'Peralta', 'Juan Calderon', 2, 1, '962684745', '1966-07-31', NULL, '2021-09-20 01:40:08', '2022-11-02 15:07:56'),
(99, 17995199, '', 'Estephanie Valeria', 'Toro', 'Saldaño', 'Estephanie Toro', 1, 1, '975967874', '1991-11-11', NULL, '2021-09-20 01:40:08', '2022-11-02 15:14:07'),
(100, 26303301, '', 'Feguenson', 'Jean Jacques', 'Philistin', 'Feguenson Jean Jacques', 2, 3, '941631212', '1990-01-05', NULL, '2021-09-20 01:40:08', '2022-11-02 15:19:35'),
(101, 11938713, '', 'Walter Arnaldo', 'Pasten', 'Cortes', 'Walter Pasten', 2, 1, '985567214', '1972-11-28', NULL, '2021-09-20 01:40:08', '2022-11-02 15:07:51'),
(102, 9535406, '', 'Rigoberto Ivan', 'Cerda', 'Guerra', 'Rigoberto Cerda', 2, 1, '962324244', '1962-07-08', NULL, '2021-09-20 01:40:08', '2022-11-02 15:05:22'),
(103, 26598819, '', 'Jenifer Nataly', 'Huertas', 'Flores', 'Jenifer Huertas', 1, 8, '987103529', '1999-06-01', '13-11-20221668357224_foto.jpeg', '2021-09-20 01:40:08', '2022-11-13 16:33:44'),
(104, 15583027, '', 'Karina Andrea', 'Flores', 'Garcia', 'Karina Flores', 1, 1, '991337607', '1984-11-11', NULL, '2021-09-20 01:40:08', '2022-11-02 15:11:47'),
(105, 16788913, '', 'Daisy Dayana', 'Diaz', 'Garrido', 'Daisy Diaz', 1, 1, '942844779', '1988-04-17', NULL, '2021-09-20 01:40:08', '2022-11-02 15:13:30'),
(106, 6628494, '', 'Rosa Veronica', 'Olmos', 'Silva', 'Rosa Olmos', 1, 1, '972152402', '1952-07-02', '26-07-20221658851021_foto.jpg', '2021-09-20 01:40:08', '2022-11-02 15:04:38'),
(107, 10313233, '', 'Mercedes Del Carmen', 'Pontigo', 'Farias', 'Mercedes Pontigo', 1, 1, '949791787', '1964-09-24', NULL, '2021-09-20 01:40:08', '2022-11-02 15:06:25'),
(108, 23468753, '', 'Luis Antonio', 'Huasasquiche', 'Wan', 'Luis Huasasquiche', 2, 8, '946304302', '1969-06-13', NULL, '2021-09-20 01:40:08', '2022-11-02 15:18:16'),
(109, 26803446, '', 'Carlos Eduardo', 'Bruestlen', 'Tovar', 'Carlos Eduardo Bruestlen', 2, 5, '977714194', '1984-10-12', NULL, '2021-09-20 01:40:08', '2022-11-02 15:19:45'),
(110, 19181860, '', 'Vanesa Yohana Viviana', 'Guentrepan', 'Navarro', 'Vanesa Guentrepan', 1, 1, '973682891', '1996-06-30', NULL, '2021-09-20 01:40:08', '2022-11-02 15:15:31'),
(111, 26488988, '', 'Luis Javier', 'Melean', 'Sanchez', 'Luis Melean', 2, 5, '972005633', '1972-01-15', NULL, '2021-09-20 01:40:08', '2022-11-02 15:19:37'),
(112, 26173938, '', 'Oscar Horacio', 'Prada', 'Duarte', 'Oscar Prada', 2, 2, '934160592', '1994-10-11', NULL, '2021-09-20 01:40:08', '2022-11-02 15:19:31'),
(113, 27008183, '', 'Granda Isabel', 'Patiño', 'Pino', 'Granda Isabel Patiño', 1, 5, '936751486', '1960-01-30', NULL, '2021-09-20 01:40:08', '2022-11-02 15:19:57'),
(114, 26567665, '', 'Luis Ernesto', 'Miranda', 'Lucien', 'Luis Miranda', 2, 5, '986836139', '1989-08-31', NULL, '2021-09-20 01:40:08', '2022-11-02 15:53:33'),
(115, 20483426, '', 'Juan Eduardo', 'Toledo', 'Campos', 'Juan Toledo', 2, 1, '954734840', '2000-07-31', NULL, '2021-09-20 01:40:08', '2022-11-02 15:17:54'),
(116, 14352987, '', 'Marisol Alejandra', 'Monsalve', 'Aguirre', 'Marisol Monsalve', 1, 1, '991011047', '1978-12-22', NULL, '2021-09-20 01:40:08', '2022-11-02 15:11:27'),
(117, 26980959, '', 'Frank Vicente', 'Ovalles', 'Virahonda', 'Frank Ovalles', 2, 5, '988231729', '1962-11-09', NULL, '2021-09-20 01:40:08', '2022-11-02 16:29:44'),
(118, 18805028, '', 'Melanny Catalina', 'Iturriaga', 'Valverde', 'Melanny Iturriaga', 1, 1, '964047718', '1994-09-24', NULL, '2021-09-20 01:40:08', '2022-11-02 15:15:21'),
(119, 27008182, '', 'Carlos Antonio', 'Ugas', 'Gutierrez', 'Carlos Ugas', 2, 5, '937751487', '1956-04-02', NULL, '2021-09-20 01:40:08', '2022-11-02 15:19:55'),
(120, 18657051, '', 'Dennis Alexander', 'Bravo', 'YaÑez', 'Dennis Bravo', 2, 1, '965643297', '1994-08-04', NULL, '2021-09-20 01:40:08', '2022-11-02 15:15:19'),
(121, 20406658, '', 'Katie Scarlet', 'Toro', 'Vargas', 'Katie Toro', 1, 1, '958868919', '2000-05-22', NULL, '2021-09-20 01:40:08', '2022-11-02 15:17:12'),
(122, 27474935, '', 'Manuel Felipe', 'Cazorla', 'Henriquez', 'Manuel Cazorla', 2, 5, '947471898', '1956-11-25', NULL, '2021-09-20 01:40:08', '2022-11-02 15:20:07'),
(123, 16698947, '', 'Nicole Victoria', 'Sepulveda', 'Valenzuela', 'Nicole Victoria Sepulveda', 1, 1, '933247443', '1988-04-08', NULL, '2021-09-20 01:40:08', '2022-11-02 15:13:23'),
(124, 19903195, '', 'Bella Yesabella', 'Silva', 'Guitierrez', 'Bella Silva', 1, 8, '950780598', '1998-05-02', NULL, '2021-09-20 01:40:08', '2022-11-07 14:14:47'),
(125, 26868737, '', 'Alvaro David', 'Urrieta', '-', 'Alvaro Urrieta', 2, 5, '936840570', '1991-09-02', NULL, '2021-09-20 01:40:08', '2022-11-02 15:19:47'),
(126, 14594420, '', 'Nayade Macarena', 'Valverde', 'Valverde', 'Nayade Valverde', 1, 1, '941491729', '1976-06-22', NULL, '2021-09-20 01:40:08', '2022-11-02 15:11:35'),
(127, 27231254, '', 'Nelson Jose', 'Palacios', 'Palacios', 'Nelson Palacios', 2, 5, '974864693', '1958-05-22', NULL, '2021-09-20 01:40:08', '2022-11-02 15:20:02'),
(128, 19229525, '', 'Jose Miguel', 'Aravena', 'Fuentes', 'Jose Aravena', 2, 1, '949197079', '1996-01-26', '12-09-20221662999029_foto.jpg', '2021-09-20 01:40:08', '2022-11-02 15:15:33'),
(129, 10642899, '', 'Juan Manuel', 'Aranda', 'Puja', 'Juan Aranda', 2, 1, '947334764', '1969-04-11', NULL, '2021-09-20 01:40:08', '2022-11-02 15:06:35'),
(130, 11155155, '', 'Veronica Isabel', 'Fernandez', 'Quezada', 'Veronica Fernandez', 1, 1, '956325955', '1967-04-06', NULL, '2021-09-22 21:40:59', '2022-11-02 15:06:52'),
(131, 18255994, '', 'Camila Alejandra', 'Retamales', 'Contreras', 'Camila Retamales', 1, 1, '932696230', '1992-06-22', NULL, '2021-10-13 18:52:49', '2022-11-02 15:15:07'),
(132, 15949608, '', 'Jennifer Paz', 'Segura', 'Berrios', 'Jennifer Segura', 1, 1, '974142690', '1984-10-12', NULL, '2021-10-22 16:06:06', '2022-11-02 15:12:03'),
(133, 19502922, '', 'Maria Jose', 'Alarcon', 'Rebolledo', 'Maria Alarcon', 1, 1, '936342077', '1996-08-17', NULL, '2021-11-05 17:58:21', '2022-11-02 15:15:42'),
(134, 19641309, '', 'Alexandra Marisel', 'Muñoz', 'Ceron', 'Alexandra Muñoz', 1, 1, '920870569', '1997-07-29', NULL, '2021-11-10 21:17:10', '2022-11-02 15:16:33'),
(135, 20791756, '', 'Macarena Alejandra', 'Acevedo', 'Aburto', 'Macarena Acevedo', 1, 1, '951937538', '2002-04-30', NULL, '2021-12-06 21:55:20', '2022-11-02 15:17:57'),
(136, 17722392, '', 'Leonel Alfonso', 'Ossandon', 'Zepeda', 'Leonel Ossandon', 2, 1, '935375111', '1991-01-10', NULL, '2021-12-06 21:55:45', '2022-11-02 15:14:00'),
(137, 27141399, '', 'Jesus Rafael', 'Cova', 'Huerta', 'Jesus Rafael Cova', 2, 5, '935887241', '1988-10-10', '', '2021-12-09 19:50:02', '2022-11-02 15:21:01'),
(138, 12746837, '', 'Veronica Ana', 'Cifuentes', 'Cortez', 'Veronica Cifuentes', 1, 1, '974772539', '1969-04-06', NULL, '2021-12-13 19:49:51', '2022-11-02 15:08:15'),
(139, 8804983, '', 'Luisa Monica', 'Contreras', 'Acuña', 'Luisa Contreras', 1, 1, '993350955', '1960-05-10', NULL, '2021-12-13 20:04:39', '2022-11-02 15:05:04'),
(140, 20456116, '', 'Danitza Daniela', 'Sepulveda', 'Valenzuela', 'Danitza Sepulveda', 1, 1, '984845042', '2000-12-10', NULL, '2022-01-11 23:06:55', '2022-11-02 15:17:14'),
(141, 8507859, '', 'Juana Maria', 'Adaos', 'Medalla', 'Juana Adaos', 1, 1, '942534512', '1961-11-25', '21-06-20221655832330_foto.jpg', '2022-01-24 16:40:17', '2022-11-02 15:05:00'),
(142, 22594024, '', 'Maria Natividad', 'Cabanillas', 'Flores', 'Maria Cabanillas', 1, 8, '954529145', '1971-09-09', NULL, '2022-02-04 18:02:05', '2022-11-02 15:18:13'),
(143, 23541053, '', 'Julio Adrian', 'Pastor', 'Mantilla', 'Julio Pastor', 2, 8, '968687531', '1988-03-01', NULL, '2022-02-04 18:15:50', '2022-11-02 15:18:18'),
(144, 11422146, '', 'Jacqueline Del Pilar', 'Tapia', 'Nanjari', 'Jacqueline Tapia', 1, 1, '976135927', '1968-10-31', NULL, '2022-02-10 18:23:09', '2022-11-02 15:07:00'),
(145, 11450384, '', 'Mario Enrique', 'San Martin', 'Sobarzo', 'Mario San Martin', 2, 1, '978491202', '1968-08-24', NULL, '2022-03-03 00:32:32', '2022-11-02 16:56:37'),
(146, 21220816, '', 'Millaray Ignacia', 'Gutierrez', 'Gonzalez', 'Millaray Gutierrez', 1, 1, '958966228', '2003-01-22', NULL, '2022-03-03 00:41:48', '2022-11-02 15:18:04'),
(147, 13215814, '', 'Silvia Elisa', 'Muñoz', 'Jaramillo', 'Silvia Muñoz', 1, 1, '953559766', '1977-06-11', NULL, '2022-03-10 00:11:12', '2022-11-02 15:09:08'),
(148, 19635271, '', 'Tamara Irene', 'Candia', 'Vasquez', 'Tamara Candia', 1, 1, '937537792', '1997-07-15', NULL, '2022-03-23 21:46:06', '2022-11-02 15:15:44'),
(149, 19460849, '', 'Paullette Estefania', 'Rojo', 'Castillo', 'Paullette Rojo', 1, 1, '976071699', '1998-03-03', '06-10-20221665086578_foto.png', '2022-04-05 00:22:19', '2022-11-02 15:15:40'),
(150, 27333165, '', 'Ana Rosa', 'Acuña', 'Segura', 'Ana Acuña', 1, 5, '950455498', '1981-06-21', NULL, '2022-04-05 00:37:59', '2022-11-02 15:20:04'),
(151, 20478226, '', 'Adali Patricia', 'Moya', 'Navea', 'Adali Moya', 1, 1, '983896196', '2000-06-27', NULL, '2022-04-06 01:59:44', '2022-11-02 15:17:19'),
(152, 13224433, '', 'Andrea Valeska', 'Varela', 'Varela', 'Andrea Varela', 1, 1, '944031037', '1977-08-05', NULL, '2022-04-06 20:15:00', '2022-11-02 15:09:10'),
(153, 20406308, '', 'Ignacio Andres', 'Flores', 'Pizarro', 'Ignacio Flores', 2, 1, '983607415', '2000-03-28', '19-08-20221660943989_foto.jpg', '2022-04-06 20:29:03', '2022-11-02 15:17:09'),
(154, 20167026, '', 'Renata Belen', 'Sanhueza', 'Fuentes', 'Renata Sanhueza', 1, 1, '961048571', '1999-05-03', '18-08-20221660842247_foto.jpeg', '2022-04-06 20:39:39', '2022-11-02 15:32:05'),
(155, 18871148, '', 'Daniela Alejandra', 'Emilqueo', 'Coronado', 'Daniela Alejandra Emilqueo', 1, 1, '983237529', '1994-09-05', NULL, '2022-04-12 00:05:28', '2022-11-02 15:15:26'),
(156, 18382569, '', 'Daniela Noemi', 'Mena', 'Olivares', 'Daniela Mena', 1, 1, '920300091', '1993-08-23', '09-11-20221668032639_foto.jpg', '2022-04-12 19:45:01', '2022-11-09 22:23:59'),
(157, 15214405, '', 'Alicia Viviana', 'Sandoval', 'Pino', 'Alicia Sandoval', 1, 1, '947148408', '1982-09-23', NULL, '2022-05-11 00:54:21', '2022-11-02 16:10:04'),
(158, 16166948, '', 'Elia Andrea', 'Labrin', 'Sandoval', 'Elia Labrin', 1, 1, '959281455', '1986-04-13', NULL, '2022-05-11 01:25:07', '2022-11-02 15:12:08'),
(159, 12603512, '', 'Lilian Gladys', 'Muñoz', 'Diaz', 'Lilian Muñoz', 1, 1, '944969323', '1974-10-23', NULL, '2022-05-12 00:54:41', '2022-11-02 15:08:10'),
(160, 18228287, '', 'Anibal Isaac', 'Alvear', 'Saavedra', 'Anibal Alvear', 2, 1, '978085299', '1993-03-29', NULL, '2022-05-26 18:37:41', '2022-11-04 15:05:11'),
(161, 20181073, '', 'Francisca Jimena', 'Aguilera', 'Aguero', 'Francisca Jimena Aguilera', 1, 1, '975983380', '2000-01-19', NULL, '2022-06-02 21:31:37', '2022-11-02 15:17:00'),
(162, 8602937, '', 'Alejandro Hector', 'Del Canto', 'Zepeda', 'Alejandro Hector Del Canto', 2, 1, '957529852', '1958-12-26', NULL, '2022-06-02 23:31:44', '2022-11-02 15:05:02'),
(163, 16031459, '', 'Daniela Jenniffer', 'Alfaro', 'Castillo', 'Daniela Jenniffer Alfaro', 1, 1, '975916768', '1985-04-25', NULL, '2022-06-03 00:33:14', '2022-11-02 15:48:02'),
(164, 10778964, '', 'Sandra Luisa', 'Millan', 'Saenz', 'Sandra Luisa Millan', 1, 1, '940448450', '1968-04-13', NULL, '2022-06-03 00:43:13', '2022-11-02 15:06:42'),
(165, 15438533, '', 'Valeria Alejandra', 'Contreras', 'Carrasco', 'Valeria Alejandra Contreras', 1, 1, '933681733', '1982-04-20', NULL, '2022-06-03 00:50:57', '2022-11-09 19:47:03'),
(166, 12412764, '', 'Roxana Elizabeth', 'Diaz', 'Lorca', 'Roxana Elizabeth Diaz', 1, 1, '967201194', '1973-11-26', NULL, '2022-06-07 20:41:49', '2022-11-02 15:08:07'),
(167, 20832254, '', 'Patrick Ignacio De Jesus', 'Gonzalez', 'Diaz', 'Patrick Ignacio De Jesus Gonzalez', 2, 1, '950460799', '2001-08-21', NULL, '2022-06-07 21:03:38', '2022-11-02 15:17:59'),
(168, 18101806, '', 'Nicol Solange', 'Gonzalez', 'Saez', 'Nicol Solange Gonzalez', 1, 1, '981895524', '1992-07-21', NULL, '2022-06-07 21:21:14', '2022-11-02 15:14:09'),
(169, 24437831, '', 'Susan Marleny', 'Silva', 'Espinoza', 'Susan Marleny Silva', 1, 8, '967255400', '1985-02-26', NULL, '2022-07-04 20:40:49', '2022-11-02 15:18:27'),
(170, 19855558, '', 'Bastian Ariel', 'Neira', 'Isla', 'Bastian Ariel Neira', 2, 1, '965670775', '1998-11-26', NULL, '2022-07-05 23:20:17', '2022-11-02 15:16:38'),
(171, 11819715, '', 'Graciela Carolina', 'Contreras', 'Gonzalez', 'Graciela Carolina Contreras', 1, 1, '963535223', '1971-08-06', NULL, '2022-07-14 21:15:38', '2022-11-02 15:07:44'),
(172, 19392274, '', 'Cristóbal Andrés', 'Hernandez', 'Garrido', 'Cristóbal Andrés Hernandez', 2, 1, '957424487', '1997-05-18', NULL, '2022-08-02 20:24:38', '2022-11-02 15:15:37'),
(173, 19985262, '', 'Bastian Raul', 'Gonzalez', 'Diaz', 'Bastian Gonzalez', 2, 1, '978624674', '1998-09-14', NULL, '2022-08-03 00:31:48', '2022-11-06 03:46:12'),
(174, 27834958, '', 'Eliana Marcela', 'Alquerque', 'Avendaño', 'Eliana Marcela Alquerque', 1, 2, '945714126', '1995-02-19', NULL, '2022-08-04 19:20:28', '2022-11-06 14:09:47'),
(175, 20460536, '', 'Fernando Antonio', 'Cuello', 'Neira', 'Fernando Antonio Cuello', 2, 1, '965455752', '2001-05-30', NULL, '2022-09-08 19:14:02', '2022-11-02 15:17:16'),
(176, 8488685, '', 'Jacqueline del Carmen', 'Ampuero', 'Navarro', 'Jacqueline del Carmen Ampuero', 1, 1, '569654060', '1968-07-18', NULL, '2022-09-08 20:08:24', '2022-11-02 15:04:58'),
(177, 18984116, '', 'Jose Ignacio', 'Carvajal', 'Carvajal', 'Jose Ignacio Carvajal', 2, 1, '930942297', '1994-09-25', NULL, '2022-09-08 20:50:25', '2022-11-02 15:15:28'),
(178, 20050393, '', 'Catalina Andrea', 'Nahuelhueique', 'Contreras', 'Catalina Andrea Nahuelhueique', 1, 1, '921990684', '1999-01-31', NULL, '2022-09-08 21:48:13', '2022-11-02 15:16:53'),
(179, 14584925, '', 'John Patricio', 'Riveros', 'Salas', 'John Patricio Riveros', 2, 1, '973952352', '1980-07-28', NULL, '2022-09-12 18:35:26', '2022-11-02 15:11:33'),
(180, 13995235, '', 'Carolina Sybyl de Lourdes', 'Tapia', 'Leal', 'Carolina Sybyl de Loudes Tapia', 1, 1, '988837106', '1981-03-27', NULL, '2022-09-14 00:04:39', '2022-11-02 15:09:26'),
(181, 20040658, '', 'Camila Almendra', 'Cuevas', 'Aravena', 'Camila Almendra Cuevas', 1, 1, '996885970', '1998-10-17', NULL, '2022-09-14 19:04:43', '2022-11-02 15:16:50'),
(182, 12307656, '', 'Miguel Francisco', 'Tenorio', 'Vidal', 'Miguel Francisco Tenorio', 2, 1, '98818795', '1971-10-07', NULL, '2022-10-07 14:17:27', '2022-11-02 15:08:05'),
(183, 15737253, '', 'Luis Omar', 'Pinto', 'Urrejola', 'Luis Omar Pinto', 2, 1, '942113007', '1983-12-25', NULL, '2022-10-07 14:31:23', '2022-11-02 16:22:21'),
(184, 20903503, '', 'Dagney Kelsey', 'Vega', 'Pardo', 'Dagney Kelsey Vega', 1, 1, '981927485', '2002-01-18', NULL, '2022-10-07 15:26:12', '2022-11-02 15:18:01'),
(185, 17946694, '', 'Esteban Exequiel', 'illesca', 'Torres', 'Esteban Exequiel illesca', 2, 1, '983680598', '1984-12-21', NULL, '2022-10-11 16:16:33', '2022-11-02 15:14:05'),
(186, 20313567, '', 'Marcelo Antonio', 'Ocaranza', 'Herrera', 'Marcelo Antonio Ocaranza', 2, 1, '967777921', '2001-02-04', NULL, '2022-10-12 20:01:46', '2022-11-02 15:17:07'),
(187, 19984683, '', 'Melisa Nataly', 'Sepúlveda', 'Westermeier', 'Melisa Nataly Sepúlveda', 1, 1, '930977268', '1998-08-01', NULL, '2022-10-13 13:50:28', '2022-11-02 15:16:46'),
(188, 16813515, '', 'Tannya Andrea', 'Montano', 'Ossa', 'Tannya Andrea Montano', 1, 1, '956094084', '1988-06-14', NULL, '2022-10-14 14:10:42', '2022-11-02 15:13:33'),
(189, 10157343, '', 'Eva', 'Santibañez', 'Contreras', 'Eva Santibañez', 1, 1, '991736160', '1964-05-08', NULL, '2022-11-02 17:18:33', '2022-11-03 15:58:13'),
(190, 19564927, '', 'Bastian Andres', 'Torroja', 'Mena', 'Bastian Andres Torroja', 2, 1, 'null', '1997-03-14', NULL, '2022-11-03 17:07:32', '2022-11-03 21:03:47'),
(191, 20146124, '', 'Marco Jesus', 'Pizarro', 'Valdivia', 'Marco Jesus Pizarro', 2, 1, '940228559', '1999-04-22', NULL, '2022-10-17 18:32:55', '2022-11-08 13:16:22'),
(192, 21378739, '', 'Catalina Alejandra', 'Javia', 'Rojas', 'Catalina Alejandra Javia', 2, 1, '965736431', '2003-08-29', NULL, '2022-11-09 14:34:33', '2022-11-09 14:42:03'),
(193, 20433991, '', 'Valeria Alejandra', 'Paredes', 'Riffo', 'Valeria Alejandra Paredes', 1, 1, '965036758', '2000-05-06', NULL, '2022-11-09 15:14:30', '2022-11-09 15:20:18'),
(194, 12067461, '', 'Patricia Esmeralda', 'Estolaza', 'Peralta', 'Patricia Esmeralda Estolaza', 1, 1, '921684559', '1969-05-21', NULL, '2022-11-09 16:25:51', '2022-11-09 18:55:11'),
(195, 16281232, '', 'Gonzalo Ignacio', 'Aballay', 'Sanchez', NULL, 2, 1, '967513180', '1986-07-10', NULL, '2022-10-18 17:29:26', '2022-11-09 21:00:58'),
(196, 14003387, '', 'Ariana Elizabeth', 'Lopez', 'Lopez', NULL, 2, 1, '964296565', '1981-06-03', NULL, '2022-10-18 17:30:01', '2022-10-18 17:30:01'),
(197, 21923989, '', 'Yesica Licett', 'Tisnado', 'Villena', 'Yesica Licett Tisnado', 1, 8, '979797985', '1980-08-22', NULL, '2022-10-17 18:33:29', '2022-11-10 20:29:26'),
(208, 28789456, '28789456-8', 'jesus', 'cova', 'Huerta', 'jesus cova', 1, 5, '935887241', '2022-11-16', NULL, '2022-11-16 15:28:33', '2022-11-16 15:45:55'),
(209, 18456789, '18456789-8', '66454', '33', 'qw2', '66454 33', 2, 2, '2323', '2022-11-16', NULL, '2022-11-16 16:12:58', '2022-11-17 10:17:40'),
(210, 15456789, '15456789-8', 'Nombres', 'Apeli', 'qw2', 'Nombres Apeli', 1, 1, '22222', '2022-11-16', NULL, '2022-11-16 16:15:29', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `employee_labor_data`
--

CREATE TABLE `employee_labor_data` (
  `id` int(11) NOT NULL,
  `rut` int(20) DEFAULT NULL,
  `visual_rut` varchar(150) NOT NULL,
  `contract_type_id` int(11) DEFAULT NULL,
  `branch_office_id` int(11) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `region_id` int(11) DEFAULT NULL,
  `commune_id` int(11) DEFAULT NULL,
  `civil_state_id` int(11) DEFAULT NULL,
  `health_id` int(11) DEFAULT NULL,
  `pention_id` int(11) DEFAULT NULL,
  `job_position_id` int(11) DEFAULT NULL,
  `entrance_company` date DEFAULT NULL,
  `exit_company` date DEFAULT NULL,
  `salary` int(11) DEFAULT NULL,
  `collation` int(11) DEFAULT NULL,
  `locomotion` int(11) DEFAULT NULL,
  `added_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `employee_labor_data`
--

INSERT INTO `employee_labor_data` (`id`, `rut`, `visual_rut`, `contract_type_id`, `branch_office_id`, `address`, `region_id`, `commune_id`, `civil_state_id`, `health_id`, `pention_id`, `job_position_id`, `entrance_company`, `exit_company`, `salary`, `collation`, `locomotion`, `added_date`, `updated_date`) VALUES
(1, 55555, '55555', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(2, 2222, '2222', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2022-11-16 15:24:37', NULL),
(3, 14587987, '14587987', NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, '2022-11-16 15:28:33', NULL),
(4, 18456789, '18456789-8', 2, 3, '2323', 2, 0, 2, 12, 3, 4, '2022-12-02', '2022-11-26', 123456, 11, 1234, '2022-11-16 16:12:58', '2022-11-17 10:17:18'),
(5, 0, '', 1, 108, '2323', 2, 0, 2, 8, 2, 28, '2022-11-18', '2022-11-24', 21323, 232, 32323, '2022-11-17 09:59:46', '2022-11-17 09:59:46');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `family_burdens`
--

CREATE TABLE `family_burdens` (
  `family_burden_id` int(150) NOT NULL,
  `family_burden` varchar(255) NOT NULL,
  `added_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `family_core_data`
--

CREATE TABLE `family_core_data` (
  `id` int(150) NOT NULL,
  `family_type_id` int(150) NOT NULL,
  `rut_user` int(150) NOT NULL,
  `gender_id` int(150) NOT NULL,
  `rut` varchar(255) NOT NULL,
  `names` varchar(255) NOT NULL,
  `father_lastname` varchar(255) NOT NULL,
  `mother_lastname` varchar(255) NOT NULL,
  `born_date` datetime NOT NULL,
  `support` varchar(255) NOT NULL,
  `added_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `family_core_data`
--

INSERT INTO `family_core_data` (`id`, `family_type_id`, `rut_user`, `gender_id`, `rut`, `names`, `father_lastname`, `mother_lastname`, `born_date`, `support`, `added_date`) VALUES
(10, 0, 18456789, 1, '232', '323', '232', '2323', '2022-11-05 00:00:00', '', '2022-11-21 08:05:02'),
(11, 0, 18456789, 1, '232', '3232', '323', '2323', '2022-11-04 00:00:00', '', '2022-11-21 08:05:28'),
(13, 2, 18456789, 1, '111111', '3232', '232', '3232', '0000-00-00 00:00:00', '', '2022-11-21 08:06:50'),
(14, 4, 18456789, 1, 'qqq', 'bbbbb', '2323', '232', '0000-00-00 00:00:00', '', '2022-11-21 08:07:36');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `family_types`
--

CREATE TABLE `family_types` (
  `id` int(150) NOT NULL,
  `family_type` varchar(255) NOT NULL,
  `added_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `family_types`
--

INSERT INTO `family_types` (`id`, `family_type`, `added_date`) VALUES
(1, 'Conyugue', '2022-11-17 15:07:42'),
(2, 'Hijo(a)', '2022-11-17 15:07:42'),
(3, 'Padre', '2022-11-17 15:07:42'),
(4, 'Madre', '2022-11-17 15:07:42');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `genders`
--

CREATE TABLE `genders` (
  `id` int(11) NOT NULL,
  `gender` varchar(255) DEFAULT NULL,
  `added_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `genders`
--

INSERT INTO `genders` (`id`, `gender`, `added_date`, `updated_date`) VALUES
(1, 'Masculino', '2022-11-14 15:04:15', '2022-11-14 15:04:15'),
(2, 'Femenino', '2022-11-14 15:04:15', '2022-11-14 15:04:15');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `healths`
--

CREATE TABLE `healths` (
  `id` int(11) NOT NULL,
  `health` varchar(255) DEFAULT NULL,
  `health_remuneration_code` int(11) DEFAULT NULL,
  `rut` varchar(20) DEFAULT NULL,
  `previred_code` int(11) DEFAULT NULL,
  `added_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `healths`
--

INSERT INTO `healths` (`id`, `health`, `health_remuneration_code`, `rut`, `previred_code`, `added_date`, `updated_date`) VALUES
(1, 'Consalud', 9, '96856780-2', 2, NULL, NULL),
(2, 'Fonasa', 102, '61603000-0 ', 7, NULL, NULL),
(3, 'Banmedica', 3, '96572800-7 ', 1, NULL, NULL),
(4, 'Colmena', 4, '76296619-0', 4, NULL, NULL),
(5, 'Cruz Blanca', 1, '96501450-0 ', 5, NULL, NULL),
(6, 'Mas Vida', 43, '96504160-5 ', 10, NULL, NULL),
(7, 'Óptima', 0, NULL, NULL, NULL, NULL),
(8, 'VidaTres', 12, '96502530-8', 3, NULL, NULL),
(9, 'Dipreca', 0, NULL, NULL, NULL, NULL),
(10, 'Rio Blanco', 41, NULL, NULL, NULL, NULL),
(11, 'Cruz del Norte', 38, '79906120-1', 25, NULL, NULL),
(12, 'San Lorenzo', 42, NULL, NULL, NULL, NULL),
(13, 'Chuquicamata', 37, NULL, NULL, NULL, NULL),
(14, 'Inst S.P.F', 0, NULL, NULL, NULL, NULL),
(15, 'Fund Bco. Estado', 40, '71235700-2 ', 12, NULL, NULL),
(16, 'Isapre Codelco', 0, '76334370-7', 11, NULL, NULL),
(17, 'Isapre Bancoestado', 0, '71235700-2', 12, NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `job_positions`
--

CREATE TABLE `job_positions` (
  `id` int(11) NOT NULL,
  `job_position` varchar(255) NOT NULL,
  `functions` varchar(255) NOT NULL,
  `added_date` datetime NOT NULL,
  `updated_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `job_positions`
--

INSERT INTO `job_positions` (`id`, `job_position`, `functions`, `added_date`, `updated_date`) VALUES
(1, 'Asistente Administrativo', '', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(2, 'Supervisor', '', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(3, 'Gerente General', 'Administración y representación de la empresa. Ejecución de políticas y directrices de la compañía determinadas por el directorio', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(4, 'Gerente de Operaciones', 'Organizar y administrar la cadena de sucursales con la finalidad de aumentar las ventas, maximizar la rentabilidad de la empresa y buscar la satisfacción del cliente brindando el mejor servicio', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(5, 'Personal de Aseo', '', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(6, 'Trabajador Multifuncional Parcial 10 hrs', 'Función de Caja, Auxiliar de patio y en general tareas asociadas al funcionamiento del establecimiento', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(7, 'Trabajador Multifuncional Parcial 20 hrs', 'Función de Caja, Auxiliar de patio y en general tareas asociadas al funcionamiento del establecimiento.\r\n', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(8, 'Trabajador Multifuncional Parcial 25 hrs', 'Función de Caja, Auxiliar de patio y en general tareas asociadas al funcionamiento del establecimiento', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(9, 'Trabajador Multifuncional Parcial 30 hrs', 'Función de Caja, Auxiliar de patio y en general tareas asociadas al funcionamiento del establecimiento', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(10, 'Trabajador Multifuncional', 'Función de Caja, Auxiliar de patio y en general tareas asociadas al funcionamiento del establecimiento', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(11, 'Analista Contable', 'Alto nivel de experiencia en el registro periódico todos los hechos económicos en que incurre la empresa y su ingreso en los libros de contabilidad, proporcionando información para la elaboración de los informes contables', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(12, 'Encargado de Sucursal', 'Lograr los resultados de venta asignados, buscando mantener un alto nivel de servicio a los clientes', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(13, 'Gerente de Planificación y Control de Gestión', 'Coordinar y supervisar la elaboración, control, análisis y gestión de los distintos presupuestos confeccionados en la empresa, velando por la correcta administración e imputación de partidas sobre estos', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(14, 'Analista Senior de Planificación y Control de Gestión', 'Contribuir en la elaboración, control, análisis y gestión de los distintos presupuestos confeccionados en la empresa, de acuerdo a las directrices establecidas. Confección de informes de gestión para la Gerencia', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(15, 'Gerente de Recursos Humanos', 'Apoyar los planes estratégicos y operativos de la empresa proveyendo las herramientas de administración de recursos humanos para la gestión de cada una de las gerencias de la compañía', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(16, 'Técnico en Mantención', 'Apoyar a la Gerencia de Operaciones en la mantención de las sucursales de forma preventiva y correctiva. Apoyar a la Gerencia de Operaciones en las reparaciones de infraestructura y mantención de las sucursales en buen funcionamiento. Atender a las sucurs', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(17, 'Prevencionista de Riesgos', 'Planificar, organizar, asesorar, ejecutar, supervisar y promover acciones permanentes para evitar accidentes de trabajo y enfermedades profesionales', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(18, 'Analista Junior', 'Registrar periódicamente todos los hechos económicos en que incurre la empresa e ingresarlos en los libros de contabilidad, proporcionando información para la elaboración de los informes contables', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(19, 'Encargada de Personal y Remuneraciones', 'Llevar a cabo el proceso de pago de las remuneraciones del personal de la empresa, velando por el cumplimiento de las obligaciones contractuales adquiridas y la correcta aplicación de la legislación laboral vigente', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(20, 'Contador General', 'Coordinar de manera eficiente y oportuna la gestión operativa del área contable y financiera de la empresa. Gestionar los procesos contables de las distintas cuentas administradas por la empresa, a fin de ejecutar los programas previstos y dar solución a ', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(21, 'Gerente de Mantencion', '', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(22, 'Jefe de Operaciones', 'Organizar y administrar la cadena de sucursales con la finalidad de aumentar las ventas, maximizar la rentabilidad de la\r\nempresa y buscar la satisfacción del cliente brindando el mejor servicio.', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(23, 'Asistente de Recursos Humanos', 'Procesar datos de la asistencia diaria del personal, elaborando los informes correspondientes. Preparar y despachar  a sucursales registro de asistencia, faltas, retrasos etc. Cumplir los lineamientos del sistema de gestión de calidad. ', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(24, 'Ingeniero de Proyectos Web', 'Responsable del diseño, desarrollo, implementación, integración y mantención del software. componentes o subconjuntos de software (clases, módulos, pantallas, rutinas, subsistemas, programas en general) conforme a especificaciones (funcionales y técnicas)', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(25, 'Coordinadora de Comunicaciones', '', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(26, 'Diseñador Gráfico', '', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(27, 'Encargada de Área', '', '0000-00-00 00:00:00', '0000-00-00 00:00:00'),
(28, 'Encargado de Mantención', '', '0000-00-00 00:00:00', '0000-00-00 00:00:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `letter_informations`
--

CREATE TABLE `letter_informations` (
  `id` int(11) NOT NULL,
  `document_employee_id` int(255) NOT NULL,
  `letter_type_id` int(255) NOT NULL,
  `description` text NOT NULL,
  `date` datetime NOT NULL,
  `added_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `letter_types`
--

CREATE TABLE `letter_types` (
  `id` int(11) NOT NULL,
  `letter_type` varchar(255) NOT NULL,
  `added_date` datetime NOT NULL,
  `updated_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `letter_types`
--

INSERT INTO `letter_types` (`id`, `letter_type`, `added_date`, `updated_date`) VALUES
(1, 'Carta de Amonestación', '2022-11-15 21:49:36', '2022-11-15 21:49:36'),
(2, 'Carta de Felicitación', '2022-11-15 21:49:36', '2022-11-15 21:49:36'),
(3, 'Carta de Término (Necesidades de la Empresa)', '2022-11-15 21:49:36', '2022-11-15 21:49:36'),
(4, 'Carta de Término (No Concurrencia)', '2022-11-15 21:49:36', '2022-11-15 21:49:36'),
(5, 'Carta de Término (Vencimiento de Plazo)', '2022-11-15 21:49:36', '2022-11-15 21:49:36');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `nationalities`
--

CREATE TABLE `nationalities` (
  `id` int(11) NOT NULL,
  `nationality` varchar(255) DEFAULT NULL,
  `previred_code` varchar(150) NOT NULL,
  `added_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `nationalities`
--

INSERT INTO `nationalities` (`id`, `nationality`, `previred_code`, `added_date`, `updated_date`) VALUES
(1, 'Chileno (a)', '0', NULL, NULL),
(2, 'Colombiano (a)', '1', NULL, NULL),
(3, 'Haitiano (a)', '1', NULL, NULL),
(4, 'Paraguayo (a)', '1', NULL, NULL),
(5, 'Venezolano (a)', '1', NULL, NULL),
(6, 'Boliviano (a)', '1', NULL, NULL),
(7, 'Peruano (a)', '1', NULL, NULL),
(8, 'Ecuatoriano (a)', '1', NULL, NULL),
(9, 'Cubano (a)', '1', NULL, NULL),
(10, 'Argentino (a)', '1', NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pentions`
--

CREATE TABLE `pentions` (
  `id` int(11) NOT NULL,
  `pention` varchar(255) DEFAULT NULL,
  `pention_remuneration_code` int(11) DEFAULT NULL,
  `rut` varchar(20) DEFAULT NULL,
  `previred_code` int(11) DEFAULT NULL,
  `added_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `pentions`
--

INSERT INTO `pentions` (`id`, `pention`, `pention_remuneration_code`, `rut`, `previred_code`, `added_date`, `updated_date`) VALUES
(1, 'Sin AFP', 0, NULL, 0, NULL, NULL),
(2, 'Cuprum', 13, NULL, 3, NULL, NULL),
(3, 'Habitat', 14, NULL, 5, NULL, NULL),
(4, 'Plan Vital', 11, NULL, 29, NULL, NULL),
(5, 'Provida', 6, NULL, 8, NULL, NULL),
(6, 'Capital', 31, NULL, 33, NULL, NULL),
(7, 'Modelo', 103, NULL, 34, NULL, NULL),
(8, 'Uno', 19, NULL, 35, NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `principal`
--

CREATE TABLE `principal` (
  `principal_id` int(11) NOT NULL,
  `principal` varchar(255) DEFAULT NULL,
  `added_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `puntuality_annexed_documents`
--

CREATE TABLE `puntuality_annexed_documents` (
  `id` int(11) NOT NULL,
  `document_employee_id` int(255) NOT NULL,
  `asignation` varchar(255) NOT NULL,
  `added_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `regions`
--

CREATE TABLE `regions` (
  `id` int(11) NOT NULL,
  `region` varchar(255) DEFAULT NULL,
  `region_remuneration_code` int(11) DEFAULT NULL,
  `added_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `regions`
--

INSERT INTO `regions` (`id`, `region`, `region_remuneration_code`, `added_date`, `updated_date`) VALUES
(1, 'Tarapacá', NULL, NULL, NULL),
(2, 'Antofagasta', NULL, NULL, NULL),
(3, 'Atacama', NULL, NULL, NULL),
(4, 'Coquimbo', NULL, NULL, NULL),
(5, 'Valparaiso', NULL, NULL, NULL),
(6, 'Libertador General Bernardo O\'Higgins', NULL, NULL, NULL),
(7, 'Maule', NULL, NULL, NULL),
(8, 'Biobío', NULL, NULL, NULL),
(9, 'La Araucanía', NULL, NULL, NULL),
(10, 'Los Lagos', NULL, NULL, NULL),
(11, 'Aisén del General Carlos Ibáñez del Campo', NULL, NULL, NULL),
(12, 'Magallanes y de la Antártica Chilena', NULL, NULL, NULL),
(13, 'Metropolitana de Santiago', NULL, NULL, NULL),
(14, 'Los Ríos', NULL, NULL, NULL),
(15, 'Arica y Parinacota', NULL, NULL, NULL),
(16, 'Ñuble', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rols`
--

CREATE TABLE `rols` (
  `id` int(11) NOT NULL,
  `rol` varchar(255) DEFAULT NULL,
  `added_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `rols`
--

INSERT INTO `rols` (`id`, `rol`, `added_date`, `updated_date`) VALUES
(1, 'Colaborador', '2022-11-14 15:06:45', '2022-11-14 15:06:45');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `segment`
--

CREATE TABLE `segment` (
  `segment_id` int(11) NOT NULL,
  `segment` varchar(255) DEFAULT NULL,
  `added_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `supervisor`
--

CREATE TABLE `supervisor` (
  `id` int(11) NOT NULL,
  `branch_office_id` int(11) DEFAULT NULL,
  `rut` varchar(20) DEFAULT NULL,
  `added_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `rol_id` int(11) DEFAULT NULL,
  `rut` int(150) DEFAULT NULL,
  `visual_rut` varchar(150) NOT NULL,
  `nickname` varchar(255) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `added_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `rol_id`, `rut`, `visual_rut`, `nickname`, `email`, `password`, `added_date`, `updated_date`) VALUES
(2, 1, 271413998, '27141399-8', 'Jesus Cova', NULL, 'pbkdf2:sha256:260000$LmXaOX6SU376XpnO$628793fe4ff2e1755cb3c2ab272b78e7f192d1fc5b6500d5dcc21d5e48577545', '2022-11-14 11:07:00', '2022-11-14 11:07:00'),
(3, 1, 15456789, '15456789-8', 'Nombres Apeli', '222@k.com3', 'pbkdf2:sha256:260000$qWWCMlo7jKXnknwy$89b6b2098d1ee733de94f4f78743eb937513f1ea08e1bd04eb917c8ecb5bf3a9', '2022-11-16 16:15:29', '2022-11-16 16:15:29');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `zone`
--

CREATE TABLE `zone` (
  `zone_id` int(11) NOT NULL,
  `zone` varchar(255) DEFAULT NULL,
  `added_date` datetime DEFAULT NULL,
  `updated_date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `abandon_day_documents`
--
ALTER TABLE `abandon_day_documents`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indices de la tabla `audits`
--
ALTER TABLE `audits`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `branch_offices`
--
ALTER TABLE `branch_offices`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `branch_office_transbanks`
--
ALTER TABLE `branch_office_transbanks`
  ADD PRIMARY KEY (`branch_office_transbank_id`),
  ADD UNIQUE KEY `branch_office_id` (`branch_office_id`);

--
-- Indices de la tabla `civil_states`
--
ALTER TABLE `civil_states`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `communes`
--
ALTER TABLE `communes`
  ADD PRIMARY KEY (`commune_id`);

--
-- Indices de la tabla `contract_type`
--
ALTER TABLE `contract_type`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `contract_update_documents`
--
ALTER TABLE `contract_update_documents`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `documents_employees`
--
ALTER TABLE `documents_employees`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `documents_group`
--
ALTER TABLE `documents_group`
  ADD PRIMARY KEY (`documents_group_id`);

--
-- Indices de la tabla `document_types`
--
ALTER TABLE `document_types`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `employees`
--
ALTER TABLE `employees`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `employee_labor_data`
--
ALTER TABLE `employee_labor_data`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `family_burdens`
--
ALTER TABLE `family_burdens`
  ADD PRIMARY KEY (`family_burden_id`);

--
-- Indices de la tabla `family_core_data`
--
ALTER TABLE `family_core_data`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `family_types`
--
ALTER TABLE `family_types`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `genders`
--
ALTER TABLE `genders`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `healths`
--
ALTER TABLE `healths`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `job_positions`
--
ALTER TABLE `job_positions`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `letter_informations`
--
ALTER TABLE `letter_informations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `letter_types`
--
ALTER TABLE `letter_types`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `nationalities`
--
ALTER TABLE `nationalities`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `pentions`
--
ALTER TABLE `pentions`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `principal`
--
ALTER TABLE `principal`
  ADD PRIMARY KEY (`principal_id`);

--
-- Indices de la tabla `regions`
--
ALTER TABLE `regions`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `rols`
--
ALTER TABLE `rols`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `segment`
--
ALTER TABLE `segment`
  ADD PRIMARY KEY (`segment_id`);

--
-- Indices de la tabla `supervisor`
--
ALTER TABLE `supervisor`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD KEY `rol_id` (`rol_id`);

--
-- Indices de la tabla `zone`
--
ALTER TABLE `zone`
  ADD PRIMARY KEY (`zone_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `abandon_day_documents`
--
ALTER TABLE `abandon_day_documents`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `audits`
--
ALTER TABLE `audits`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT de la tabla `branch_offices`
--
ALTER TABLE `branch_offices`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=109;

--
-- AUTO_INCREMENT de la tabla `branch_office_transbanks`
--
ALTER TABLE `branch_office_transbanks`
  MODIFY `branch_office_transbank_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `civil_states`
--
ALTER TABLE `civil_states`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `communes`
--
ALTER TABLE `communes`
  MODIFY `commune_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `contract_type`
--
ALTER TABLE `contract_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `contract_update_documents`
--
ALTER TABLE `contract_update_documents`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `documents_employees`
--
ALTER TABLE `documents_employees`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT de la tabla `documents_group`
--
ALTER TABLE `documents_group`
  MODIFY `documents_group_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `document_types`
--
ALTER TABLE `document_types`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=121;

--
-- AUTO_INCREMENT de la tabla `employees`
--
ALTER TABLE `employees`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=211;

--
-- AUTO_INCREMENT de la tabla `employee_labor_data`
--
ALTER TABLE `employee_labor_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `family_burdens`
--
ALTER TABLE `family_burdens`
  MODIFY `family_burden_id` int(150) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `family_core_data`
--
ALTER TABLE `family_core_data`
  MODIFY `id` int(150) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `family_types`
--
ALTER TABLE `family_types`
  MODIFY `id` int(150) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `genders`
--
ALTER TABLE `genders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `healths`
--
ALTER TABLE `healths`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT de la tabla `job_positions`
--
ALTER TABLE `job_positions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT de la tabla `letter_informations`
--
ALTER TABLE `letter_informations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `letter_types`
--
ALTER TABLE `letter_types`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `nationalities`
--
ALTER TABLE `nationalities`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `pentions`
--
ALTER TABLE `pentions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `principal`
--
ALTER TABLE `principal`
  MODIFY `principal_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `rols`
--
ALTER TABLE `rols`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `segment`
--
ALTER TABLE `segment`
  MODIFY `segment_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `supervisor`
--
ALTER TABLE `supervisor`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `zone`
--
ALTER TABLE `zone`
  MODIFY `zone_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`rol_id`) REFERENCES `rols` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
