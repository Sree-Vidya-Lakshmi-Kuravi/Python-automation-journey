-- 11. Display:
    -- Employee Name
    -- Department
    -- Manager
SELECT 
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    d.department_name,
    CONCAT(m.first_name, ' ', m.last_name) AS manager_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id
LEFT JOIN employees m ON e.manager_id = m.employee_id;

-- 12. Find employees who don't have a project.
SELECT e.*
FROM employees e
LEFT JOIN employee_projects ep 
ON e.employee_id = ep.employee_id
WHERE ep.project_id IS NULL;

-- 13. Display:
    -- Employee
    -- Department
    -- Project
SELECT 
    CONCAT(e.first_name, ' ', e.last_name) AS employee_name,
    d.department_name,
    p.project_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id
LEFT JOIN employee_projects ep ON e.employee_id = ep.employee_id
LEFT JOIN projects p ON ep.project_id = p.project_id;

-- 14. Find departments that have no employees.
SELECT d.*
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
WHERE e.employee_id IS NULL;

-- 15. Find employees working on a specific project.
SELECT e.*
FROM employees e
JOIN employee_projects ep ON e.employee_id = ep.employee_id
JOIN projects p ON ep.project_id = p.project_id
WHERE p.project_name = 'Automation Framework';