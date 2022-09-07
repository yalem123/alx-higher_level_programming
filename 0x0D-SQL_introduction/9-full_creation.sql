-- prints script that creates a table second_table in the database.
-- query for creating a table second_table in the database hbtn_0c_0.
CREATE TABLE IF NOT EXISTS second_table(id INT, name VARCHAR(256), score INT);
INSERT INTO second_table (id, name, score) VALUES (1, "John", 10);
INSERT INTO second_table (id, name, score) VALUES (2, "alex", 3);
INSERT INTO second_table (id, name, score) VALUES (3, "Bob", 4);
INSERT INTO second_table (id, name, score) VALUES (4, "Goerge", 8);
