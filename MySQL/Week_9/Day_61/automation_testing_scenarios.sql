-- 1. Employee displayed in UI belongs to the correct department
SELECT 
    e.emp_id, 
    CONCAT(e.first_name, ' ', e.last_name) AS ui_employee_name, 
    d.dept_name AS db_expected_department
FROM employees e
INNER JOIN departments d ON e.dept = d.dept_name
WHERE e.emp_id = 11; 
-- 2. Dashboard manager matches database
SELECT e.emp_id, e.first_name, d.manager FROM employees e
INNER JOIN departments d
ON e.dept = d.dept_name
WHERE e.emp_id = 10;
-- 3. Validate Employee Project Assignment
SELECT 
    e.emp_id, 
    e.first_name, 
    p.project_id, 
    p.project_name AS assigned_project
FROM employees e
INNER JOIN projects p ON e.emp_id = p.emp_id
WHERE e.emp_id = 10;
-- 4. Validate Employee Salary Displayed in UI Matches DB
SELECT 
    emp_id, 
    CONCAT(first_name, ' ', last_name) AS employee_name, 
    salary AS db_exp_salary
FROM employees
WHERE emp_id = 10;
-- 5. Validate Employee City Matches DB
SELECT 
    emp_id, 
    CONCAT(first_name, ' ', last_name) AS employee_name, 
    city AS db_exp_city
FROM employees
WHERE emp_id = 11;
-- 6. Validate Project Report Accuracy
SELECT 
    p.project_id, 
    p.project_name, 
    COUNT(DISTINCT p.emp_id) AS total_assigned_employees, 
    SUM(e.salary) AS total_project_salary_expense
FROM projects p
INNER JOIN employees e ON p.emp_id = e.emp_id
GROUP BY p.project_id, p.project_name
ORDER BY p.project_id;
-- 7. Validate Department-wise Employee List
SELECT 
    d.dept_name, 
    e.emp_id, 
    CONCAT(e.first_name, ' ', e.last_name) AS emp_name, 
    e.city
FROM departments d
INNER JOIN employees e ON d.dept_name = e.dept
WHERE d.dept_name = 'IT' 
ORDER BY e.emp_id;
-- 8. Validate Employees Not Assigned to Projects
SELECT 
    e.emp_id, 
    CONCAT(e.first_name, ' ', e.last_name) AS unassigned_emp_name, 
    e.dept AS department
FROM employees e
LEFT JOIN projects p ON e.emp_id = p.emp_id
WHERE p.emp_id IS NULL;