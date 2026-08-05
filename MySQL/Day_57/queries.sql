
-- SELECT QUERIES
SELECT * FROM employees;
SELECT first_name, dept FROM employees;
SELECT emp_id, first_name, designation, salary FROM employees;
SELECT * FROM employees where dept = 'Finance';
SELECT * FROM employees WHERE salary > 60000;
SELECT * FROM employees WHERE exp_yrs > 3;
SELECT * FROM employees WHERE city = 'Hyderabad';
SELECT * FROM employees WHERE designation = 'Software Engineer';
SELECT email FROM employees; 
SELECT first_name, last_name, joining_date FROM employees;

-- WHERE + Comparison Operators
SELECT * FROM employees WHERE salary < 50000;
SELECT * FROM employees WHERE exp_yrs = 5;
SELECT * FROM employees WHERE city = 'Banglore';
SELECT * FROM employees WHERE joining_date > '2023-01-01';
SELECT * FROM employees WHERE joining_date < '2022-01-01';
SELECT * FROM employees WHERE dept = 'Development';
SELECT * FROM employees WHERE salary >= 80000;
SELECT * FROM employees WHERE exp_yrs <= 2;
SELECT * FROM employees WHERE designation = 'Recruiter';
SELECT * FROM employees WHERE emp_id = 10;

-- AND, OR, NOT
SELECT * FROM employees WHERE dept = 'IT' AND city = 'Hyderabad';
SELECT * FROM employees WHERE dept = 'HR' AND salary = 70000;
SELECT * FROM employees WHERE dept = 'HR' OR dept = 'Finance'; 
SELECT * FROM employees WHERE city = 'Hyderabad' OR dept = 'Bangalore';
SELECT * FROM employees WHERE salary > 60000 AND exp_yrs > 4;
SELECT * FROM employees WHERE dept = 'Marketing' AND designation = 'Content Writer';
SELECT * FROM employees WHERE NOT dept = 'Marketing';
SELECT * FROM employees WHERE NOT city = 'Hyderabad';
SELECT * FROM employees WHERE salary < 50000 AND exp_yrs < 2;
SELECT * FROM employees WHERE joining_date = '2022-02-01' AND city = 'Banglore';
SELECT * FROM employees WHERE NOT designation = 'Support Engineer';
SELECT * FROM employees WHERE dept = 'Support' OR dept = 'IT';
SELECT * FROM employees WHERE salary > 90000 OR exp_yrs > 8;
SELECT * FROM employees WHERE city = 'Chennai' AND dept = 'HR';
SELECT * FROM employees WHERE NOT city = 'Bangalore' AND salary > 65000;

-- Practice Problems
SELECT * FROM employees WHERE designation = 'Support Engineer' AND year(joining_date) = '2023';
SELECT * FROM employees WHERE exp_yrs > 5;
-- Find employees whose email belongs to the company domain.
SELECT * FROM employees WHERE email LIKE '%@example.com';
SELECT * FROM employees WHERE dept = 'IT';
--Find employees with duplicate first names.
SELECT first_name, COUNT(*) AS name_count
FROM employees GROUP BY first_name HAVING COUNT(*) > 1 ORDER BY name_count DESC;
SELECT * FROM employees WHERE salary BETWEEN 50000 AND 80000;
SELECT * FROM employees WHERE year(joining_date) BETWEEN 2023 AND 2024;
SELECT * FROM employees WHERE city = 'Hyderabad' AND salary > 75000;
SELECT * FROM employees WHERE designation = 'Support Engineer' OR designation = 'Frontend Developer';
SELECT * FROM employees WHERE exp_yrs BETWEEN 2 AND 5;
SELECT * FROM employees WHERE salary = 65000;
SELECT * FROM employees WHERE NOT dept = 'HR';
SELECT * FROM employees WHERE joining_date = '2021-11-27';

-- BONUS CHALLENGES
SELECT * FROM employees WHERE CONCAT(first_name, " ", last_name) = 'Peter Parker';
SELECT email, COUNT(*) FROM employees GROUP BY email HAVING COUNT(*) > 1;
SELECT * FROM employees WHERE dept IS NOT NULL;
SELECT * FROM employees WHERE salary > 0;
SELECT * FROM employees WHERE dept = 'IT' AND salary > 40000;
SELECT COUNT(*) AS total_emp FROM employees; 
SELECT * FROM employees WHERE YEAR(joining_date) > 2020;
SELECT * FROM employees WHERE designation LIKE '%Manager' AND exp_yrs > 5;
SELECT * FROM employees WHERE email IS NULL;
SELECT emp_id, dept FROM employees WHERE emp_id = 15;