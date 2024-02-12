-- Script that lists all records of a table second_table of database hbtn_0c_0
-- Query to lists all records of the table
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
