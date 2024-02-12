-- Script that lists all the cities of California registered in the database
SELECT id, name -- Query that lists all the cities from California
FROM cities
WHERE state_id = ( -- Query to get the state_id of California
      SELECT id
      FROM states
      WHERE name = "California");
