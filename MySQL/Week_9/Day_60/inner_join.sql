-- 1. Display employee name with department name.
SELECT first_name, last_name, dept FROM employees
INNER JOIN departments
ON employees.dept = departments.dept_name;
-- 2. Display employee name with manager name.
SELECT first_name, last_name, manager FROM employees
INNER JOIN departments
ON employees.dept = departments.dept_name;
-- 3. Display employee salary with department.
SELECT first_name, last_name, salary FROM employees
INNER JOIN departments
ON employees.dept = departments.dept_name;
-- 4. Display project name with employee name.
SELECT project_name, first_name, last_name FROM employees INNER JOIN projects ON employees.emp_id = projects.emp_id;
-- 5. Display employees working in the IT department.
SELECT e.emp_id, d.dept_name FROM employees e 
INNER JOIN departments d 
ON e.dept = d.dept_name 
WHERE e.dept = 'IT';
-- 6. Display employees with their department and project.
SELECT e.first_name, e.last_name, d.dept_name, p.project_name FROM employees e
INNER JOIN departments d ON e.dept = d.dept_name
INNER JOIN projects p ON e.emp_id = p.emp_id;
-- 7. Display employees whose manager is Rohit.
SELECT e.first_name, e.last_name, d.manager FROM employees e INNER JOIN departments d 
ON e.dept = d.dept_name 
WHERE d.manager = 'Rohit';
-- 8. Display employee city with department.
SELECT e.first_name, e.last_name, e.city, d.dept_name FROM employees e
INNER JOIN departments d 
ON e.dept = d.dept_name; 
-- 9. Display employee experience with project.
SELECT e.first_name, e.last_name, e.exp_yrs, p.project_name FROM employees e
INNER JOIN projects p 
ON e.emp_id = p.emp_id;
-- 10. Display all employee details with department details.
SELECT e.*, d.* FROM employees e INNER JOIN departments d
ON e.dept = d.dept_name;