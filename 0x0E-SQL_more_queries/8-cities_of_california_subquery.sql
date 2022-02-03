-- lists all the cities of California
SELECT id, name
FROM cities
WHERE state_id = (
SELECT state_id
FROM states
WHERE name = 'California'
ORDER BY id ASC
);
