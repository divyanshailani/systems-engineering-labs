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

---------------------------------------------------------

-- Problem: Weather Observation Station 6
-- Query the list of CITY names starting with vowels (i.e., a, e, i, o, or u) from STATION. 
-- Your result cannot contain duplicates.

-- Approach 1: Using REGEXP (Concise)
-- SELECT DISTINCT city FROM station WHERE city REGEXP '^[aeiou]';

-- Approach 2: Using LEFT and IN (User Implemented)
SELECT DISTINCT city 
FROM station 
WHERE LEFT(city, 1) IN ('a', 'e', 'i', 'o', 'u');
