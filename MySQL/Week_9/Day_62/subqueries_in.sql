-- 1. Find employees working in departments managed by Rohit.
SELECT emp_id, first_name, last_name FROM employees 
WHERE dept 
IN (SELECT dept_name FROM departments WHERE manager = 'Rohit');
-- 2. Find employees working in departments whose name is either IT or Finance.
SELECT emp_id, first_name FROM employees WHERE dept IN (SELECT dept_name FROM departments WHERE dept_name IN ('IT', 'Finance'));
-- 3. Find departments that have employees earning more than ₹80,000.
SELECT dept_id, dept_name, manager FROM departments
WHERE dept_name IN (SELECT DISTINCT dept FROM employees WHERE salary > 80000);
-- 4. Find employees who are working in departments containing more than 3 employees.
SELECT emp_id, first_name, dept FROM employees WHERE dept IN (SELECT dept FROM employees GROUP BY dept HAVING COUNT(emp_id) > 3);
-- 5. Find employees belonging to departments located in selected cities
SELECT emp_id, first_name, last_name, dept, city
FROM employees WHERE dept IN (
    SELECT dept_name FROM departments 
    WHERE city IN ('Hyderabad', 'Bangalore'));