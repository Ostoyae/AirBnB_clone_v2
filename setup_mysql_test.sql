-- Setup the hbnb_dev database for testing
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnh_test_pwd';
GRANT ALL PRIVILEGES ON `hbnb_test_db` . * TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema` . * TO 'hbnb_test'@'localhost';
