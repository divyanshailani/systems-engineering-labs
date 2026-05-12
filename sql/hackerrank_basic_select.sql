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

---------------------------------------------------------

-- Problem: Weather Observation Station 11
-- Query the list of CITY names from STATION that either do not start with vowels or do not end with vowels. 
-- Your result cannot contain duplicates.

SELECT DISTINCT city 
FROM station 
WHERE LEFT(city, 1) NOT IN ('a', 'e', 'i', 'o', 'u')
   OR RIGHT(city, 1) NOT IN ('a', 'e', 'i', 'o', 'u');

---------------------------------------------------------

-- Problem: Weather Observation Station 12
-- Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. 
-- Your result cannot contain duplicates.

SELECT DISTINCT city 
FROM station 
WHERE LEFT(city, 1) NOT IN ('a', 'e', 'i', 'o', 'u')
   AND RIGHT(city, 1) NOT IN ('a', 'e', 'i', 'o', 'u');

---------------------------------------------------------

-- Problem: Higher Than 75 Marks
-- Query the Name of any student in STUDENTS who scored higher than 75 Marks. 
-- Order by the last three characters of each name, secondary sort by ascending ID.

SELECT Name 
FROM STUDENTS 
WHERE Marks > 75 
ORDER BY RIGHT(Name, 3) ASC, ID ASC;

---------------------------------------------------------

-- Problem: Employee Salaries
-- Query a list of employee names for employees in Employee having a salary greater than $2000 per month 
-- who have been employees for less than 10 months. Sort by ascending employee_id.

SELECT name 
FROM Employee 
WHERE salary > 2000 
  AND months < 10 
ORDER BY employee_id ASC;
