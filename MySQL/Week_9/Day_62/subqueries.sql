-- 1. Find employees earning more than the average salary.
SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);
-- 2. Find the employee(s) earning the highest salary.
SELECT * FROM employees WHERE salary = (SELECT MAX(salary) FROM employees);
-- 3. Find the employee(s) earning the lowest salary.
SELECT * FROM employees WHERE salary = (SELECT MIN(salary) FROM employees);
-- 4. Find employees whose salary is greater than the salary of employee ID 5.
SELECT * FROM employees WHERE salary > (SELECT salary FROM employees WHERE emp_id = 5);
-- 5. Find employees whose experience is greater than the average experience.
SELECT * FROM employees WHERE exp_yrs > (SELECT AVG(exp_yrs) FROM employees);