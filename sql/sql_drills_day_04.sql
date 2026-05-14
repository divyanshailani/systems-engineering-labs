-- DAY 04: SQL CORE THREAD DRILLS
-- Focus: Aggregations, Subqueries, and String Function Mastering
-- Dialect: PostgreSQL

-----------------------------------------------------------
-- 1. AGGREGATIONS: TOP EARNERS LOGIC
-----------------------------------------------------------
-- Find the maximum salary and count how many employees earn it.
SELECT MAX(salary) AS max_salary, COUNT(*) AS employee_count
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);

-- Alternative approach using ORDER BY and LIMIT
SELECT salary, COUNT(*) 
FROM employees 
GROUP BY salary 
ORDER BY salary DESC 
LIMIT 1;

-----------------------------------------------------------
-- 2. STRING FUNCTIONS: DATA CLEANING & REFINING
-----------------------------------------------------------

-- FORMAT EMAILS: Uppercase transformation
SELECT fname, UPPER(email) as upper_email FROM employees;

-- DOMAIN EXTRACTION: Using POSITION + SUBSTRING (Surgical extraction)
-- Extracts everything after the '@' symbol dynamically
SELECT 
    fname, 
    SUBSTRING(email FROM POSITION('@' IN email) + 1) AS domain 
FROM employees;

-- FORMAL NAMES: Concat with initials
-- Pattern: "R. Sharma"
SELECT LEFT(fname, 1) || '. ' || lname AS formal_name FROM employees;

-- INITCAP: Standardizing casing for departments
SELECT INITCAP(dept) AS formatted_dept FROM employees;

-----------------------------------------------------------
-- 3. DIALECT MASTERY: POSTGRES REGEX
-----------------------------------------------------------
-- Case-insensitive match for names starting with 'A'
SELECT * FROM employees WHERE fname ~* '^a';

-----------------------------------------------------------
-- NEXT STEPS (DAY 05)
-----------------------------------------------------------
-- 1. Joins (Population Census level)
-- 2. Window Functions (MPrashant 04:13:39)
-- 3. NumPy Deep Dive (Keith Galli)
