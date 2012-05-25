-- MySQL dump 10.13  Distrib 5.5.21, for Linux (x86_64)
--
-- Host: localhost    Database: providerprofile
-- ------------------------------------------------------
-- Server version		 5.5.21-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `active_table`
--

DROP TABLE IF EXISTS `active_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `active_table` (
  `name` char(1) NOT NULL,
  `updated_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `chapter_a`
--

DROP TABLE IF EXISTS `chapter_a`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chapter_a` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `chapter_id` varchar(30) NOT NULL,
  `chapter_score` int(11) DEFAULT NULL,
  `hashvalue` char(32) NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`location_id`,`chapter_id`),
  UNIQUE KEY `locid` (`location_id`,`chapter_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`chapter_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `chapter_b`
--

DROP TABLE IF EXISTS `chapter_b`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `chapter_b` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `chapter_id` varchar(30) NOT NULL,
  `chapter_score` int(11) DEFAULT NULL,
  `hashvalue` char(32) NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`location_id`,`chapter_id`),
  UNIQUE KEY `locid` (`location_id`,`chapter_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`chapter_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `compliance_condition_a`
--

DROP TABLE IF EXISTS `compliance_condition_a`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `compliance_condition_a` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `condition_id` varchar(30) NOT NULL,
  `regulated_activity_id` varchar(30) NOT NULL,
  `compliance_condition` longtext,
  `compliance_reason` longtext,
  `hashvalue` char(32) NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`location_id`,`condition_id`),
  UNIQUE KEY `locid` (`location_id`,`regulated_activity_id`,`condition_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`condition_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `compliance_condition_b`
--

DROP TABLE IF EXISTS `compliance_condition_b`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `compliance_condition_b` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `condition_id` varchar(30) NOT NULL,
  `regulated_activity_id` varchar(30) NOT NULL,
  `compliance_condition` longtext,
  `compliance_reason` longtext,
  `hashvalue` char(32) NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`location_id`,`condition_id`),
  UNIQUE KEY `locid` (`location_id`,`regulated_activity_id`,`condition_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`condition_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `cqc_address_cache`
--

DROP TABLE IF EXISTS `cqc_address_cache`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cqc_address_cache` (
  `lid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `street` varchar(255) NOT NULL DEFAULT '',
  `additional` varchar(255) NOT NULL DEFAULT '',
  `city` varchar(255) NOT NULL DEFAULT '',
  `province` varchar(255) NOT NULL DEFAULT '',
  `postal_code` varchar(16) NOT NULL DEFAULT '',
  `country` char(2) NOT NULL DEFAULT '',
  `latitude` decimal(10,8) NOT NULL DEFAULT '0.00000000',
  `longitude` decimal(10,8) NOT NULL DEFAULT '0.00000000',
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=126191 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `historicreport`
--

DROP TABLE IF EXISTS `historicreport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `historicreport` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `filename` varchar(512) NOT NULL,
  `csa_id` int(11) DEFAULT NULL,
  `report_date` date DEFAULT NULL,
  `report_id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`report_id`),
  KEY `provlocid` (`provider_id`,`location_id`)
) ENGINE=InnoDB AUTO_INCREMENT=19929 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `job_status`
--

DROP TABLE IF EXISTS `job_status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `job_status` (
  `job_id` varchar(15) NOT NULL,
  `stage1_status` varchar(15) NOT NULL,
  `stage2_status` varchar(15) NOT NULL,
  `last_updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`job_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `judgement_method_a`
--

DROP TABLE IF EXISTS `judgement_method_a`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `judgement_method_a` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `outcome_id` varchar(30) NOT NULL,
  `method_id` varchar(30) NOT NULL,
  `method_text` longtext,
  `hashvalue` char(32) NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`location_id`,`outcome_id`,`method_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`outcome_id`,`method_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `judgement_method_b`
--

DROP TABLE IF EXISTS `judgement_method_b`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `judgement_method_b` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `outcome_id` varchar(30) NOT NULL,
  `method_id` varchar(30) NOT NULL,
  `method_text` longtext,
  `hashvalue` char(32) NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`location_id`,`outcome_id`,`method_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`outcome_id`,`method_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `location_a`
--

DROP TABLE IF EXISTS `location_a`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `location_a` (
  `provider_id` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `location_id` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `location_name` longtext COLLATE utf8_unicode_ci,
  `in_process` varchar(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `location_type` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `location_local_authority` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `location_region` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `also_known_as` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `address1` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `address2` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `towncity` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `county` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `postcode` varchar(16) COLLATE utf8_unicode_ci DEFAULT NULL,
  `latitude` decimal(10,8) DEFAULT '0.00000000',
  `longitude` decimal(10,8) DEFAULT '0.00000000',
  `type_info_1` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `type_info_2` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `telephone` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `email` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `website` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `fax` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `under_review_text` longtext COLLATE utf8_unicode_ci,
  `location_user_experience` longtext COLLATE utf8_unicode_ci,
  `location_license_information` longtext COLLATE utf8_unicode_ci,
  `location_statement_date` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `location_statement_id` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `hashvalue` char(32) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`location_id`),
  KEY `provider_id` (`provider_id`,`location_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `location_b`
--

DROP TABLE IF EXISTS `location_b`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `location_b` (
  `provider_id` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `location_id` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `location_name` longtext COLLATE utf8_unicode_ci,
  `in_process` varchar(1) COLLATE utf8_unicode_ci DEFAULT NULL,
  `location_type` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `location_local_authority` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `location_region` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `also_known_as` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `address1` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `address2` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `towncity` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `county` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `postcode` varchar(16) COLLATE utf8_unicode_ci DEFAULT NULL,
  `latitude` decimal(10,8) DEFAULT '0.00000000',
  `longitude` decimal(10,8) DEFAULT '0.00000000',
  `type_info_1` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `type_info_2` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `telephone` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `email` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `website` varchar(100) COLLATE utf8_unicode_ci DEFAULT NULL,
  `fax` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `under_review_text` longtext COLLATE utf8_unicode_ci,
  `location_user_experience` longtext COLLATE utf8_unicode_ci,
  `location_license_information` longtext COLLATE utf8_unicode_ci,
  `location_statement_date` varchar(20) COLLATE utf8_unicode_ci DEFAULT NULL,
  `location_statement_id` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL,
  `hashvalue` char(32) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`location_id`),
  KEY `provider_id` (`provider_id`,`location_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `location_compliance_condition_a`
--

DROP TABLE IF EXISTS `location_compliance_condition_a`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `location_compliance_condition_a` (
  `provider_id` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `location_id` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `condition_id` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `regulated_activity_id` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `location_compliance_condition` longtext COLLATE utf8_unicode_ci,
  `location_compliance_reason` longtext COLLATE utf8_unicode_ci,
  `hashvalue` char(32) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`location_id`,`condition_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`condition_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `location_compliance_condition_b`
--

DROP TABLE IF EXISTS `location_compliance_condition_b`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `location_compliance_condition_b` (
  `provider_id` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `location_id` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `condition_id` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `regulated_activity_id` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `location_compliance_condition` longtext COLLATE utf8_unicode_ci,
  `location_compliance_reason` longtext COLLATE utf8_unicode_ci,
  `hashvalue` char(32) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`location_id`,`condition_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`condition_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary table structure for view `location_delete_a`
--

DROP TABLE IF EXISTS `location_delete_a`;
/*!50001 DROP VIEW IF EXISTS `location_delete_a`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `location_delete_a` (
  `provider_id` varchar(30),
  `location_id` varchar(30),
  `location_name` longtext,
  `in_process` varchar(1),
  `location_type` varchar(50),
  `location_local_authority` varchar(50),
  `location_region` varchar(50),
  `also_known_as` varchar(100),
  `address1` varchar(255),
  `address2` varchar(255),
  `towncity` varchar(255),
  `county` varchar(255),
  `postcode` varchar(16),
  `latitude` decimal(10,8),
  `longitude` decimal(10,8),
  `type_info_1` varchar(50),
  `type_info_2` varchar(50),
  `telephone` varchar(20),
  `email` varchar(100),
  `website` varchar(100),
  `fax` varchar(20),
  `under_review_text` longtext,
  `location_user_experience` longtext,
  `location_license_information` longtext,
  `location_statement_date` varchar(20),
  `location_statement_id` varchar(30),
  `hashvalue` char(32)
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `location_delete_b`
--

DROP TABLE IF EXISTS `location_delete_b`;
/*!50001 DROP VIEW IF EXISTS `location_delete_b`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `location_delete_b` (
  `provider_id` varchar(30),
  `location_id` varchar(30),
  `location_name` longtext,
  `in_process` varchar(1),
  `location_type` varchar(50),
  `location_local_authority` varchar(50),
  `location_region` varchar(50),
  `also_known_as` varchar(100),
  `address1` varchar(255),
  `address2` varchar(255),
  `towncity` varchar(255),
  `county` varchar(255),
  `postcode` varchar(16),
  `latitude` decimal(10,8),
  `longitude` decimal(10,8),
  `type_info_1` varchar(50),
  `type_info_2` varchar(50),
  `telephone` varchar(20),
  `email` varchar(100),
  `website` varchar(100),
  `fax` varchar(20),
  `under_review_text` longtext,
  `location_user_experience` longtext,
  `location_license_information` longtext,
  `location_statement_date` varchar(20),
  `location_statement_id` varchar(30),
  `hashvalue` char(32)
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `location_insert_a`
--

DROP TABLE IF EXISTS `location_insert_a`;
/*!50001 DROP VIEW IF EXISTS `location_insert_a`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `location_insert_a` (
  `provider_id` varchar(30),
  `location_id` varchar(30),
  `location_name` longtext,
  `in_process` varchar(1),
  `location_type` varchar(50),
  `location_local_authority` varchar(50),
  `location_region` varchar(50),
  `also_known_as` varchar(100),
  `address1` varchar(255),
  `address2` varchar(255),
  `towncity` varchar(255),
  `county` varchar(255),
  `postcode` varchar(16),
  `latitude` decimal(10,8),
  `longitude` decimal(10,8),
  `type_info_1` varchar(50),
  `type_info_2` varchar(50),
  `telephone` varchar(20),
  `email` varchar(100),
  `website` varchar(100),
  `fax` varchar(20),
  `under_review_text` longtext,
  `location_user_experience` longtext,
  `location_license_information` longtext,
  `location_statement_date` varchar(20),
  `location_statement_id` varchar(30),
  `hashvalue` char(32)
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `location_insert_b`
--

DROP TABLE IF EXISTS `location_insert_b`;
/*!50001 DROP VIEW IF EXISTS `location_insert_b`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `location_insert_b` (
  `provider_id` varchar(30),
  `location_id` varchar(30),
  `location_name` longtext,
  `in_process` varchar(1),
  `location_type` varchar(50),
  `location_local_authority` varchar(50),
  `location_region` varchar(50),
  `also_known_as` varchar(100),
  `address1` varchar(255),
  `address2` varchar(255),
  `towncity` varchar(255),
  `county` varchar(255),
  `postcode` varchar(16),
  `latitude` decimal(10,8),
  `longitude` decimal(10,8),
  `type_info_1` varchar(50),
  `type_info_2` varchar(50),
  `telephone` varchar(20),
  `email` varchar(100),
  `website` varchar(100),
  `fax` varchar(20),
  `under_review_text` longtext,
  `location_user_experience` longtext,
  `location_license_information` longtext,
  `location_statement_date` varchar(20),
  `location_statement_id` varchar(30),
  `hashvalue` char(32)
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `location_routine_condition_a`
--

DROP TABLE IF EXISTS `location_routine_condition_a`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `location_routine_condition_a` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `condition_id` varchar(30) NOT NULL,
  `regulated_activity_id` varchar(30) NOT NULL,
  `location_routine_condition` longtext,
  `hashvalue` char(32) NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`location_id`,`condition_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`condition_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `location_routine_condition_b`
--

DROP TABLE IF EXISTS `location_routine_condition_b`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `location_routine_condition_b` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `condition_id` varchar(30) NOT NULL,
  `regulated_activity_id` varchar(30) NOT NULL,
  `location_routine_condition` longtext,
  `hashvalue` char(32) NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`location_id`,`condition_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`condition_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary table structure for view `location_update_a`
--

DROP TABLE IF EXISTS `location_update_a`;
/*!50001 DROP VIEW IF EXISTS `location_update_a`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `location_update_a` (
  `provider_id` varchar(30),
  `location_id` varchar(30),
  `location_name` longtext,
  `in_process` varchar(1),
  `location_type` varchar(50),
  `location_local_authority` varchar(50),
  `location_region` varchar(50),
  `also_known_as` varchar(100),
  `address1` varchar(255),
  `address2` varchar(255),
  `towncity` varchar(255),
  `county` varchar(255),
  `postcode` varchar(16),
  `latitude` decimal(10,8),
  `longitude` decimal(10,8),
  `type_info_1` varchar(50),
  `type_info_2` varchar(50),
  `telephone` varchar(20),
  `email` varchar(100),
  `website` varchar(100),
  `fax` varchar(20),
  `under_review_text` longtext,
  `location_user_experience` longtext,
  `location_license_information` longtext,
  `location_statement_date` varchar(20),
  `location_statement_id` varchar(30),
  `hashvalue` char(32)
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `location_update_b`
--

DROP TABLE IF EXISTS `location_update_b`;
/*!50001 DROP VIEW IF EXISTS `location_update_b`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `location_update_b` (
  `provider_id` varchar(30),
  `location_id` varchar(30),
  `location_name` longtext,
  `in_process` varchar(1),
  `location_type` varchar(50),
  `location_local_authority` varchar(50),
  `location_region` varchar(50),
  `also_known_as` varchar(100),
  `address1` varchar(255),
  `address2` varchar(255),
  `towncity` varchar(255),
  `county` varchar(255),
  `postcode` varchar(16),
  `latitude` decimal(10,8),
  `longitude` decimal(10,8),
  `type_info_1` varchar(50),
  `type_info_2` varchar(50),
  `telephone` varchar(20),
  `email` varchar(100),
  `website` varchar(100),
  `fax` varchar(20),
  `under_review_text` longtext,
  `location_user_experience` longtext,
  `location_license_information` longtext,
  `location_statement_date` varchar(20),
  `location_statement_id` varchar(30),
  `hashvalue` char(32)
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `lookuptable`
--

DROP TABLE IF EXISTS `lookuptable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lookuptable` (
  `nid` int(11) NOT NULL,
  `pid` varchar(30) DEFAULT NULL,
  `lid` varchar(30) DEFAULT NULL,
  KEY `idxnid` (`nid`),
  KEY `idxpid` (`pid`),
  KEY `idxlid` (`lid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `nominated_individual_a`
--

DROP TABLE IF EXISTS `nominated_individual_a`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nominated_individual_a` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `regulated_activity_id` varchar(30) NOT NULL,
  `nominated_individual` longtext,
  `hashvalue` char(32) NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`location_id`,`regulated_activity_id`),
  UNIQUE KEY `locid` (`location_id`,`regulated_activity_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`regulated_activity_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `nominated_individual_b`
--

DROP TABLE IF EXISTS `nominated_individual_b`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nominated_individual_b` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `regulated_activity_id` varchar(30) NOT NULL,
  `nominated_individual` longtext,
  `hashvalue` char(32) NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`location_id`,`regulated_activity_id`),
  UNIQUE KEY `locid` (`location_id`,`regulated_activity_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`regulated_activity_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `outcome_a`
--

DROP TABLE IF EXISTS `outcome_a`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `outcome_a` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `outcome_id` varchar(30) NOT NULL,
  `judgement_id` varchar(30) DEFAULT NULL,
  `judgement_date` varchar(20) DEFAULT NULL,
  `judgement_reason` longtext,
  `judgement_user_experience` longtext,
  `judgement_other_evidence` longtext,
  `judgement_score_id` varchar(30) DEFAULT NULL,
  `outcome_statement_id` varchar(30) DEFAULT NULL,
  `judgement_summary` longtext,
  `hashvalue` char(32) NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`location_id`,`outcome_id`),
  UNIQUE KEY `locid` (`location_id`,`outcome_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`outcome_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `outcome_b`
--

DROP TABLE IF EXISTS `outcome_b`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `outcome_b` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `outcome_id` varchar(30) NOT NULL,
  `judgement_id` varchar(30) DEFAULT NULL,
  `judgement_date` varchar(20) DEFAULT NULL,
  `judgement_reason` longtext,
  `judgement_user_experience` longtext,
  `judgement_other_evidence` longtext,
  `judgement_score_id` varchar(30) DEFAULT NULL,
  `outcome_statement_id` varchar(30) DEFAULT NULL,
  `judgement_summary` longtext,
  `hashvalue` char(32) NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`location_id`,`outcome_id`),
  UNIQUE KEY `locid` (`location_id`,`outcome_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`outcome_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `partner_a`
--

DROP TABLE IF EXISTS `partner_a`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `partner_a` (
  `provider_id` varchar(30) NOT NULL,
  `partner_id` varchar(30) NOT NULL,
  `partner_name` longtext,
  `hashvalue` char(32) NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`partner_id`),
  KEY `provider_id` (`provider_id`,`partner_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `partner_b`
--

DROP TABLE IF EXISTS `partner_b`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `partner_b` (
  `provider_id` varchar(30) NOT NULL,
  `partner_id` varchar(30) NOT NULL,
  `partner_name` longtext,
  `hashvalue` char(32) NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`partner_id`),
  KEY `provider_id` (`provider_id`,`partner_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `provider_a`
--

DROP TABLE IF EXISTS `provider_a`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `provider_a` (
  `provider_id` varchar(30) NOT NULL,
  `provider_name` longtext,
  `in_process` varchar(1) DEFAULT NULL,
  `provider_type` varchar(50) DEFAULT NULL,
  `provider_local_authority` varchar(50) DEFAULT NULL,
  `provider_region` varchar(50) DEFAULT NULL,
  `also_known_as` varchar(100) DEFAULT NULL,
  `address1` varchar(255) DEFAULT NULL,
  `address2` varchar(255) DEFAULT NULL,
  `towncity` varchar(255) DEFAULT NULL,
  `county` varchar(255) DEFAULT NULL,
  `postcode` varchar(16) DEFAULT NULL,
  `latitude` decimal(10,8) DEFAULT '0.00000000',
  `longitude` decimal(10,8) DEFAULT '0.00000000',
  `type_info_1` varchar(50) DEFAULT NULL,
  `type_info_2` varchar(50) DEFAULT NULL,
  `under_review_text` longtext,
  `telephone` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `website` varchar(100) DEFAULT NULL,
  `fax` varchar(20) DEFAULT NULL,
  `is_partnership` varchar(1) DEFAULT NULL,
  `hashvalue` char(32) NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`),
  KEY `provider_id` (`provider_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `provider_b`
--

DROP TABLE IF EXISTS `provider_b`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `provider_b` (
  `provider_id` varchar(30) NOT NULL,
  `provider_name` longtext,
  `in_process` varchar(1) DEFAULT NULL,
  `provider_type` varchar(50) DEFAULT NULL,
  `provider_local_authority` varchar(50) DEFAULT NULL,
  `provider_region` varchar(50) DEFAULT NULL,
  `also_known_as` varchar(100) DEFAULT NULL,
  `address1` varchar(255) DEFAULT NULL,
  `address2` varchar(255) DEFAULT NULL,
  `towncity` varchar(255) DEFAULT NULL,
  `county` varchar(255) DEFAULT NULL,
  `postcode` varchar(16) DEFAULT NULL,
  `latitude` decimal(10,8) DEFAULT '0.00000000',
  `longitude` decimal(10,8) DEFAULT '0.00000000',
  `type_info_1` varchar(50) DEFAULT NULL,
  `type_info_2` varchar(50) DEFAULT NULL,
  `under_review_text` longtext,
  `telephone` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `website` varchar(100) DEFAULT NULL,
  `fax` varchar(20) DEFAULT NULL,
  `is_partnership` varchar(1) DEFAULT NULL,
  `hashvalue` char(32) NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`),
  KEY `provider_id` (`provider_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `provider_compliance_condition_a`
--

DROP TABLE IF EXISTS `provider_compliance_condition_a`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `provider_compliance_condition_a` (
  `provider_id` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `condition_id` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `regulated_activity_id` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `provider_compliance_condition` longtext COLLATE utf8_unicode_ci,
  `provider_compliance_reason` longtext COLLATE utf8_unicode_ci,
  `hashvalue` char(32) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`condition_id`,`regulated_activity_id`),
  KEY `provider_id` (`provider_id`,`condition_id`,`regulated_activity_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `provider_compliance_condition_b`
--

DROP TABLE IF EXISTS `provider_compliance_condition_b`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `provider_compliance_condition_b` (
  `provider_id` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `condition_id` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `regulated_activity_id` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `provider_compliance_condition` longtext COLLATE utf8_unicode_ci,
  `provider_compliance_reason` longtext COLLATE utf8_unicode_ci,
  `hashvalue` char(32) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`condition_id`,`regulated_activity_id`),
  KEY `provider_id` (`provider_id`,`condition_id`,`regulated_activity_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary table structure for view `provider_delete_a`
--

DROP TABLE IF EXISTS `provider_delete_a`;
/*!50001 DROP VIEW IF EXISTS `provider_delete_a`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `provider_delete_a` (
  `provider_id` varchar(30),
  `provider_name` longtext,
  `in_process` varchar(1),
  `provider_type` varchar(50),
  `provider_local_authority` varchar(50),
  `provider_region` varchar(50),
  `also_known_as` varchar(100),
  `address1` varchar(255),
  `address2` varchar(255),
  `towncity` varchar(255),
  `county` varchar(255),
  `postcode` varchar(16),
  `latitude` decimal(10,8),
  `longitude` decimal(10,8),
  `type_info_1` varchar(50),
  `type_info_2` varchar(50),
  `under_review_text` longtext,
  `telephone` varchar(20),
  `email` varchar(100),
  `website` varchar(100),
  `fax` varchar(20),
  `is_partnership` varchar(1),
  `hashvalue` char(32)
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `provider_delete_b`
--

DROP TABLE IF EXISTS `provider_delete_b`;
/*!50001 DROP VIEW IF EXISTS `provider_delete_b`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `provider_delete_b` (
  `provider_id` varchar(30),
  `provider_name` longtext,
  `in_process` varchar(1),
  `provider_type` varchar(50),
  `provider_local_authority` varchar(50),
  `provider_region` varchar(50),
  `also_known_as` varchar(100),
  `address1` varchar(255),
  `address2` varchar(255),
  `towncity` varchar(255),
  `county` varchar(255),
  `postcode` varchar(16),
  `latitude` decimal(10,8),
  `longitude` decimal(10,8),
  `type_info_1` varchar(50),
  `type_info_2` varchar(50),
  `under_review_text` longtext,
  `telephone` varchar(20),
  `email` varchar(100),
  `website` varchar(100),
  `fax` varchar(20),
  `is_partnership` varchar(1),
  `hashvalue` char(32)
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `provider_insert_a`
--

DROP TABLE IF EXISTS `provider_insert_a`;
/*!50001 DROP VIEW IF EXISTS `provider_insert_a`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `provider_insert_a` (
  `provider_id` varchar(30),
  `provider_name` longtext,
  `in_process` varchar(1),
  `provider_type` varchar(50),
  `provider_local_authority` varchar(50),
  `provider_region` varchar(50),
  `also_known_as` varchar(100),
  `address1` varchar(255),
  `address2` varchar(255),
  `towncity` varchar(255),
  `county` varchar(255),
  `postcode` varchar(16),
  `latitude` decimal(10,8),
  `longitude` decimal(10,8),
  `type_info_1` varchar(50),
  `type_info_2` varchar(50),
  `under_review_text` longtext,
  `telephone` varchar(20),
  `email` varchar(100),
  `website` varchar(100),
  `fax` varchar(20),
  `is_partnership` varchar(1),
  `hashvalue` char(32)
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `provider_insert_b`
--

DROP TABLE IF EXISTS `provider_insert_b`;
/*!50001 DROP VIEW IF EXISTS `provider_insert_b`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `provider_insert_b` (
  `provider_id` varchar(30),
  `provider_name` longtext,
  `in_process` varchar(1),
  `provider_type` varchar(50),
  `provider_local_authority` varchar(50),
  `provider_region` varchar(50),
  `also_known_as` varchar(100),
  `address1` varchar(255),
  `address2` varchar(255),
  `towncity` varchar(255),
  `county` varchar(255),
  `postcode` varchar(16),
  `latitude` decimal(10,8),
  `longitude` decimal(10,8),
  `type_info_1` varchar(50),
  `type_info_2` varchar(50),
  `under_review_text` longtext,
  `telephone` varchar(20),
  `email` varchar(100),
  `website` varchar(100),
  `fax` varchar(20),
  `is_partnership` varchar(1),
  `hashvalue` char(32)
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `provider_routine_condition_a`
--

DROP TABLE IF EXISTS `provider_routine_condition_a`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `provider_routine_condition_a` (
  `provider_id` varchar(30) NOT NULL,
  `condition_id` varchar(30) NOT NULL,
  `regulated_activity_id` varchar(30) NOT NULL,
  `provider_routine_condition` longtext,
  `hashvalue` char(32) NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`condition_id`,`regulated_activity_id`),
  KEY `provider_id` (`provider_id`,`condition_id`,`regulated_activity_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `provider_routine_condition_b`
--

DROP TABLE IF EXISTS `provider_routine_condition_b`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `provider_routine_condition_b` (
  `provider_id` varchar(30) NOT NULL,
  `condition_id` varchar(30) NOT NULL,
  `regulated_activity_id` varchar(30) NOT NULL,
  `provider_routine_condition` longtext,
  `hashvalue` char(32) NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`condition_id`,`regulated_activity_id`),
  KEY `provider_id` (`provider_id`,`condition_id`,`regulated_activity_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary table structure for view `provider_update_a`
--

DROP TABLE IF EXISTS `provider_update_a`;
/*!50001 DROP VIEW IF EXISTS `provider_update_a`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `provider_update_a` (
  `provider_id` varchar(30),
  `provider_name` longtext,
  `in_process` varchar(1),
  `provider_type` varchar(50),
  `provider_local_authority` varchar(50),
  `provider_region` varchar(50),
  `also_known_as` varchar(100),
  `address1` varchar(255),
  `address2` varchar(255),
  `towncity` varchar(255),
  `county` varchar(255),
  `postcode` varchar(16),
  `latitude` decimal(10,8),
  `longitude` decimal(10,8),
  `type_info_1` varchar(50),
  `type_info_2` varchar(50),
  `under_review_text` longtext,
  `telephone` varchar(20),
  `email` varchar(100),
  `website` varchar(100),
  `fax` varchar(20),
  `is_partnership` varchar(1),
  `hashvalue` char(32)
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `provider_update_b`
--

DROP TABLE IF EXISTS `provider_update_b`;
/*!50001 DROP VIEW IF EXISTS `provider_update_b`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `provider_update_b` (
  `provider_id` varchar(30),
  `provider_name` longtext,
  `in_process` varchar(1),
  `provider_type` varchar(50),
  `provider_local_authority` varchar(50),
  `provider_region` varchar(50),
  `also_known_as` varchar(100),
  `address1` varchar(255),
  `address2` varchar(255),
  `towncity` varchar(255),
  `county` varchar(255),
  `postcode` varchar(16),
  `latitude` decimal(10,8),
  `longitude` decimal(10,8),
  `type_info_1` varchar(50),
  `type_info_2` varchar(50),
  `under_review_text` longtext,
  `telephone` varchar(20),
  `email` varchar(100),
  `website` varchar(100),
  `fax` varchar(20),
  `is_partnership` varchar(1),
  `hashvalue` char(32)
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `registered_manager_a`
--

DROP TABLE IF EXISTS `registered_manager_a`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registered_manager_a` (
  `provider_id` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `location_id` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `regulated_activity_id` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `manager_id` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `manager_name` longtext COLLATE utf8_unicode_ci,
  `manager_condition` longtext COLLATE utf8_unicode_ci,
  `hashvalue` char(32) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`location_id`,`regulated_activity_id`,`manager_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`regulated_activity_id`,`manager_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `registered_manager_b`
--

DROP TABLE IF EXISTS `registered_manager_b`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `registered_manager_b` (
  `provider_id` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `location_id` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `regulated_activity_id` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `manager_id` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `manager_name` longtext COLLATE utf8_unicode_ci,
  `manager_condition` longtext COLLATE utf8_unicode_ci,
  `hashvalue` char(32) COLLATE utf8_unicode_ci NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`location_id`,`regulated_activity_id`,`manager_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`regulated_activity_id`,`manager_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `regulated_activity_a`
--

DROP TABLE IF EXISTS `regulated_activity_a`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `regulated_activity_a` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `regulated_activity_id` varchar(30) NOT NULL,
  `hashvalue` char(32) NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`location_id`,`regulated_activity_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`regulated_activity_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `regulated_activity_b`
--

DROP TABLE IF EXISTS `regulated_activity_b`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `regulated_activity_b` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `regulated_activity_id` varchar(30) NOT NULL,
  `hashvalue` char(32) NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`location_id`,`regulated_activity_id`),
  UNIQUE KEY `location_id` (`location_id`,`regulated_activity_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`regulated_activity_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `routine_condition_a`
--

DROP TABLE IF EXISTS `routine_condition_a`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `routine_condition_a` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `condition_id` varchar(30) NOT NULL,
  `regulated_activity_id` varchar(30) NOT NULL,
  `routine_condition` longtext,
  `hashvalue` char(32) NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`location_id`,`condition_id`),
  UNIQUE KEY `location_id` (`location_id`,`condition_id`,`regulated_activity_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`condition_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `routine_condition_b`
--

DROP TABLE IF EXISTS `routine_condition_b`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `routine_condition_b` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `condition_id` varchar(30) NOT NULL,
  `regulated_activity_id` varchar(30) NOT NULL,
  `routine_condition` longtext,
  `hashvalue` char(32) NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`location_id`,`condition_id`),
  UNIQUE KEY `location_id` (`location_id`,`condition_id`,`regulated_activity_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`condition_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `service_type_a`
--

DROP TABLE IF EXISTS `service_type_a`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `service_type_a` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `service_type_id` varchar(30) NOT NULL,
  `hashvalue` char(32) NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`location_id`,`service_type_id`),
  UNIQUE KEY `location_id` (`service_type_id`,`location_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`service_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `service_type_b`
--

DROP TABLE IF EXISTS `service_type_b`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `service_type_b` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `service_type_id` varchar(30) NOT NULL,
  `hashvalue` char(32) NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`location_id`,`service_type_id`),
  UNIQUE KEY `location_id` (`service_type_id`,`location_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`service_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `service_user_band_a`
--

DROP TABLE IF EXISTS `service_user_band_a`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `service_user_band_a` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `service_user_band_id` varchar(30) NOT NULL,
  `hashvalue` char(32) NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`location_id`,`service_user_band_id`),
  UNIQUE KEY `location_id` (`location_id`,`service_user_band_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`service_user_band_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `service_user_band_b`
--

DROP TABLE IF EXISTS `service_user_band_b`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `service_user_band_b` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `service_user_band_id` varchar(30) NOT NULL,
  `hashvalue` char(32) NOT NULL DEFAULT 'HASHVALUE',
  PRIMARY KEY (`provider_id`,`location_id`,`service_user_band_id`),
  UNIQUE KEY `location_id` (`location_id`,`service_user_band_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`service_user_band_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `variable`
--

DROP TABLE IF EXISTS `variable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `variable` (
  `name` varchar(128) NOT NULL DEFAULT '',
  `value` longtext NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `watchdog`
--

DROP TABLE IF EXISTS `watchdog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `watchdog` (
  `wid` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NOT NULL DEFAULT '0',
  `type` varchar(16) NOT NULL DEFAULT '',
  `message` longtext NOT NULL,
  `variables` longtext NOT NULL,
  `severity` tinyint(3) unsigned NOT NULL DEFAULT '0',
  `link` varchar(255) NOT NULL DEFAULT '',
  `location` text NOT NULL,
  `referer` text,
  `hostname` varchar(128) NOT NULL DEFAULT '',
  `timestamp` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`wid`),
  KEY `type` (`type`)
) ENGINE=InnoDB AUTO_INCREMENT=17072 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `websitelookupcategory`
--

DROP TABLE IF EXISTS `websitelookupcategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `websitelookupcategory` (
  `idWebsiteLookup` int(11) NOT NULL AUTO_INCREMENT,
  `LookupText` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idWebsiteLookup`)
) ENGINE=InnoDB AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `websitelookuptext`
--

DROP TABLE IF EXISTS `websitelookuptext`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `websitelookuptext` (
  `idWebsiteLookupText` int(11) NOT NULL AUTO_INCREMENT,
  `idWebsiteLookupCategory` int(11) NOT NULL,
  `KeyField` varchar(30) NOT NULL,
  `ValueField` longtext,
  PRIMARY KEY (`idWebsiteLookupText`),
  UNIQUE KEY `catkey` (`idWebsiteLookupCategory`,`KeyField`)
) ENGINE=InnoDB AUTO_INCREMENT=296 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Final view structure for view `location_delete_a`
--

/*!50001 DROP TABLE IF EXISTS `location_delete_a`*/;
/*!50001 DROP VIEW IF EXISTS `location_delete_a`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`quantum`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `location_delete_a` AS select `b`.`provider_id` AS `provider_id`,`b`.`location_id` AS `location_id`,`b`.`location_name` AS `location_name`,`b`.`in_process` AS `in_process`,`b`.`location_type` AS `location_type`,`b`.`location_local_authority` AS `location_local_authority`,`b`.`location_region` AS `location_region`,`b`.`also_known_as` AS `also_known_as`,`b`.`address1` AS `address1`,`b`.`address2` AS `address2`,`b`.`towncity` AS `towncity`,`b`.`county` AS `county`,`b`.`postcode` AS `postcode`,`b`.`latitude` AS `latitude`,`b`.`longitude` AS `longitude`,`b`.`type_info_1` AS `type_info_1`,`b`.`type_info_2` AS `type_info_2`,`b`.`telephone` AS `telephone`,`b`.`email` AS `email`,`b`.`website` AS `website`,`b`.`fax` AS `fax`,`b`.`under_review_text` AS `under_review_text`,`b`.`location_user_experience` AS `location_user_experience`,`b`.`location_license_information` AS `location_license_information`,`b`.`location_statement_date` AS `location_statement_date`,`b`.`location_!
 statement_id` AS `location_statement_id`,`b`.`hashvalue` AS `hashvalue` from `location_b` `b` where (not((`b`.`provider_id`,`b`.`location_id`) in (select `a`.`provider_id`,`a`.`location_id` from `location_a` `a`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `location_delete_b`
--

/*!50001 DROP TABLE IF EXISTS `location_delete_b`*/;
/*!50001 DROP VIEW IF EXISTS `location_delete_b`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`quantum`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `location_delete_b` AS select `a`.`provider_id` AS `provider_id`,`a`.`location_id` AS `location_id`,`a`.`location_name` AS `location_name`,`a`.`in_process` AS `in_process`,`a`.`location_type` AS `location_type`,`a`.`location_local_authority` AS `location_local_authority`,`a`.`location_region` AS `location_region`,`a`.`also_known_as` AS `also_known_as`,`a`.`address1` AS `address1`,`a`.`address2` AS `address2`,`a`.`towncity` AS `towncity`,`a`.`county` AS `county`,`a`.`postcode` AS `postcode`,`a`.`latitude` AS `latitude`,`a`.`longitude` AS `longitude`,`a`.`type_info_1` AS `type_info_1`,`a`.`type_info_2` AS `type_info_2`,`a`.`telephone` AS `telephone`,`a`.`email` AS `email`,`a`.`website` AS `website`,`a`.`fax` AS `fax`,`a`.`under_review_text` AS `under_review_text`,`a`.`location_user_experience` AS `location_user_experience`,`a`.`location_license_information` AS `location_license_information`,`a`.`location_statement_date` AS `location_statement_date`,`a`.`location_!
 statement_id` AS `location_statement_id`,`a`.`hashvalue` AS `hashvalue` from `location_a` `a` where (not((`a`.`provider_id`,`a`.`location_id`) in (select `b`.`provider_id`,`b`.`location_id` from `location_b` `b`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `location_insert_a`
--

/*!50001 DROP TABLE IF EXISTS `location_insert_a`*/;
/*!50001 DROP VIEW IF EXISTS `location_insert_a`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`quantum`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `location_insert_a` AS select `a`.`provider_id` AS `provider_id`,`a`.`location_id` AS `location_id`,`a`.`location_name` AS `location_name`,`a`.`in_process` AS `in_process`,`a`.`location_type` AS `location_type`,`a`.`location_local_authority` AS `location_local_authority`,`a`.`location_region` AS `location_region`,`a`.`also_known_as` AS `also_known_as`,`a`.`address1` AS `address1`,`a`.`address2` AS `address2`,`a`.`towncity` AS `towncity`,`a`.`county` AS `county`,`a`.`postcode` AS `postcode`,`a`.`latitude` AS `latitude`,`a`.`longitude` AS `longitude`,`a`.`type_info_1` AS `type_info_1`,`a`.`type_info_2` AS `type_info_2`,`a`.`telephone` AS `telephone`,`a`.`email` AS `email`,`a`.`website` AS `website`,`a`.`fax` AS `fax`,`a`.`under_review_text` AS `under_review_text`,`a`.`location_user_experience` AS `location_user_experience`,`a`.`location_license_information` AS `location_license_information`,`a`.`location_statement_date` AS `location_statement_date`,`a`.`location_!
 statement_id` AS `location_statement_id`,`a`.`hashvalue` AS `hashvalue` from `location_a` `a` where (not((`a`.`provider_id`,`a`.`location_id`) in (select `b`.`provider_id`,`b`.`location_id` from `location_b` `b`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `location_insert_b`
--

/*!50001 DROP TABLE IF EXISTS `location_insert_b`*/;
/*!50001 DROP VIEW IF EXISTS `location_insert_b`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`quantum`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `location_insert_b` AS select `b`.`provider_id` AS `provider_id`,`b`.`location_id` AS `location_id`,`b`.`location_name` AS `location_name`,`b`.`in_process` AS `in_process`,`b`.`location_type` AS `location_type`,`b`.`location_local_authority` AS `location_local_authority`,`b`.`location_region` AS `location_region`,`b`.`also_known_as` AS `also_known_as`,`b`.`address1` AS `address1`,`b`.`address2` AS `address2`,`b`.`towncity` AS `towncity`,`b`.`county` AS `county`,`b`.`postcode` AS `postcode`,`b`.`latitude` AS `latitude`,`b`.`longitude` AS `longitude`,`b`.`type_info_1` AS `type_info_1`,`b`.`type_info_2` AS `type_info_2`,`b`.`telephone` AS `telephone`,`b`.`email` AS `email`,`b`.`website` AS `website`,`b`.`fax` AS `fax`,`b`.`under_review_text` AS `under_review_text`,`b`.`location_user_experience` AS `location_user_experience`,`b`.`location_license_information` AS `location_license_information`,`b`.`location_statement_date` AS `location_statement_date`,`b`.`location_!
 statement_id` AS `location_statement_id`,`b`.`hashvalue` AS `hashvalue` from `location_b` `b` where (not((`b`.`provider_id`,`b`.`location_id`) in (select `a`.`provider_id`,`a`.`location_id` from `location_a` `a`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `location_update_a`
--

/*!50001 DROP TABLE IF EXISTS `location_update_a`*/;
/*!50001 DROP VIEW IF EXISTS `location_update_a`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`quantum`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `location_update_a` AS select `a`.`provider_id` AS `provider_id`,`a`.`location_id` AS `location_id`,`a`.`location_name` AS `location_name`,`a`.`in_process` AS `in_process`,`a`.`location_type` AS `location_type`,`a`.`location_local_authority` AS `location_local_authority`,`a`.`location_region` AS `location_region`,`a`.`also_known_as` AS `also_known_as`,`a`.`address1` AS `address1`,`a`.`address2` AS `address2`,`a`.`towncity` AS `towncity`,`a`.`county` AS `county`,`a`.`postcode` AS `postcode`,`a`.`latitude` AS `latitude`,`a`.`longitude` AS `longitude`,`a`.`type_info_1` AS `type_info_1`,`a`.`type_info_2` AS `type_info_2`,`a`.`telephone` AS `telephone`,`a`.`email` AS `email`,`a`.`website` AS `website`,`a`.`fax` AS `fax`,`a`.`under_review_text` AS `under_review_text`,`a`.`location_user_experience` AS `location_user_experience`,`a`.`location_license_information` AS `location_license_information`,`a`.`location_statement_date` AS `location_statement_date`,`a`.`location_!
 statement_id` AS `location_statement_id`,`a`.`hashvalue` AS `hashvalue` from (`location_a` `a` join `location_b` `b`) where ((`a`.`provider_id` = `b`.`provider_id`) and (`a`.`location_id` = `b`.`location_id`) and (`a`.`hashvalue` <> `b`.`hashvalue`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `location_update_b`
--

/*!50001 DROP TABLE IF EXISTS `location_update_b`*/;
/*!50001 DROP VIEW IF EXISTS `location_update_b`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`quantum`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `location_update_b` AS select `b`.`provider_id` AS `provider_id`,`b`.`location_id` AS `location_id`,`b`.`location_name` AS `location_name`,`b`.`in_process` AS `in_process`,`b`.`location_type` AS `location_type`,`b`.`location_local_authority` AS `location_local_authority`,`b`.`location_region` AS `location_region`,`b`.`also_known_as` AS `also_known_as`,`b`.`address1` AS `address1`,`b`.`address2` AS `address2`,`b`.`towncity` AS `towncity`,`b`.`county` AS `county`,`b`.`postcode` AS `postcode`,`b`.`latitude` AS `latitude`,`b`.`longitude` AS `longitude`,`b`.`type_info_1` AS `type_info_1`,`b`.`type_info_2` AS `type_info_2`,`b`.`telephone` AS `telephone`,`b`.`email` AS `email`,`b`.`website` AS `website`,`b`.`fax` AS `fax`,`b`.`under_review_text` AS `under_review_text`,`b`.`location_user_experience` AS `location_user_experience`,`b`.`location_license_information` AS `location_license_information`,`b`.`location_statement_date` AS `location_statement_date`,`b`.`location_!
 statement_id` AS `location_statement_id`,`b`.`hashvalue` AS `hashvalue` from (`location_a` `a` join `location_b` `b`) where ((`a`.`provider_id` = `b`.`provider_id`) and (`a`.`location_id` = `b`.`location_id`) and (`a`.`hashvalue` <> `b`.`hashvalue`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `provider_delete_a`
--

/*!50001 DROP TABLE IF EXISTS `provider_delete_a`*/;
/*!50001 DROP VIEW IF EXISTS `provider_delete_a`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`quantum`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `provider_delete_a` AS select `b`.`provider_id` AS `provider_id`,`b`.`provider_name` AS `provider_name`,`b`.`in_process` AS `in_process`,`b`.`provider_type` AS `provider_type`,`b`.`provider_local_authority` AS `provider_local_authority`,`b`.`provider_region` AS `provider_region`,`b`.`also_known_as` AS `also_known_as`,`b`.`address1` AS `address1`,`b`.`address2` AS `address2`,`b`.`towncity` AS `towncity`,`b`.`county` AS `county`,`b`.`postcode` AS `postcode`,`b`.`latitude` AS `latitude`,`b`.`longitude` AS `longitude`,`b`.`type_info_1` AS `type_info_1`,`b`.`type_info_2` AS `type_info_2`,`b`.`under_review_text` AS `under_review_text`,`b`.`telephone` AS `telephone`,`b`.`email` AS `email`,`b`.`website` AS `website`,`b`.`fax` AS `fax`,`b`.`is_partnership` AS `is_partnership`,`b`.`hashvalue` AS `hashvalue` from `provider_b` `b` where (not(`b`.`provider_id` in (select `a`.`provider_id` from `provider_a` `a`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `provider_delete_b`
--

/*!50001 DROP TABLE IF EXISTS `provider_delete_b`*/;
/*!50001 DROP VIEW IF EXISTS `provider_delete_b`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`quantum`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `provider_delete_b` AS select `a`.`provider_id` AS `provider_id`,`a`.`provider_name` AS `provider_name`,`a`.`in_process` AS `in_process`,`a`.`provider_type` AS `provider_type`,`a`.`provider_local_authority` AS `provider_local_authority`,`a`.`provider_region` AS `provider_region`,`a`.`also_known_as` AS `also_known_as`,`a`.`address1` AS `address1`,`a`.`address2` AS `address2`,`a`.`towncity` AS `towncity`,`a`.`county` AS `county`,`a`.`postcode` AS `postcode`,`a`.`latitude` AS `latitude`,`a`.`longitude` AS `longitude`,`a`.`type_info_1` AS `type_info_1`,`a`.`type_info_2` AS `type_info_2`,`a`.`under_review_text` AS `under_review_text`,`a`.`telephone` AS `telephone`,`a`.`email` AS `email`,`a`.`website` AS `website`,`a`.`fax` AS `fax`,`a`.`is_partnership` AS `is_partnership`,`a`.`hashvalue` AS `hashvalue` from `provider_a` `a` where (not(`a`.`provider_id` in (select `b`.`provider_id` from `provider_b` `b`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `provider_insert_a`
--

/*!50001 DROP TABLE IF EXISTS `provider_insert_a`*/;
/*!50001 DROP VIEW IF EXISTS `provider_insert_a`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`quantum`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `provider_insert_a` AS select `a`.`provider_id` AS `provider_id`,`a`.`provider_name` AS `provider_name`,`a`.`in_process` AS `in_process`,`a`.`provider_type` AS `provider_type`,`a`.`provider_local_authority` AS `provider_local_authority`,`a`.`provider_region` AS `provider_region`,`a`.`also_known_as` AS `also_known_as`,`a`.`address1` AS `address1`,`a`.`address2` AS `address2`,`a`.`towncity` AS `towncity`,`a`.`county` AS `county`,`a`.`postcode` AS `postcode`,`a`.`latitude` AS `latitude`,`a`.`longitude` AS `longitude`,`a`.`type_info_1` AS `type_info_1`,`a`.`type_info_2` AS `type_info_2`,`a`.`under_review_text` AS `under_review_text`,`a`.`telephone` AS `telephone`,`a`.`email` AS `email`,`a`.`website` AS `website`,`a`.`fax` AS `fax`,`a`.`is_partnership` AS `is_partnership`,`a`.`hashvalue` AS `hashvalue` from `provider_a` `a` where (not(`a`.`provider_id` in (select `b`.`provider_id` from `provider_b` `b`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `provider_insert_b`
--

/*!50001 DROP TABLE IF EXISTS `provider_insert_b`*/;
/*!50001 DROP VIEW IF EXISTS `provider_insert_b`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`quantum`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `provider_insert_b` AS select `b`.`provider_id` AS `provider_id`,`b`.`provider_name` AS `provider_name`,`b`.`in_process` AS `in_process`,`b`.`provider_type` AS `provider_type`,`b`.`provider_local_authority` AS `provider_local_authority`,`b`.`provider_region` AS `provider_region`,`b`.`also_known_as` AS `also_known_as`,`b`.`address1` AS `address1`,`b`.`address2` AS `address2`,`b`.`towncity` AS `towncity`,`b`.`county` AS `county`,`b`.`postcode` AS `postcode`,`b`.`latitude` AS `latitude`,`b`.`longitude` AS `longitude`,`b`.`type_info_1` AS `type_info_1`,`b`.`type_info_2` AS `type_info_2`,`b`.`under_review_text` AS `under_review_text`,`b`.`telephone` AS `telephone`,`b`.`email` AS `email`,`b`.`website` AS `website`,`b`.`fax` AS `fax`,`b`.`is_partnership` AS `is_partnership`,`b`.`hashvalue` AS `hashvalue` from `provider_b` `b` where (not(`b`.`provider_id` in (select `a`.`provider_id` from `provider_a` `a`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `provider_update_a`
--

/*!50001 DROP TABLE IF EXISTS `provider_update_a`*/;
/*!50001 DROP VIEW IF EXISTS `provider_update_a`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`quantum`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `provider_update_a` AS select `a`.`provider_id` AS `provider_id`,`a`.`provider_name` AS `provider_name`,`a`.`in_process` AS `in_process`,`a`.`provider_type` AS `provider_type`,`a`.`provider_local_authority` AS `provider_local_authority`,`a`.`provider_region` AS `provider_region`,`a`.`also_known_as` AS `also_known_as`,`a`.`address1` AS `address1`,`a`.`address2` AS `address2`,`a`.`towncity` AS `towncity`,`a`.`county` AS `county`,`a`.`postcode` AS `postcode`,`a`.`latitude` AS `latitude`,`a`.`longitude` AS `longitude`,`a`.`type_info_1` AS `type_info_1`,`a`.`type_info_2` AS `type_info_2`,`a`.`under_review_text` AS `under_review_text`,`a`.`telephone` AS `telephone`,`a`.`email` AS `email`,`a`.`website` AS `website`,`a`.`fax` AS `fax`,`a`.`is_partnership` AS `is_partnership`,`a`.`hashvalue` AS `hashvalue` from (`provider_a` `a` join `provider_b` `b`) where ((`a`.`provider_id` = `b`.`provider_id`) and (`a`.`provider_id` = `b`.`provider_id`) and (`a`.`hashvalue` <> `b`.`!
 hashvalue`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `provider_update_b`
--

/*!50001 DROP TABLE IF EXISTS `provider_update_b`*/;
/*!50001 DROP VIEW IF EXISTS `provider_update_b`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_unicode_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`quantum`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `provider_update_b` AS select `b`.`provider_id` AS `provider_id`,`b`.`provider_name` AS `provider_name`,`b`.`in_process` AS `in_process`,`b`.`provider_type` AS `provider_type`,`b`.`provider_local_authority` AS `provider_local_authority`,`b`.`provider_region` AS `provider_region`,`b`.`also_known_as` AS `also_known_as`,`b`.`address1` AS `address1`,`b`.`address2` AS `address2`,`b`.`towncity` AS `towncity`,`b`.`county` AS `county`,`b`.`postcode` AS `postcode`,`b`.`latitude` AS `latitude`,`b`.`longitude` AS `longitude`,`b`.`type_info_1` AS `type_info_1`,`b`.`type_info_2` AS `type_info_2`,`b`.`under_review_text` AS `under_review_text`,`b`.`telephone` AS `telephone`,`b`.`email` AS `email`,`b`.`website` AS `website`,`b`.`fax` AS `fax`,`b`.`is_partnership` AS `is_partnership`,`b`.`hashvalue` AS `hashvalue` from (`provider_a` `a` join `provider_b` `b`) where ((`a`.`provider_id` = `b`.`provider_id`) and (`a`.`provider_id` = `b`.`provider_id`) and (`a`.`hashvalue` <> `b`.`!
 hashvalue`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2012-05-23 15:27:18

