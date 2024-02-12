-- Script that creates a table unique_id on your MySQL server.
-- Query to create the table 'unique_id'
CREATE TABLE IF NOT EXISTS unique_id (
       id INT UNIQUE DEFAULT 1,
       name VARCHAR(256));
