-- 1. Employee + Department + Project
SELECT 
    e.first_name, 
    e.last_name, 
    e.dept AS department_name, 
    p.project_name
FROM employees e
INNER JOIN departments d ON e.dept = d.dept_name
INNER JOIN projects p ON e.emp_id = p.emp_id;
-- 2. Employee + Manager + Project
SELECT 
    e.first_name, 
    e.last_name, 
    d.manager AS manager_name, 
    p.project_name
FROM employees e
INNER JOIN departments d ON e.dept = d.dept_name
INNER JOIN projects p ON e.emp_id = p.emp_id;
-- 3. Department + Manager + Employee Count
SELECT d.dept_name,
       d.manager AS manager_name,
       COUNT(e.emp_id) AS emp_count
FROM departments d
LEFT JOIN employees e ON d.dept_name = e.dept
GROUP BY d.dept_name, d.manager;
-- 4. Employee + Salary + Project
SELECT 
    e.first_name, 
    e.last_name, 
    e.salary, 
    p.project_name
FROM employees e
INNER JOIN projects p ON e.emp_id = p.emp_id;
-- 5. IT employees working on Project 'IMS'
SELECT 
    e.first_name, 
    e.last_name, 
    e.dept, 
    p.project_name
FROM employees e
INNER JOIN projects p ON e.emp_id = p.emp_id
WHERE e.dept = 'IT' 
  AND p.project_name = 'IMS';
-- 6. Employees from Hyderabad working on Project 'Budgeting'
SELECT 
    e.first_name, 
    e.last_name, 
    e.city, 
    p.project_name
FROM employees e
INNER JOIN projects p ON e.emp_id = p.emp_id
WHERE e.city = 'Hyderabad' 
  AND p.project_name = 'Budgeting';
-- 7. Managers with all their employees.
SELECT 
    d.manager AS manager_name, 
    d.dept_name, 
    e.first_name AS employee_first_name, 
    e.last_name AS employee_last_name
FROM departments d
LEFT JOIN employees e ON d.dept_name = e.dept
ORDER BY d.manager; 