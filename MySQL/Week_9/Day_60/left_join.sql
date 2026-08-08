-- 1. Show all employees even if they don't have projects.
SELECT e.*, p.project_name FROM employees e
LEFT JOIN projects p
ON e.emp_id = p.emp_id;
-- 2. Show all departments even if they have no employees.
SELECT d.*, e.emp_id FROM departments d 
LEFT JOIN employees e 
ON d.dept_name = e.dept;
-- 3. Show all employees and their managers.
SELECT e.*, d.manager FROM employees e 
LEFT JOIN departments d 
ON e.dept = d.dept_name;
-- 4. Find employees without projects.
SELECT e.first_name, e.last_name, p.project_name FROM employees e 
LEFT JOIN projects p 
ON e.emp_id = p.emp_id
WHERE p.emp_id IS NULL;
-- 5. Find departments without employees.
SELECT d.dept_name, d.manager 
FROM departments d
LEFT JOIN employees e 
ON d.dept_name = e.dept
WHERE e.emp_id IS NULL;

-- Key Takeaway for Filtering Missing Data with LEFT JOIN:
-- Whenever a question asks to "Find [X] without [Y]":

-- Put [X] in the FROM clause (left table).

-- LEFT JOIN with [Y] (right table).

-- Add WHERE [Y].primary_key IS NULL at the end!