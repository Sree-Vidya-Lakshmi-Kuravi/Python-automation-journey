SELECT first_name FROM employees WHERE first_name LIKE 'A%';
SELECT first_name FROM employees WHERE first_name LIKE '%n';
SELECT email FROM employees WHERE email LIKE '%example%';
SELECT dept FROM employees WHERE dept LIKE '%IT%';
SELECT city FROM employees WHERE city LIKE 'H%';
-- Employees with exactly five-letter first names
SELECT first_name FROM employees WHERE first_name LIKE '_____';