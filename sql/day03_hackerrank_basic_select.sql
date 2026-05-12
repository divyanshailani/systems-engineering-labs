-- Problem: Weather Observation Station 5
-- Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths.
-- If there is more than one smallest or largest city, choose the one that comes first when ordered alphabetically.

-- Smallest city name
SELECT city, LENGTH(city) 
FROM station 
ORDER BY LENGTH(city) ASC, city ASC 
LIMIT 1;

-- Largest city name
SELECT city, LENGTH(city) 
FROM station 
ORDER BY LENGTH(city) DESC, city ASC 
LIMIT 1;
