-- Name validation
-- Write SQL that produces the employee's full name from: first_name and last_name
SELECT CONCAT(fname, ' ', lname) AS full_name FROM emp;

-- Email Validation
-- Write SQL to retrieve the employee email and normalize it using LOWER() before comparison.
SELECT LOWER(email) AS email FROM emp;

-- Missing Data
-- Write SQL using COALESCE() to produce the same value when the database contains NULL for city.
SELECT COALESCE(city, 'Unknown') FROM emp;

-- Salary Classification
-- Use CASE to verify the database classification of salary.
SELECT eid,
    CASE 
        WHEN salary > 20000 THEN 'High' 
        WHEN salary BETWEEN 10000 AND 19999 THEN 'Medium' 
        ELSE 'Low'
    END AS salary_class
FROM emp;

-- Experience Classification
-- Use CASE to validate it.
SELECT eid,
    CASE    
        WHEN experience_years >= 5 THEN 'Senior'
        WHEN experience_years = 3 OR experience_years = 4 THEN 'Mid-Level'
        WHEN experience_years < 3 THEN 'Junior'
    END AS exp_level
FROM emp;

-- Joining Date
-- Use YEAR() to validate the database value.
SELECT YEAR(joining_date) AS joined_year
FROM emp;

-- Employee Tenure
-- Use date calculations to derive the value.
SELECT TIMESTAMPDIFF(YEAR, joining_date, CURDATE()) AS tenure_years FROM emp;

-- Dashboard Validation
SELECT 
    CONCAT(fname, ' ', lname) AS employee_name,
    COALESCE(dept, 'Unassigned') AS department,
    salary,
    CASE 
        WHEN salary >= 2000000 THEN 'High'
        WHEN salary BETWEEN 1000000 AND 1999999 THEN 'Medium'
        ELSE 'Low'
    END AS salary_category,
    experience_years AS experience,
    CASE 
        WHEN experience_years >= 15 THEN 'Senior'
        WHEN experience_years BETWEEN 5 AND 14 THEN 'Mid-level'
        ELSE 'Junior'
    END AS experience_level,
    YEAR(joining_date) AS joining_year
FROM emp;
