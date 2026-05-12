-- Day 01: Employee Management System - Schema & Bulk Operations
-- Focus: DDL (Data Definition), DML (Bulk Inserts), and Basic Aggregates

-- 1. Schema Creation
CREATE TABLE IF NOT EXISTS employees (
    emp_id SERIAL PRIMARY KEY,
    fname VARCHAR(50) NOT NULL,
    lname VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    dept VARCHAR(20),
    salary NUMERIC(10,2),
    hire_date DATE NOT NULL DEFAULT CURRENT_DATE
);

-- 2. Bulk Insert (Industry Standard vs Row-by-Row)
INSERT INTO employees (fname, lname, email, dept, salary, hire_date) VALUES
('Raj', 'Sharma', 'raj.sharma@example.com', 'IT', 50000, '2020-01-15'),
('Priya', 'Singh', 'priya.singh@example.com', 'HR', 45000, '2019-03-22'),
('Arjun', 'Verma', 'arjun.verma@example.com', 'IT', 55000, '2021-06-01'),
('Suman', 'Patel', 'suman.patel@example.com', 'Finance', 60000, '2018-07-30'),
('Kavita', 'Rao', 'kavita.rao@example.com', 'HR', 47000, '2020-11-10'),
('Amit', 'Gupta', 'amit.gupta@example.com', 'Marketing', 52000, '2020-09-25'),
('Neha', 'Desai', 'neha.desai@example.com', 'IT', 48000, '2019-05-18'),
('Rahul', 'Kumar', 'rahul.kumar@example.com', 'IT', 53000, '2021-02-14'),
('Anjali', 'Mehta', 'anjali.mehta@example.com', 'Finance', 61000, '2018-12-03'),
('Vijay', 'Nair', 'vijay.nair@example.com', 'Marketing', 50000, '2020-04-12')
ON CONFLICT (email) DO NOTHING; -- Prevents duplicate errors during re-runs

-- 3. Mastery Drills
-- A) Departmental Salary Analysis
SELECT dept, COUNT(*) as emp_count, SUM(salary) as total_budget
FROM employees
GROUP BY dept;

-- B) Seniority Check (Who has been here longest?)
SELECT fname, lname, hire_date
FROM employees
ORDER BY hire_date ASC
LIMIT 1;

-- C) High-Earner Filtering
SELECT * FROM employees WHERE salary > 55000;
