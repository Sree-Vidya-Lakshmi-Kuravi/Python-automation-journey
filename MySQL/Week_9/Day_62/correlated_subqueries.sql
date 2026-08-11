-- 1. Find employees whose salary is greater than the average salary of their own department.
SELECT e1.emp_id, CONCAT(e1.first_name, " ", e1.last_name), e1.dept AS emp_name FROM employees e1 
WHERE salary > (
    SELECT AVG(e2.salary) FROM employees e2
    WHERE e1.dept = e2.dept);

-- 2. Find employees who have the highest salary within their department.
SELECT e1.emp_id, CONCAT(e1.first_name, " ", e1.last_name) AS emp_name, e1.dept FROM employees e1
WHERE e1.salary = (
    SELECT MAX(e2.salary) FROM employees e2
    WHERE e2.dept = e1.dept);  

-- 3. Find employees whose experience is greater than the average experience of their department.
SELECT e1.emp_id, CONCAT(e1.first_name, " ", e1.last_name) AS emp_name FROM employees e1 WHERE exp_yrs > (
    SELECT AVG(e2.exp_yrs) FROM employees e2
    WHERE e2.dept = e1.dept);

-- 4. Find departments where at least one employee earns more than ₹90,000.
SELECT d.dept_id, d.dept_name
FROM departments d
WHERE EXISTS (
    SELECT 1 FROM employees e
    WHERE e.dept = d.dept_name AND e.salary > 90000);