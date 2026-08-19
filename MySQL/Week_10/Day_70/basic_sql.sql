-- 1. Find all QA employees earning more than ₹60,000.
SELECT e.* FROM employees e
JOIN departments d
ON e.department_id = d.department_id
WHERE d.department_name = 'QA' AND e.salary = 60000;

-- 2. Find employees from Hyderabad or Bangalore.
SELECT * FROM employees
WHERE city IN ('Hyderabad', 'Bangalore');

-- 3. Find employees whose names start with `A`.
SELECT * FROM employees
WHERE first_name LIKE 'A%';

-- 4. Display the five highest-paid employees.
SELECT * FROM employees
ORDER BY salary DESC
LIMIT 5;

-- 5. Display unique departments.
SELECT DISTINCT department_name 
FROM departments;