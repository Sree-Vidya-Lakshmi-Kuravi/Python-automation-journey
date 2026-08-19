-- 6. Find the total number of employees.
SELECT COUNT(*) AS emp_count FROM employees;

-- 7. Find the average salary per department.
SELECT d.department_name, ROUND(AVG(e.salary), 2) AS avg_salary
FROM departments d
JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_id, d.department_name;

-- 8. Find departments containing more than 3 employees.
SELECT d.department_name, COUNT(e.employee_id) AS employee_count FROM departments d
JOIN employees e
ON d.department_id = e.department_id
GROUP BY d.department_name 
HAVING COUNT(e.employee_id) > 3;

-- 9. Find the highest salary in each department.
SELECT d.department_name, MAX(e.salary) AS emp_salary FROM departments d
JOIN employees e
ON d.department_id = e.department_id
GROUP BY d.department_name;

-- 10. Find cities having more than 2 employees.
SELECT city, COUNT(*) AS employee_count
FROM employees
WHERE city IS NOT NULL
GROUP BY city
HAVING COUNT(*) > 2;