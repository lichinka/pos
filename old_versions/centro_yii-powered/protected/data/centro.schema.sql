--
-- -------
-- WARNING  All languages must have the same IDs in all tables!
-- -------  For example, English has ID 2 in the 'languages' table and it should 
--			also have ID 2 in the 'item_field_values' table.-
-- 
-- Host: localhost:8889
-- Server version: 5.1.39
-- PHP Version: 5.3.0
-- 
-- Database: `centro_yii`
-- 

--
-- To create an everyday user for this database, use the
-- following commands AFTER the creating the database:
--
-- shell> mysql --user=root mysql -p
-- mysql> CREATE USER 'garufa'@'localhost' IDENTIFIED BY 'clave';
-- mysql> GRANT SELECT,INSERT,UPDATE,DELETE
--    ->     ON centro_yii.*
--    ->     TO 'garufa'@'localhost';
--

CREATE DATABASE IF NOT EXISTS centro_yii CHARACTER SET = utf8 COLLATE = utf8_bin;
USE centro_yii;



-- --------------------------------------------------------
--
-- Table structure for table `company`
--
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS `company` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(255) COLLATE utf8_bin NOT NULL,
  `address` char(255) COLLATE utf8_bin NOT NULL,
  `identification` char(255) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=2 ;

--
-- Dumping data for table `company`
--

INSERT INTO `company` (`id`, `name`, `address`, `identification`) 
VALUES
(1, 'Centro, Inc.', 'Cesta na hrib 123', 'SI666666');


-- --------------------------------------------------------
--
-- Table structure for table `store`
--
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS `store` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(255) COLLATE utf8_bin NOT NULL,
  `address` char(255) COLLATE utf8_bin NOT NULL,
  `telephone` char(255) COLLATE utf8_bin NOT NULL,
  `company_id` int(11) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `company_id` (`company_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='This table represents bussiness units inside a company' AUTO_INCREMENT=2 ;

--
-- Dumping data for table `store`
--
INSERT INTO `store` (`id`, `name`, `address`, `telephone`, `company_id`) 
VALUES
(1, 'Virtual store', 'Virtual street 1911', '040 666 777', 1);


/*
-- --------------------------------------------------------
--
-- Table structure for table `centro_terminals`
--
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS `centro_terminals` (
  `terminal_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(255) COLLATE utf8_bin NOT NULL,
  `store_id` int(11) NOT NULL,
  PRIMARY KEY (`terminal_id`),
  KEY `store_id` (`store_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin COMMENT='A single terminal (i.e. host or cash registry) in a store.' AUTO_INCREMENT=2 ;

--
-- Dumping data for table `centro_terminals`
--

INSERT INTO `centro_terminals` (`terminal_id`, `name`, `store_id`) 
VALUES
(1, '555-444-333-222', 1),
(2, '222-333-444-555', 1);


-- --------------------------------------------------------
--
-- Table structure for table `centro_terminal_configuration`
--
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS `centro_terminal_configuration` (
  `terminal_configuration_id` int(11) NOT NULL AUTO_INCREMENT,
  `key` char(255) COLLATE utf8_bin NOT NULL,
  `value` char(255) COLLATE utf8_bin NOT NULL,
  `terminal_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`terminal_configuration_id`),
  KEY `terminal_id` (`terminal_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=10;

--
-- Dumping data for table `centro_terminal_configuration`
--
INSERT INTO `centro_terminal_configuration` (`terminal_configuration_id`, `key`, `value`, `terminal_id`) 
VALUES
(1, 'address', 'Cesta na hrib 123', 1),
(2, 'company', 'Centro, Inc', 1),
(3, 'default_tax_rate', '8', 1),
(4, 'email', 'info@centro.si', 1),
(5, 'fax', '05 121 112', 1),
(6, 'phone', '031 555 555', 1),
(7, 'return_policy', 'Return policy - testiranje ...', 1),
(8, 'version', '1.0', 1),
(9, 'website', '', 1);


-- --------------------------------------------------------
-- 
-- Table structure for table `centro_languages`
-- 
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS `centro_languages` (
  `language_id` int(11) NOT NULL AUTO_INCREMENT,
  `name` char(20) COLLATE utf8_bin NOT NULL,
  `short_name` char(10) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`language_id`),
  UNIQUE KEY `short_name` (`short_name`),
  KEY `name` (`name`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=3;


-- 
-- Dumping data for table `centro_languages`
-- 
INSERT INTO `centro_languages` (`language_id`, `name`, `short_name`) 
VALUES
(1, 'slovene', 'SI'),
(2, 'english', 'EN');


-- --------------------------------------------------------
-- 
-- Table structure for table `centro_categories`
-- 
-- --------------------------------------------------------
CREATE TABLE `centro_categories` (
  `category_id` int NOT NULL AUTO_INCREMENT,
  `parent_category_id` int NULL,
  PRIMARY KEY (`category_id`),
  KEY `parent_category_id` (`parent_category_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=4;


-- 
-- Dumping data for table `centro_categories`
-- 
INSERT INTO `centro_categories` (`category_id`, `parent_category_id`) VALUES (1, NULL);
INSERT INTO `centro_categories` (`category_id`, `parent_category_id`) VALUES (2, 1);
INSERT INTO `centro_categories` (`category_id`, `parent_category_id`) VALUES (3, 1);


-- --------------------------------------------------------
-- 
-- Table structure for table `centro_categories_lang`
-- 
-- --------------------------------------------------------
CREATE TABLE `centro_categories_lang` (
  `category_lang_id` int NOT NULL AUTO_INCREMENT,
  `category_id` int NOT NULL,
  `language_id` int NOT NULL,
  `name` char(255) NOT NULL,
  `description` char(255) DEFAULT NULL,
  PRIMARY KEY (`category_lang_id`),
  UNIQUE KEY  `category_language` (`category_id`, `language_id`),
  KEY `name` (`name`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=10;

-- 
-- Dumping data for table `centro_categories_lang`
-- 
INSERT INTO `centro_categories_lang` (`category_lang_id`, `category_id`, `language_id`, `name`, `description`) 
VALUES 
(1, 1, 2, 'Shirts', 'High quality shirts. 100% cotton'),
(2, 1, 1, 'Majce', 'Majce prvega razreda. 100% bombaž'),
(3, 2, 2, 'T-shirts', 'Spring oriented t-shirts.'),
(4, 2, 1, 'S kratkimi rokavami', 'Prava izbira za spomlad.'),
(5, 3, 2, 'Long-sleeved shirts', 'Autumm oriented shirts.'),
(6, 3, 1, 'Z dolgimi rokavami', 'Za zimo ali jesen.');


-- --------------------------------------------------------
-- 
-- Table structure for table `centro_item_fields`
-- 
-- --------------------------------------------------------
CREATE TABLE `centro_item_fields` (
  `item_field_id` int NOT NULL AUTO_INCREMENT,
  `name` char(255) NOT NULL,
  `parent_item_field_id` int,
  PRIMARY KEY (`item_field_id`),
  UNIQUE KEY `name` (`name`),
  KEY `parent_item_field_id` (`parent_item_field_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=10;


-- 
-- Dumping data for table `centro_item_fields`
-- 
INSERT INTO `centro_item_fields` (`item_field_id`, `name`, `parent_item_field_id`)
VALUES 
    ( 1, 'language',     NULL),
    ( 2, 'name',         1),
    ( 3, 'description',  1),
    ( 4, 'cost_price',   1),
    ( 5, 'sale_price',   1),
    ( 6, 'size_group',   NULL),
    ( 7, 'size',         6),
    ( 8, 'tax',          1),
    (10, 'tax_percent',  8),
    (11, 'barcode',      NULL);


-- --------------------------------------------------------
-- 
-- Table structure for table `centro_item_values`
-- 
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS `centro_item_values` (
  `item_value_id` int NOT NULL AUTO_INCREMENT,
  `item_field_id` int NOT NULL,
  `value`         char(255) COLLATE utf8_bin,
  `item_id`       int NOT NULL,
  `item_field_value_id` int,
  PRIMARY KEY (`item_value_id`),
  KEY `item_field_id` (`item_field_id`),
  KEY `value`   (`value`),
  KEY `item_id` (`item_id`),
  KEY `item_field_value_id` (`item_field_value_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=13 ;


-- 
-- Dumping data for table `centro_item_values`
--
INSERT INTO `centro_item_values` (`item_value_id`, `item_field_id`, `value`, `item_id`, `item_field_value_id`) 
VALUES
    (1,    1, 'SI',                    1, 1),
    (11,   2, 'Prvi artikel',          1, NULL),
    (12,   3, 'Naš prvi opis artikla', 1, NULL),
    (13,   4, '100',                   1, NULL),
    (14,   5, '1000',                  1, NULL),
    (15,   6, 'XS, S, M, L, XL',       1, 5),
    (16,   7, 'XS',                    1, 11),
    (17,   8, 'D.D.V. 20%',            1, 31),
    (182, 10, '2000',                  1, 33),
    (18,  11, '0001-1',                1, NULL),
    
    (2,    1, 'SI',                    2, 1),
    (21,   2, 'Prvi artikel',          2, NULL),
    (22,   3, 'Naš prvi opis artikla', 2, NULL),
    (23,   4, '100',                   2, NULL),
    (24,   5, '1000',                  2, NULL),
    (25,   6, 'XS, S, M, L, XL',       2, 5),
    (26,   7, 'S',                     2, 12),
    (27,   8, 'D.D.V. 20%',            2, 31),
    (282, 10, '2000',                  2, 33),
    (28,  11, '0001-2',                2, NULL),

    (3,    1, 'SI',                    3, 1),
    (31,   2, 'Prvi artikel',          3, NULL),
    (32,   3, 'Naš prvi opis artikla', 3, NULL),
    (33,   4, '100',                   3, NULL),
    (34,   5, '1000',                  3, NULL),
    (35,   6, 'XS, S, M, L, XL',       3, 5),
    (36,   7, 'M',                     3, 13),
    (37,   8, 'D.D.V. 20%',            3, 31),
    (382, 10, '2000',                  3, 33),
    (38,  11, '0001-3',                3, NULL),

    (4,    1, 'SI',                    4, 1),
    (41,   2, 'Prvi artikel',          4, NULL),
    (42,   3, 'Naš prvi opis artikla', 4, NULL),
    (43,   4, '100',                   4, NULL),
    (44,   5, '1000',                  4, NULL),
    (45,   6, 'XS, S, M, L, XL',       4, 5),
    (46,   7, 'L',                     4, 14),
    (47,   8, 'D.D.V. 20%',            4, 31),
    (482, 10, '2000',                  4, 33),
    (48,  11, '0001-4',                4, NULL),

    (5,    1, 'SI',                    5, 1),
    (51,   2, 'Prvi artikel',          5, NULL),
    (52,   3, 'Naš prvi opis artikla', 5, NULL),
    (53,   4, '100',                   5, NULL),
    (54,   5, '1000',                  5, NULL),
    (55,   6, 'XS, S, M, L, XL',       5, 5),
    (56,   7, 'XL',                    5, 15),
    (57,   8, 'D.D.V. 20%',            5, 31),
    (582, 10, '2000',                  5, 33),
    (58,  11, '0001-5',                5, NULL),

    (10,    1, 'EN',                         10, 2),
    (101,   2, 'First item',                 10, NULL),
    (102,   3, 'Our first item description', 10, NULL),
    (103,   4, '100',                        10, NULL),
    (104,   5, '1000',                       10, NULL),
    (105,   6, 'XS, S, M, L, XL',            10, 5),
    (106,   7, 'XS',                         10, 11),
    (107,   8, 'V.A.T. 17%',                 10, 41),
    (1082, 10, '1700',                       10, 43),
    (108,  11, '0002-1',                     10, NULL),
    
    (20,    1, 'EN',                         20, 2),
    (201,   2, 'First item',                 20, NULL),
    (202,   3, 'Our first item description', 20, NULL),
    (203,   4, '100',                        20, NULL),
    (204,   5, '1000',                       20, NULL),
    (205,   6, 'XS, S, M, L, XL',            20, 5),
    (206,   7, 'S',                          20, 12),
    (207,   8, 'V.A.T. 17%',                 20, 41),
    (2082, 10, '1700',                       20, 43),
    (208,  11, '0002-2',            	     20, NULL),

    (30,    1, 'EN',                         30, 2),
    (301,   2, 'First item',                 30, NULL),
    (302,   3, 'Our first item description', 30, NULL),
    (303,   4, '100',                        30, NULL),
    (304,   5, '1000',                       30, NULL),
    (305,   6, 'XS, S, M, L, XL',            30, 5),
    (306,   7, 'M',                          30, 13),
    (307,   8, 'V.A.T. 17%',                 30, 41),
    (3082, 10, '1700',                       30, 43),
    (308,  11, '0002-3',                     30, NULL),

    (40,    1, 'EN',                         40, 2),
    (401,   2, 'First item',                 40, NULL),
    (402,   3, 'Our first item description', 40, NULL),
    (403,   4, '100',                        40, NULL),
    (404,   5, '1000',                       40, NULL),
    (405,   6, 'XS, S, M, L, XL',            40, 5),
    (406,   7, 'L',                          40, 14),
    (407,   8, 'V.A.T. 17%',                 40, 41),
    (4082, 10, '1700',                       40, 43),
    (408,  11, '0002-4',                     40, NULL);
	

-- --------------------------------------------------------
-- 
-- Table structure for table `centro_item_field_values`
--
-- -------------------------------------------------------- 
CREATE TABLE `centro_item_field_values` (
  `item_field_value_id` int NOT NULL AUTO_INCREMENT,
  `value` CHAR(255) NOT NULL,
  `order` int,
  `item_field_id` int NOT NULL,
  `parent_item_field_value_id` int,
  PRIMARY KEY (`item_field_value_id`),
  KEY `value` (`value`),
  KEY `item_field_id` (`item_field_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=10;

-- 
-- Dumping data for table `centro_item_field_values`
-- 
INSERT INTO `centro_item_field_values` (`item_field_value_id`, `value`, `order`, `item_field_id`, `parent_item_field_value_id`)
VALUES
    --
    -- language
    --
    (1, 'SI', NULL, 1, NULL),
    (2, 'EN', NULL, 1, NULL),
    
    --
    -- size_group
    --
    (5, 'XS, S, M, L, XL',    NULL, 6, NULL),
    (6, '34, 36, 38,..., 52', NULL, 6, NULL),

    --
    -- size
    --
    (11, 'XS', 1, 7, 5),
    (12, 'S',  2, 7, 5),
    (13, 'M',  3, 7, 5),
    (14, 'L',  4, 7, 5),
    (15, 'XL', 5, 7, 5),
    
    (20, '34', 0, 7, 6),
    (21, '36', 1, 7, 6),
    (22, '38', 2, 7, 6),
    (23, '40', 3, 7, 6),
    (24, '42', 4, 7, 6),
    (25, '44', 5, 7, 6),
    (26, '46', 6, 7, 6),
    (27, '48', 7, 7, 6),
    (28, '50', 8, 7, 6),
    (29, '52', 9, 7, 6),

    --
    -- tax
    --
    (31, 'D.D.V. 20%', NULL, 8,  1),
    (33, '2000',       NULL, 10, 31),
    
    (41, 'V.A.T. 17%', NULL, 8,  2),
    (43, '1700',       NULL, 10, 41),
    
    (51, 'D.D.V. 8,5%', NULL, 8,  1),
    (53, '850',         NULL, 10, 51);


-- --------------------------------------------------------
-- 
-- Table structure for table `centro_items`
--
-- -------------------------------------------------------- 
CREATE TABLE `centro_items` (
  `item_id` int NOT NULL AUTO_INCREMENT,
  `category_id` int NOT NULL,
  PRIMARY KEY (`item_id`),
  KEY `category_id` (`category_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=10;

-- 
-- Dumping data for table `centro_items`
-- 
INSERT INTO `centro_items` (`item_id`, `category_id`)
VALUES
	(1, 1),
	(2, 1),
	(3, 1),
	(4, 1),
	(5, 1),
	(10, 1),
	(20, 1),
	(30, 1),
	(40, 1);


-- --------------------------------------------------------
-- 
-- Table structure for table `centro_stocks`
-- 
-- --------------------------------------------------------
CREATE TABLE `centro_stocks` (
  `stock_id` int NOT NULL AUTO_INCREMENT,
  `store_id` int NOT NULL,
  `item_id` int NOT NULL,
  `quantity` int NOT NULL DEFAULT '0' COMMENT 'Expressed in 1/100 units.',
  `reorder_level` int NOT NULL DEFAULT '0' COMMENT 'Expressed in 1/100 units.',
  PRIMARY KEY (`stock_id`),
  KEY `store_id` (`store_id`),
  KEY `item_id`  (`item_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=10;

-- 
-- Dumping data for table `centro_stocks`
-- 
INSERT INTO `centro_stocks` (`stock_id`, `store_id`, `item_id`, `quantity`, `reorder_level`)
VALUES 
(1,  1, 1,  1000, 100),
(10, 1, 10, 1000, 100),
(2,  1, 2,  2000, 200),
(20, 1, 20, 2000, 200),
(3,  1, 3,  3000, 300),
(30, 1, 30, 3000, 300),
(4,  1, 4,  4000, 400),
(40, 1, 40, 4000, 400),
(5,  1, 5,  5000, 500);


-- --------------------------------------------------------
-- 
-- Table structure for table `centro_modules`
-- 
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS `centro_modules` (
  `module_id` int NOT NULL AUTO_INCREMENT,
  `sort` int NOT NULL,
  `path` char(50) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`module_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=8 ;

-- 
-- Dumping data for table `centro_modules`
-- 
INSERT INTO `centro_modules` (`module_id`, `sort`, `path`) 
VALUES
(1, 7, 'company/config_controller'),
(2, 1, 'people/customer_controller'),
(3, 6, 'people/employee_controller'),
(4, 3, 'items/items_controller'),
(5, 4, 'reports_controller'),
(6, 5, 'sales_controller'),
(7, 2, 'items/stock_controller');


-- --------------------------------------------------------
-- 
-- Table structure for table `centro_modules_lang`
-- 
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS `centro_modules_lang` (
  `module_lang_id` int NOT NULL AUTO_INCREMENT,
  `name` CHAR(255) COLLATE utf8_bin NOT NULL,
  `description` CHAR(255) COLLATE utf8_bin NOT NULL,
  `module_id` int NOT NULL,
  `language_id` int NOT NULL,
  PRIMARY KEY (`module_lang_id`),
  KEY `module_id` (`module_id`),
  KEY `language_id` (`language_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=8 ;

-- 
-- Dumping data for table `centro_modules_lang`
-- 
INSERT INTO `centro_modules_lang` (`module_lang_id`, `name`, `description`, `module_id`, `language_id`) 
VALUES
(1, 'Nastavitve sistema',   'Spreminanje nastavitev blagajniškega sistema CenTRO', 1, 1),
(2, 'System configuration', 'Change system settings for the application',          1, 2),
(3, 'Stranke',   'Urejanje šifranta strank',     2, 1),
(4, 'Customers', "Change the customers' database", 2, 2),
(5, 'Osebje',    'Urejanje šifranta osebja',       3, 1),
(6, 'Employees', "Change the employees' database", 3, 2),
(7, 'Artikli', 'Urejanje šifranta artiklov', 4, 1),
(8, 'Items',   'Change the items database',  4, 2),
(9,  'Poročila', 'Pogled in urejanje različnih poročil', 5, 1),
(10, 'Reports',  'View and generate reports',            5, 2),
(11, 'Prodaja', 'Izdaja računov in dobropisov', 6, 1),
(12, 'Sales',   'Process sales and returns',    6, 2),
(13, 'Skladišče', 'Iskanje in urejanje zalogo artiklov', 7, 1),
(14, 'Stock',     'Item stock per warehouse',            7, 2);


-- --------------------------------------------------------
--
-- Table structure for table `centro_terminals_modules_employees`
--
-- --------------------------------------------------------
CREATE TABLE `centro_terminals_modules_employees` (
  `terminal_id` int(11) NOT NULL,
  `module_id`   int(11) NOT NULL,
  `employee_id` int(11) NOT NULL,
  UNIQUE KEY `unique` (`terminal_id`,`module_id`,`employee_id`),
  KEY `centro_terminals_modules_employees_ibfk_3` (`employee_id`),
  KEY `centro_terminals_modules_employees_ibfk_2` (`module_id`),
  KEY `centro_terminals_modules_employees_ibfk_1` (`terminal_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=10;


--
-- Dumping data for table `centro_terminals_modules_employees`
--

INSERT INTO `centro_terminals_modules_employees` (`terminal_id`, `module_id`, `employee_id`) 
VALUES
--
-- Admin modules
--
(1, 1, 1),
(1, 2, 1),
(1, 3, 1),
(1, 4, 1),
(1, 5, 1),
(1, 6, 1),
(1, 7, 1), 
--
-- Alenka modules
--
(1, 6, 2),
--
-- Pepe modules
-- 
(1, 6, 3),
--
-- Ramon modules
--
(1, 1, 5),
(1, 6, 5);


-- --------------------------------------------------------
-- 
-- Table structure for table `centro_customers`
-- 
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS `centro_customers` (
  `customer_id` int NOT NULL AUTO_INCREMENT,
  `name` char(255) COLLATE utf8_bin NOT NULL,
  `phone_number` char(255) COLLATE utf8_bin DEFAULT NULL,
  `email` char(255) COLLATE utf8_bin DEFAULT NULL,
  `address` char(255) COLLATE utf8_bin DEFAULT NULL,
  `city` char(255) COLLATE utf8_bin DEFAULT NULL,
  `state` char(255) COLLATE utf8_bin DEFAULT NULL,
  `zip_code` char(255) COLLATE utf8_bin DEFAULT NULL,
  `country` char(255) COLLATE utf8_bin DEFAULT NULL,
  `tax_payback` boolean DEFAULT TRUE NOT NULL,
  `comments` text COLLATE utf8_bin DEFAULT NULL,
  PRIMARY KEY (`customer_id`),
  KEY `name` (`name`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=10;

--
-- Dumping data for table `centro_customers`
--
INSERT INTO `centro_customers` (`customer_id`, `name`, `phone_number`, `email`, `address`, `city`, `state`, `zip_code`, `country`, `tax_payback`, `comments`)
VALUES
(1, 'Končni kupec', NULL, NULL, NULL, NULL, NULL, NULL, NULL, FALSE, 'Stranka za prodajo pri pultu.-'),
(2, 'Sašo Hribar', '040 879 987', 'saso.hribar@gmail.com', 'Jadranska cesta 87', 'Koper', 'Koper', '4000', 'Slovenija', TRUE, 'Izmišljena oseba.');



--
-- Table structure for table `centro_employees`
--

CREATE TABLE IF NOT EXISTS `centro_employees` (
  `employee_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` char(255) COLLATE utf8_bin NOT NULL,
  `last_name` char(255) COLLATE utf8_bin NOT NULL,
  `phone_number` char(255) COLLATE utf8_bin DEFAULT NULL,
  `email` char(255) COLLATE utf8_bin DEFAULT NULL,
  `address` char(255) COLLATE utf8_bin DEFAULT NULL,
  `city` char(255) COLLATE utf8_bin DEFAULT NULL,
  `state` char(255) COLLATE utf8_bin DEFAULT NULL,
  `zip_code` char(255) COLLATE utf8_bin DEFAULT NULL,
  `country` char(255) COLLATE utf8_bin DEFAULT NULL,
  `comments` text COLLATE utf8_bin DEFAULT NULL,
  `username` char(255) COLLATE utf8_bin NOT NULL,
  `password` char(255) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`employee_id`),
  UNIQUE KEY `username` (`username`),
  KEY `name` (`first_name`,`last_name`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=6 ;

--
-- Dumping data for table `centro_employees`
--

INSERT INTO `centro_employees` (`first_name`, `last_name`, `phone_number`, `email`, `address`, `city`, `state`, `zip_code`, `country`, `comments`, `employee_id`, `username`, `password`) 
VALUES
('John', 'Doe', '05 555 5555', 'admin@centro.si', 'Address', '', '', '', '', '', 1, 'admin', MD5 ('5')),
('Alenka', 'Blagajna', '-', 'alenka@email.si', '-', 'Nova Gorica', 'GO', '4000', 'Slovenija', 'Blagajničarka', 2, 'alenka', MD5 ('444')),
('Pepe', 'Vendesi', '040 222 111', 'pepe@telekom.it', '-', 'Trieste', 'TR', '9000', 'Italia', 'Prodajalec', 3, 'pepe', MD5 ('555')),
('Ramon', 'Diaz', '4585 1288', 'ramon@terra.es', 'La cerrona 221', 'Bilbao', 'BI', '21900', 'España', 'Prodajalec', 5, 'ramon', MD5 ('777'));


-- --------------------------------------------------------
-- 
-- Table structure for table `centro_sales`
-- 
-- --------------------------------------------------------
CREATE TABLE `centro_sales` (
  `sale_id` int NOT NULL AUTO_INCREMENT,
  `sale_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `customer_id` int NOT NULL,
  `employee_id` int NOT NULL,
  `terminal_id` int NOT NULL,
  `invoice_number` int DEFAULT NULL,
  `comment` text NOT NULL,
  PRIMARY KEY (`sale_id`),
  KEY `customer_id`    (`customer_id`),
  KEY `employee_id`    (`employee_id`),
  KEY `invoice_number` (`invoice_number`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=10;

-- 
-- Dumping data for table `centro_sales`
-- 
INSERT INTO `centro_sales` (`sale_id`, `sale_time`, `customer_id`, `employee_id`, `terminal_id`, `invoice_number`, `comment`)
VALUES 
(1, '2010-05-01 13:42:59', 1, 1, 1, NULL, 'Komentar');


-- --------------------------------------------------------
-- 
-- Table structure for table `centro_sale_details`
-- 
-- --------------------------------------------------------
CREATE TABLE `centro_sale_details` (
  `sale_detail_id` int NOT NULL AUTO_INCREMENT,
  `sale_id` int NOT NULL,
  `item_id` int NOT NULL,
  `quantity` int NOT NULL,
  `item_sale_price` int NOT NULL,
  PRIMARY KEY 	(`sale_detail_id`),
  KEY `sale_id` (`sale_id`),
  KEY `item_id` (`item_id`),
  KEY `sale_id_item_id` (`sale_id`,`item_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=10;

-- 
-- Dumping data for table `centro_sale_details`
-- 
INSERT INTO `centro_sale_details` (`sale_detail_id`, `sale_id`, `item_id`, `quantity`, `item_sale_price`)
VALUES 
(1, 1, 1, 500, 2000);


-- --------------------------------------------------------
-- 
-- Table structure for table `centro_sales_details_taxes`
-- 
-- --------------------------------------------------------
CREATE TABLE `centro_sales_details_taxes` (
  `sale_detail_tax_id` int NOT NULL AUTO_INCREMENT,
  `sale_detail_id` int NOT NULL,
  `name` char(255) NOT NULL,
  `percent` int NOT NULL,
  PRIMARY KEY 	(`sale_detail_tax_id`),
  KEY `sale_id` (`sale_detail_id`),
  KEY `name` 	(`name`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=10;

-- 
-- Dumping data for table `centro_sales_details_taxes`
-- 
INSERT INTO `centro_sales_details_taxes` VALUES (1, 1, 'D.D.V. 8,5%', 850);


-- --------------------------------------------------------
-- 
-- Table structure for table `centro_payments`
-- 
-- --------------------------------------------------------
CREATE TABLE `centro_payments` (
  `payment_id` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`payment_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=10;

-- 
-- Dumping data for table `centro_payments`
-- 
INSERT INTO `centro_payments` VALUES (1), (2), (3), (4), (5);


-- --------------------------------------------------------
-- 
-- Table structure for table `centro_payments_lang`
-- 
-- --------------------------------------------------------
CREATE TABLE `centro_payments_lang` (
  `payment_id` int NOT NULL,
  `language_id` int NOT NULL,
  `name` char(255) NOT NULL,
  PRIMARY KEY (`payment_id`, `language_id`),
  KEY (`name`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=10;

-- 
-- Dumping data for table `centro_payments_lang`
-- 
INSERT INTO `centro_payments_lang` 
VALUES (1, 2, 'Cash'),
       (1, 1, 'Gotovina'),
       (2, 2, 'Debit card'),
       (2, 1, 'Plačilna kartica'),
       (3, 2, 'Credit card'),
       (3, 1, 'Kreditna kartica'),
       (4, 2, 'Bond / Certificate'),
       (4, 1, 'Darilni bon'),
       (5, 2, 'Free'),
       (5, 1, 'Zastonj');


-- --------------------------------------------------------
-- 
-- Table structure for table `centro_sale_payments`
-- 
-- --------------------------------------------------------
CREATE TABLE `centro_sale_payments` (
  `sale_payment_id` int NOT NULL AUTO_INCREMENT,
  `payment_id` int NOT NULL,
  `sale_id` int NOT NULL,
  `amount` int NOT NULL,
  PRIMARY KEY (`sale_payment_id`),
  KEY (`payment_id`),
  KEY (`sale_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=10;

-- 
-- Dumping data for table `centro_sale_payments`
-- 

INSERT INTO `centro_sale_payments` (`sale_payment_id`, `payment_id`, `sale_id`, `amount`)
VALUES
(1, 1, 1, 0),
(2, 2, 1, 0),
(3, 3, 1, 10805),
(4, 4, 1, 0),
(5, 5, 1, 0);



-- --------------------------------------------------------
-- 
-- Table structure for table `centro_sessions`
-- 
-- --------------------------------------------------------
CREATE TABLE `centro_sessions` (
  `session_id` char(40) NOT NULL,
  `ip_address` char(16) NOT NULL,
  `user_agent` char(50) NOT NULL,
  `last_activity` int unsigned NOT NULL,
  `user_data` text NOT NULL,
  PRIMARY KEY (`session_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=10;

-- 
-- Dumping data for table `centro_sessions`
-- 




*/

-- --------------------------------------------------------
-- 
-- Constraints for dumped tables
-- 
-- --------------------------------------------------------

--
-- Constraints for table `store`
--
ALTER TABLE `store`
  ADD CONSTRAINT `store_unit_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `company` (`id`);

/*
--
-- Constraints for table `centro_terminal_configuration`
--
ALTER TABLE `centro_terminal_configuration`
  ADD CONSTRAINT `centro_terminal_configuration_ibfk_1` FOREIGN KEY (`terminal_id`) REFERENCES `centro_terminals` (`terminal_id`);

--
-- Constraints for table `centro_terminals`
--
ALTER TABLE `centro_terminals`
  ADD CONSTRAINT `centro_terminals_ibfk_1` FOREIGN KEY (`store_id`) REFERENCES `centro_stores` (`store_id`);

--
-- Constraints for table `centro_modules_lang`
--
ALTER TABLE `centro_modules_lang`
  ADD CONSTRAINT `centro_modules_lang_ibfk_1` FOREIGN KEY (`module_id`) REFERENCES `centro_modules` (`module_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `centro_modules_lang_ibfk_2` FOREIGN KEY (`language_id`) REFERENCES `centro_languages` (`language_id`);

--
-- Constraints for table `centro_terminals_modules_employees`
--
ALTER TABLE `centro_terminals_modules_employees`
  ADD CONSTRAINT `centro_terminals_modules_employees_ibfk_3` FOREIGN KEY (`employee_id`) REFERENCES `centro_employees` (`employee_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `centro_terminals_modules_employees_ibfk_1` FOREIGN KEY (`terminal_id`) REFERENCES `centro_terminals` (`terminal_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `centro_terminals_modules_employees_ibfk_2` FOREIGN KEY (`module_id`) REFERENCES `centro_modules` (`module_id`) ON DELETE CASCADE;

-- 
-- Constraints for table `centro_categories`
-- 
ALTER TABLE `centro_categories`
  ADD CONSTRAINT `centro_categories_ibfk_1` FOREIGN KEY (`parent_category_id`) REFERENCES `centro_categories` (`category_id`);
  
-- 
-- Constraints for table `centro_categories_lang`
-- 
ALTER TABLE `centro_categories_lang`
  ADD CONSTRAINT `centro_categories_lang_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `centro_categories` (`category_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `centro_categories_lang_ibfk_2` FOREIGN KEY (`language_id`) REFERENCES `centro_languages` (`language_id`);

-- 
-- Constraints for table `centro_item_fields`
-- 
ALTER TABLE `centro_item_fields`
  ADD CONSTRAINT `centro_item_fields_ibfk_1` FOREIGN KEY (`parent_item_field_id`) REFERENCES `centro_item_fields` (`item_field_id`);

-- 
-- Constraints for table `centro_item_values`
-- 
ALTER TABLE `centro_item_values`
  ADD CONSTRAINT `centro_item_values_ibfk_1` FOREIGN KEY (`item_field_id`)       REFERENCES `centro_item_fields`       (`item_field_id`),
  ADD CONSTRAINT `centro_item_values_ibfk_2` FOREIGN KEY (`item_id`)             REFERENCES `centro_items`             (`item_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `centro_item_values_ibfk_3` FOREIGN KEY (`item_field_value_id`) REFERENCES `centro_item_field_values` (`item_field_value_id`);

-- 
-- Constraints for table `centro_items`
-- 
ALTER TABLE `centro_items`
  ADD CONSTRAINT `centro_items_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `centro_categories` (`category_id`);

-- 
-- Constraints for table `centro_stocks`
-- 
ALTER TABLE `centro_stocks`
  ADD CONSTRAINT `centro_stocks_ibfk_1` FOREIGN KEY (`item_id`)  REFERENCES `centro_items`  (`item_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `centro_stocks_ibfk_2` FOREIGN KEY (`store_id`) REFERENCES `centro_stores` (`store_id`) ON DELETE CASCADE;

-- 
-- Constraints for table `centro_sales`
-- 
ALTER TABLE `centro_sales`
  ADD CONSTRAINT `centro_sales_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `centro_employees` (`employee_id`),
  ADD CONSTRAINT `centro_sales_ibfk_2` FOREIGN KEY (`customer_id`) REFERENCES `centro_customers` (`customer_id`),
  ADD CONSTRAINT `centro_sales_ibfk_3` FOREIGN KEY (`terminal_id`) REFERENCES `centro_terminals` (`terminal_id`);

-- 
-- Constraints for table `centro_sale_details`
-- 
ALTER TABLE `centro_sale_details`
  ADD CONSTRAINT `centro_sale_details_ibfk_1` FOREIGN KEY (`item_id`) REFERENCES `centro_items` (`item_id`),
  ADD CONSTRAINT `centro_sale_details_ibfk_2` FOREIGN KEY (`sale_id`) REFERENCES `centro_sales` (`sale_id`) ON DELETE CASCADE;

-- 
-- Constraints for table `centro_sales_details_taxes`
-- 
ALTER TABLE `centro_sales_details_taxes`
  ADD CONSTRAINT `centro_sales_details_taxes_ibfk_1` FOREIGN KEY (`sale_detail_id`) REFERENCES `centro_sale_details` (`sale_detail_id`) ON DELETE CASCADE;

-- 
-- Constraints for table `centro_payments_lang`
-- 
ALTER TABLE `centro_payments_lang`
  ADD CONSTRAINT `centro_payments_lang_ibfk_1` FOREIGN KEY (`payment_id`) REFERENCES `centro_payments` (`payment_id`) ON DELETE CASCADE,
  ADD CONSTRAINT `centro_payments_lang_ibfk_2` FOREIGN KEY (`language_id`) REFERENCES `centro_languages` (`language_id`);

-- 
-- Constraints for table `centro_sale_payments`
-- 
ALTER TABLE `centro_sale_payments`
  ADD CONSTRAINT `centro_sale_payments_ibfk_1` FOREIGN KEY (`payment_id`) REFERENCES `centro_payments` (`payment_id`),
  ADD CONSTRAINT `centro_sale_payments_ibfk_2` FOREIGN KEY (`sale_id`)    REFERENCES `centro_sales`    (`sale_id`) ON DELETE CASCADE;

*/
