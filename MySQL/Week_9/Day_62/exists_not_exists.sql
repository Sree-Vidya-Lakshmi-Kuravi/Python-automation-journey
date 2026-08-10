-- 1. Find departments that have at least one employee.
SELECT dept_name FROM departments WHERE EXISTS (SELECT 1 FROM employees);
SELECT d.dept_id, d.dept_name, d.manager FROM departments d
WHERE EXISTS (SELECT 1 FROM employees e 
    WHERE e.dept = d.dept_name);
-- 2. Find departments that have no employees.
SELECT d.dept_id, d.dept_name FROM departments d 
WHERE NOT EXISTS (SELECT 1 FROM employees e WHERE e.dept = d.dept_name);
-- 3. Find employees who have at least one project assignment.
SELECT e.emp_id, e.first_name FROM employees e WHERE EXISTS (SELECT 1 FROM projects p WHERE p.emp_id = e.emp_id);
-- 4. Find employees who have no project assignment.
SELECT e.emp_id, e.first_name FROM employees e WHERE NOT EXISTS (SELECT 1 FROM projects p WHERE p.emp_id = e.emp_id);
-- 5. Find projects that have at least one employee assigned.
SELECT p.project_id, p.project_name FROM projects p WHERE EXISTS (SELECT 1 FROM employees e WHERE p.emp_id = e.emp_id);
