-- Adminer 4.8.1 MySQL 9.0.1 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `Dvd`;
CREATE TABLE `Dvd` (
  `code` varchar(15) NOT NULL,
  `salle` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `titre` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `auteur` varchar(25) NOT NULL,
  `sur_place` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'no',
  `online` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'no',
  `debut_emprunt` date NOT NULL DEFAULT '1971-01-01',
  `fin_emprunt` date NOT NULL DEFAULT '1971-01-01',
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Dvd` (`code`, `salle`, `titre`, `auteur`, `sur_place`, `online`, `debut_emprunt`, `fin_emprunt`) VALUES
('1',	'8D-121',	'star wars 2',	'JK',	'no',	'no',	'1971-01-01',	'1971-01-01');

DROP TABLE IF EXISTS `Journal`;
CREATE TABLE `Journal` (
  `code` varchar(15) NOT NULL,
  `salle` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `titre` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `date_publication` date NOT NULL,
  `sur_place` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'no',
  `online` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'no',
  `debut_emprunt` date NOT NULL DEFAULT '1971-01-01',
  `fin_emprunt` date NOT NULL DEFAULT '1971-01-01',
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Journal` (`code`, `salle`, `titre`, `date_publication`, `sur_place`, `online`, `debut_emprunt`, `fin_emprunt`) VALUES
('2',	'8D-120',	'La troisièmes vague ?',	'2021-09-05',	'no',	'no',	'1971-01-01',	'1971-01-01');

DROP TABLE IF EXISTS `Livre`;
CREATE TABLE `Livre` (
  `code` varchar(15) NOT NULL,
  `salle` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `titre` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `auteur` varchar(25) NOT NULL,
  `sur_place` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'no',
  `online` varchar(25) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL DEFAULT 'no',
  `debut_emprunt` date NOT NULL DEFAULT '1971-01-01',
  `fin_emprunt` date NOT NULL DEFAULT '1971-01-01',
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Livre` (`code`, `salle`, `titre`, `auteur`, `sur_place`, `online`, `debut_emprunt`, `fin_emprunt`) VALUES
('3',	'4C-32',	'OOP python',	'AI',	'no',	'no',	'1971-01-01',	'1971-01-01');

DROP TABLE IF EXISTS `Personne`;
CREATE TABLE `Personne` (
  `num` varchar(15) NOT NULL,
  `perm` varchar(15) NOT NULL,
  `nom` varchar(15) NOT NULL,
  `prenom` varchar(15) NOT NULL,
  `login` varchar(15) NOT NULL,
  `password` varchar(25) NOT NULL,
  PRIMARY KEY (`num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `Personne` (`num`, `perm`, `nom`, `prenom`, `login`, `password`) VALUES
('52300555',	'admin',	'djetic',	'alexandre',	'adjetic',	'wm7ze*2b'),
('55100896',	'usager',	'Chalvin',	'Axel',	'axel',	'axel');

DROP TABLE IF EXISTS `attente`;
CREATE TABLE `attente` (
  `id` int NOT NULL AUTO_INCREMENT,
  `num` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `num_livre` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `num_dvd` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `num_journal` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `num` (`num`),
  KEY `num_livre` (`num_livre`),
  KEY `num_dvd` (`num_dvd`),
  KEY `num_journal` (`num_journal`),
  CONSTRAINT `attente_ibfk_1` FOREIGN KEY (`num`) REFERENCES `Personne` (`num`),
  CONSTRAINT `attente_ibfk_2` FOREIGN KEY (`num_livre`) REFERENCES `Livre` (`code`),
  CONSTRAINT `attente_ibfk_3` FOREIGN KEY (`num`) REFERENCES `Personne` (`num`),
  CONSTRAINT `attente_ibfk_4` FOREIGN KEY (`num_livre`) REFERENCES `Livre` (`code`),
  CONSTRAINT `attente_ibfk_5` FOREIGN KEY (`num_dvd`) REFERENCES `Dvd` (`code`),
  CONSTRAINT `attente_ibfk_6` FOREIGN KEY (`num_journal`) REFERENCES `Journal` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `emprunt`;
CREATE TABLE `emprunt` (
  `id` int NOT NULL AUTO_INCREMENT,
  `num` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `num_li` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `num_dvd` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `num_journal` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `num` (`num`),
  KEY `num_li` (`num_li`),
  KEY `num_dvd` (`num_dvd`),
  KEY `num_journal` (`num_journal`),
  CONSTRAINT `emprunt_ibfk_1` FOREIGN KEY (`id`) REFERENCES `attente` (`id`),
  CONSTRAINT `emprunt_ibfk_2` FOREIGN KEY (`num`) REFERENCES `Personne` (`num`),
  CONSTRAINT `emprunt_ibfk_3` FOREIGN KEY (`num_li`) REFERENCES `Livre` (`code`),
  CONSTRAINT `emprunt_ibfk_4` FOREIGN KEY (`num_dvd`) REFERENCES `Dvd` (`code`),
  CONSTRAINT `emprunt_ibfk_5` FOREIGN KEY (`num_journal`) REFERENCES `Journal` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `retard_rendue`;
CREATE TABLE `retard_rendue` (
  `id` int NOT NULL AUTO_INCREMENT,
  `num` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `num_li` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `num_dvd` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `num_journal` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `num` (`num`),
  KEY `num_li` (`num_li`),
  KEY `num_dvd` (`num_dvd`),
  KEY `num_journal` (`num_journal`),
  CONSTRAINT `retard_rendue_ibfk_1` FOREIGN KEY (`id`) REFERENCES `attente` (`id`),
  CONSTRAINT `retard_rendue_ibfk_2` FOREIGN KEY (`num`) REFERENCES `Personne` (`num`),
  CONSTRAINT `retard_rendue_ibfk_3` FOREIGN KEY (`num_li`) REFERENCES `Livre` (`code`),
  CONSTRAINT `retard_rendue_ibfk_4` FOREIGN KEY (`num_dvd`) REFERENCES `Dvd` (`code`),
  CONSTRAINT `retard_rendue_ibfk_5` FOREIGN KEY (`num_journal`) REFERENCES `Journal` (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


-- 2024-09-30 10:36:03

