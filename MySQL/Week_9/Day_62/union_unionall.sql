-- 1. Get the names of employees from IT and Finance in one result.
SELECT CONCAT(e.first_name, " ", e.last_name) AS emp_name FROM employees e WHERE e.dept = 'IT'
UNION
SELECT CONCAT(e.first_name, " ", e.last_name) AS emp_name FROM employees e WHERE e.dept = 'Finance';

-- 2. Get employee cities from two different queries using `UNION`.
SELECT e.city FROM employees e WHERE e.dept = 'IT'
UNION
SELECT e.city FROM employees e WHERE e.dept = 'Finance';

-- 3. Combine employees from Hyderabad and Bangalore using `UNION`.
SELECT e.emp_id, CONCAT(e.first_name, " ", e.last_name) FROM employees e WHERE e.city = 'Hyderabad'
UNION
SELECT e.emp_id, CONCAT(e.first_name, " ", e.last_name) FROM employees e WHERE e.city = 'Bangalore';

-- 4. Repeat the previous query using `UNION ALL`.
SELECT e.emp_id, CONCAT(e.first_name, " ", e.last_name) FROM employees e WHERE e.city = 'Hyderabad'
UNION ALL
SELECT e.emp_id, CONCAT(e.first_name, " ", e.last_name) FROM employees e WHERE e.city = 'Bangalore';