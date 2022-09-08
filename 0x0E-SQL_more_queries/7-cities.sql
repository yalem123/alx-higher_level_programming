-- Write a script that creates the database hbtn_0d_usa and the table cities
-- cities description
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (id INT UNIQUE AUTO_INCREMENT PRIMARY KEY, state_id INT NOT NULL, CONSTRAINT FOREIGN KEY (state_id) REFERENCES states(id), name VARCHAR(256) NOT NULL);
