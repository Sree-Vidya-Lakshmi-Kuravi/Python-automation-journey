SELECT * FROM emp;
-- Inserting NULL values in few rows
INSERT INTO emp (eid, fname, lname, dept, joining_date, salary, experience_years, promotion_status, salary_status, experience_level) VALUES (
    11, 'Tom', 'Holland', 'Hollywood', '2018-08-04', 45000, 3, 'Not Eligible', 'Low', 'Junior');
INSERT INTO emp (eid, fname, lname, dept, joining_date, salary, experience_years, promotion_status, salary_status, experience_level) VALUES (
    11, 'Zendeya', 'Holland', 'Hollywood', '2019-12-23', 40000, 3, 'Not Eligible', 'Low', 'Junior');
SELECT * FROM emp;

-- Replace NULL city with Unknown.
SELECT eid, CONCAT(fname, ' ', lname) AS full_name, COALESCE(city, 'Unknown') AS city 
FROM emp;

-- Replace NULL email with Not Provided.
SELECT eid, CONCAT(fname, ' ', lname) AS full_name, COALESCE(email, 'Not Provided') AS email 
FROM emp;

-- Display an employee's phone number if available, otherwise display Not Provided.
ALTER TABLE emp
ADD phone_number VARCHAR(15);
UPDATE emp SET phone_number = '9876543210' WHERE eid = 1;  -- Allu Arjun
UPDATE emp SET phone_number = '9988776655' WHERE eid = 3;  -- Anirudh Ravichander
UPDATE emp SET phone_number = '9012345678' WHERE eid = 4;  -- Keerthy Suresh
UPDATE emp SET phone_number = '9090909090' WHERE eid = 5;  -- Devi Sri Prasad
UPDATE emp SET phone_number = '9123123123' WHERE eid = 6;  -- Mahesh Babu
UPDATE emp SET phone_number = '9345678901' WHERE eid = 7;  -- Samantha
UPDATE emp SET phone_number = '9445566778' WHERE eid = 8;  -- Ilaiyaraaja
UPDATE emp SET phone_number = '9501234567' WHERE eid = 9;  -- Ram Charan
UPDATE emp SET phone_number = '9609876543' WHERE eid = 10; -- A.R. Rahman
SELECT * FROM emp;
SELECT eid, CONCAT(fname, ' ', lname) AS full_name, COALESCE(phone_number, 'Not Provided') AS phone_number 
FROM emp;

-- Create a report where missing department values display as Unassigned.
SELECT eid, fname, lname, COALESCE(dept, 'Unassigned') AS dept, city, joining_date, salary, experience_years,promotion_status, phone_number
FROM emp;

-- Find employees whose missing values have been replaced using COALESCE().
SELECT eid, fname, lname, COALESCE(dept, 'Unassigned') AS department, city, joining_date, salary, experience_years,promotion_status, phone_number
FROM emp
WHERE dept IS NULL;