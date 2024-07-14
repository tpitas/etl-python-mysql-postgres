# Creating a target database and table to load

DROP DATABASE IF EXISTS dbstocks;
CREATE DATABASE dbstocks;
USE dbstocks;
 
CREATE TABLE stocks(
    date DATE NOT NULL, 
    open DECIMAL(13,4) NOT NULL,
    high DECIMAL(13,4) NOT NULL,
    low DECIMAL(13,4) NOT NULL,
    close DECIMAL(13,4) NOT NULL,
    volume INT(10) NOT NULL
);
 
SHOW TABLES;