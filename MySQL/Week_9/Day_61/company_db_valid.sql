-- 1. Verify every employee belongs to the correct department
SELECT e.emp_id, d.dept FROM employees e
INNER JOIN departments d
ON e.dept = d.dept_name;
-- 2. Every department displays the correct manager.
SELECT d.dept_id, d.dept_name, d.manager AS mgr_name FROM departments d;
-- 3. Employees are assigned to the correct project.
SELECT e.emp_id, p.project_id, p.project_name FROM employees e
INNER JOIN projects p
ON e.emp_id = p.emp_id;
-- 4. Verify employees without projects
SELECT 
    e.emp_id,  
    e.dept
FROM employees e
LEFT JOIN projects p ON e.emp_id = p.emp_id
WHERE p.emp_id IS NULL;
-- 5. Verify departments without employees
SELECT 
    d.dept_id, 
    d.dept_name, 
    d.manager
FROM departments d
LEFT JOIN employees e ON d.dept_name = e.dept
WHERE e.emp_id IS NULL;
-- 6. Verify managers with all their employees
SELECT d.manager, e.first_name FROM departments d
LEFT JOIN employees e
ON d.dept_name = e.dept
ORDER BY d.manager;
-- 7. Verify employees working on Project 'Budgeting'
SELECT e.emp_id, e.first_name, p.project_name FROM employees e 
INNER JOIN projects p 
ON e.emp_id = p.emp_id
WHERE p.project_name = 'Budgeting';
-- 8. Verify employees from IT working on Project 'IMS'
SELECT e.emp_id, e.first_name, e.dept, p.project_name FROM employees e 
INNER JOIN projects p
ON e.emp_id = p.emp_id
WHERE e.dept = 'IT' AND p.project_name = 'IMS';
--9. Salary report with department
SELECT d.dept_name,
       COUNT(e.emp_id) AS total_emp,
       SUM(e.salary) AS total_sal,
       AVG(e.salary) AS avg_sal
FROM departments d 
INNER JOIN employees e
ON d.dept_name = e.dept
GROUP BY d.dept_name;
-- 10. Employee Dashboard View
SELECT CONCAT(e.first_name, ' ', e.last_name) AS emp_name,
       e.dept AS department,
       d.manager, p.project_name, e.salary 
FROM employees e
LEFT JOIN departments d ON e.dept = d.dept_name
LEFT JOIN projects p ON e.emp_id = p.emp_id;