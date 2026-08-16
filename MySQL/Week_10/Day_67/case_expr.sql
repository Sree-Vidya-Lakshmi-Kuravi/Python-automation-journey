ALTER TABLE emp
ADD salary INT;
ALTER TABLE emp
ADD experience_years INT;

UPDATE emp SET salary = 15000, experience_years = 3 WHERE eid = 1;  -- Allu Arjun
UPDATE emp SET salary = 20000, experience_years = 5 WHERE eid = 2;  -- Nayanthara
UPDATE emp SET salary = 100000, experience_years = 4 WHERE eid = 3;  -- Anirudh Ravichander
UPDATE emp SET salary = 90000,  experience_years = 2  WHERE eid = 4;  -- Keerthy Suresh
UPDATE emp SET salary = 60000, experience_years = 4 WHERE eid = 4;  -- Devi Sri Prasad
UPDATE emp SET salary = 20000, experience_years = 6 WHERE eid = 6;  -- Mahesh Babu
UPDATE emp SET salary = 10000, experience_years = 3 WHERE eid = 7;  -- Samantha
UPDATE emp SET salary = 70000, experience_years = 10 WHERE eid = 8;  -- Ilaiyaraaja
UPDATE emp SET salary = 30000, experience_years = 2 WHERE eid = 9;  -- Ram Charan
UPDATE emp SET salary = 60000, experience_years = 8 WHERE eid = 10; -- A.R. Rahman
SELECT * FROM emp;

-- Categorize employees based on salary:
    -- >= 80000 → High
    -- 50000–79999 → Medium
    -- < 50000 → Low
SELECT *, 
       CASE 
        WHEN salary >= 80000 THEN 'High'
        WHEN salary >= 50000 THEN 'Medium'
        ELSE 'Low'
       END AS salary_category
FROM emp;

-- Categorize employees based on experience:
    -- >= 5 → Senior
    -- 3–4 → Mid-Level
    -- < 3 → Junior
SELECT eid, CONCAT(fname, ' ', lname) AS full_name,
       CASE 
        WHEN experience_years >= 5 THEN 'Senior'
        WHEN experience_years = 3 OR experience_years = 4 THEN 'Mid-Level'
        WHEN experience_years < 3 THEN 'Junior'
       END AS experience_level
FROM emp;

-- Mark employees as:
    -- Hyderabad → Local
    -- Other cities → Non-Local
SELECT eid, fname,
       CASE 
        WHEN city = 'Hyderabad' THEN 'Local'
        ELSE 'Non-Local'
       END AS city_status
FROM emp;

-- Categorize employees based on department
SELECT eid, fname, dept,
       CASE
        WHEN dept = 'Music' THEN 'Sangeetham'
        ELSE 'Natana'
       END AS dept_category
FROM emp;

-- Create an experience_level column using CASE.
SELECT eid, CONCAT(fname, ' ', lname) AS full_name,
       CASE 
        WHEN experience_years >= 5 THEN 'Senior'
        WHEN experience_years = 3 OR experience_years = 4 THEN 'Mid-Level'
        WHEN experience_years < 3 THEN 'Junior'
       END AS experience_level
FROM emp;

-- Create a salary_status column:
    -- salary >= 70000 → Eligible
    -- otherwise → Not Eligible
SELECT eid, salary,
       CASE
        WHEN salary >= 70000 THEN 'Eligible'
        ELSE 'Not Eligible'
       END AS salary_status
FROM emp;

-- Identify employees who joined before 2013 as Experienced.
SELECT eid, fname, joining_date,
       CASE
        WHEN YEAR(joining_date) < 2013 THEN 'Experienced'
       END AS exp
FROM emp;

-- Identify employees who joined in/after 2014 as Recent.
SELECT eid, fname, joining_date,
       CASE
        WHEN YEAR(joining_date) >= 2014 THEN 'Recent'
       END AS exp
FROM emp;

-- Create a promotion_status based on salary and experience.
ALTER TABLE emp
ADD promotion_status VARCHAR(20);
UPDATE emp
SET promotion_status = 
    CASE 
        WHEN salary >= 50000 OR experience_years >= 5 THEN 'Eligible'
        ELSE 'Not Eligible'
    END;
SELECT * FROM emp;

ALTER TABLE emp
ADD salary_status VARCHAR(20);
UPDATE emp
SET salary_status =
       CASE 
        WHEN salary >= 80000 THEN 'High'
        WHEN salary >= 50000 THEN 'Medium'
        ELSE 'Low'
       END;

ALTER TABLE emp
ADD experience_level VARCHAR(20);
UPDATE emp
SET experience_level =   
        CASE    
        WHEN experience_years >= 5 THEN 'Senior'
        WHEN experience_years = 3 OR experience_years = 4 THEN 'Mid-Level'
        WHEN experience_years < 3 THEN 'Junior'
       END;

-- 4. Create a combined employee report containing:
    -- - Name
    -- - Department
    -- - Salary
    -- - Experience
    -- - Salary category
    -- - Experience level
SELECT CONCAT('Name: ', fname, ' | Department: ', dept, ' | Salary: ', salary, ' | Experience: ', experience_years, ' | Salary Category: ', salary_status, ' | Experience Level: ', experience_level) AS emp_report
FROM emp;