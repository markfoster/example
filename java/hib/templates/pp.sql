--
-- Table structure for table `chapter`
--
DROP TABLE IF EXISTS `chapter`;
CREATE TABLE `chapter` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `chapter_id` varchar(30) NOT NULL,
  `chapter_score` int(11) DEFAULT NULL,
  `hashvalue` char(32) DEFAULT NULL,
  `action` char(1) DEFAULT NULL,
  PRIMARY KEY (`provider_id`,`location_id`,`chapter_id`),
  UNIQUE KEY `locid` (`location_id`,`chapter_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`chapter_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Table structure for table `compliance_condition`
--
DROP TABLE IF EXISTS `compliance_condition`;
CREATE TABLE `compliance_condition` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `condition_id` varchar(30) NOT NULL,
  `regulated_activity_id` varchar(30) NOT NULL,
  `compliance_condition` longtext,
  `compliance_reason` longtext,
  `hashvalue` char(32) DEFAULT NULL,
  `action` char(1) DEFAULT NULL,
  PRIMARY KEY (`provider_id`,`location_id`,`condition_id`),
  UNIQUE KEY `locid` (`location_id`,`regulated_activity_id`,`condition_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`condition_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Table structure for table `judgement_method`
--
DROP TABLE IF EXISTS `judgement_method`;
CREATE TABLE `judgement_method` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `outcome_id` varchar(30) NOT NULL,
  `method_id` varchar(30) NOT NULL,
  `method_text` longtext,
  `hashvalue` char(32) DEFAULT NULL,
  `action` char(1) DEFAULT NULL,
  PRIMARY KEY (`provider_id`,`location_id`,`outcome_id`,`method_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`outcome_id`,`method_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Table structure for table `location`
--
DROP TABLE IF EXISTS `location`;
CREATE TABLE `location` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `location_name` longtext,
  `in_process` varchar(1) DEFAULT NULL,
  `location_type` varchar(50) DEFAULT NULL,
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
  `telephone` varchar(20) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `website` varchar(100) DEFAULT NULL,
  `fax` varchar(20) DEFAULT NULL,
  `under_review_text` longtext,
  `location_user_experience` longtext,
  `location_license_information` longtext,
  `location_statement_date` varchar(20) DEFAULT NULL,
  `location_statement_id` varchar(30) DEFAULT NULL,
  `hashvalue` char(32) DEFAULT NULL,
  `action` char(1) DEFAULT NULL,
  PRIMARY KEY (`provider_id`,`location_id`),
  KEY `provider_id` (`provider_id`,`location_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Table structure for table `nominated_individual`
--
DROP TABLE IF EXISTS `nominated_individual`;
CREATE TABLE `nominated_individual` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `regulated_activity_id` varchar(30) NOT NULL,
  `nominated_individual` longtext,
  `hashvalue` char(32) DEFAULT NULL,
  `action` char(1) DEFAULT NULL,
  PRIMARY KEY (`provider_id`,`location_id`,`regulated_activity_id`),
  UNIQUE KEY `locid` (`location_id`,`regulated_activity_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`regulated_activity_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Table structure for table `outcome`
--
DROP TABLE IF EXISTS `outcome`;
CREATE TABLE `outcome` (
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
  `hashvalue` char(32) DEFAULT NULL,
  `action` char(1) DEFAULT NULL,
  PRIMARY KEY (`provider_id`,`location_id`,`outcome_id`),
  UNIQUE KEY `locid` (`location_id`,`outcome_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`outcome_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Table structure for table `partner`
--
DROP TABLE IF EXISTS `partner`;
CREATE TABLE `partner` (
  `provider_id` varchar(30) NOT NULL,
  `partner_id` varchar(30) NOT NULL,
  `partner_name` longtext,
  `hashvalue` char(32) DEFAULT NULL,
  `action` char(1) DEFAULT NULL,
  PRIMARY KEY (`provider_id`,`partner_id`),
  KEY `provider_id` (`provider_id`,`partner_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Table structure for table `provider`
--
DROP TABLE IF EXISTS `provider`;
CREATE TABLE `provider` (
  `provider_id` varchar(30) NOT NULL,
  `provider_name` longtext,
  `in_process` varchar(1) DEFAULT NULL,
  `provider_type` varchar(50) DEFAULT NULL,
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
  `hashvalue` char(32) DEFAULT NULL,
  `action` char(1) DEFAULT NULL,
  PRIMARY KEY (`provider_id`),
  KEY `provider_id` (`provider_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Table structure for table `registered_manager`
--
DROP TABLE IF EXISTS `registered_manager`;
CREATE TABLE `registered_manager` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `regulated_activity_id` varchar(30) NOT NULL,
  `manager_name` longtext,
  `manager_condition` longtext,
  `hashvalue` char(32) DEFAULT NULL,
  `action` char(1) DEFAULT NULL,
  PRIMARY KEY (`provider_id`,`location_id`,`regulated_activity_id`),
  UNIQUE KEY `location_id` (`location_id`,`regulated_activity_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`regulated_activity_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Table structure for table `regulated_activity`
--
DROP TABLE IF EXISTS `regulated_activity`;
CREATE TABLE `regulated_activity` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `regulated_activity_id` varchar(30) NOT NULL,
  `hashvalue` char(32) DEFAULT NULL,
  `action` char(1) DEFAULT NULL,
  PRIMARY KEY (`provider_id`,`location_id`,`regulated_activity_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`regulated_activity_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Table structure for table `routine_condition`
--
DROP TABLE IF EXISTS `routine_condition`;
CREATE TABLE `routine_condition` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `condition_id` varchar(30) NOT NULL,
  `regulated_activity_id` varchar(30) NOT NULL,
  `routine_condition` longtext,
  `hashvalue` char(32) DEFAULT NULL,
  `action` char(1) DEFAULT NULL,
  PRIMARY KEY (`provider_id`,`location_id`,`condition_id`),
  UNIQUE KEY `location_id` (`location_id`,`condition_id`,`regulated_activity_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`condition_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Table structure for table `service_type`
--
DROP TABLE IF EXISTS `service_type`;
CREATE TABLE `service_type` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `service_type_id` varchar(30) NOT NULL,
  `hashvalue` char(32) DEFAULT NULL,
  PRIMARY KEY (`provider_id`,`location_id`,`service_type_id`),
  UNIQUE KEY `location_id` (`service_type_id`,`location_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`service_type_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

--
-- Table structure for table `service_user_band`
--
DROP TABLE IF EXISTS `service_user_band`;
CREATE TABLE `service_user_band` (
  `provider_id` varchar(30) NOT NULL,
  `location_id` varchar(30) NOT NULL,
  `service_user_band_id` varchar(30) NOT NULL,
  `hashvalue` char(32) DEFAULT NULL,
  PRIMARY KEY (`provider_id`,`location_id`,`service_user_band_id`),
  UNIQUE KEY `location_id` (`location_id`,`service_user_band_id`),
  KEY `provider_id` (`provider_id`,`location_id`,`service_user_band_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;
