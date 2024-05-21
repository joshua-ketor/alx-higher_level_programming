-- list all records of the table secon_table

SELECT score, name
FROM second_table
WHERE name != ''
ORDER BY score DESC;
