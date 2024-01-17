-- creates the database hbtn_0d_usa and the table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use database
USE hbtn_0d_usa;
-- create table states
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY(id));
