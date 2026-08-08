-- 1. Show all departments even if no employee belongs to them.
SELECT d.dept_id, d.dept_name, e.first_name, e.last_name
FROM employees e
RIGHT JOIN departments d 
  ON e.dept = d.dept_name;
-- 2. Display all projects even if an employee is missing.
SELECT p.project_id, p.project_name, e.emp_id, e.first_name, e.last_name
FROM employees e
RIGHT JOIN projects p 
  ON e.emp_id = p.emp_id;
-- 3. Display all managers.
SELECT DISTINCT d.manager, d.dept_name
FROM employees e
RIGHT JOIN departments d 
  ON e.dept = d.dept_name;