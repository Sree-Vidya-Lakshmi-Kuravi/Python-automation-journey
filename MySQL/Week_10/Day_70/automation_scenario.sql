-- Verify Employee 125 exists.
SELECT * FROM employees WHERE employee_id = 125;

-- Verify Employee name is correct.
SELECT * FROM employees WHERE first_name = 'Rahul';

-- Department is correct.
SELECT (d.department_name = 'QA') AS correct_dept
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE e.employee_id = 125;

-- Salary is correct.
SELECT (salary = 75000) AS sal FROM employees 
WHERE employee_id = 125;

-- Verify Employee has the correct project ('Automation Framework')
SELECT (p.project_name = 'Automation Framework') AS project_is_correct FROM employee_projects ep
JOIN projects p ON ep.project_id = p.project_id
WHERE ep.employee_id = 125;

-- Department manager is correct.
SELECT (e.manager_id = d.manager_id) AS correct_manager
FROM employees e
JOIN departments d ON e.department_id = d.department_id
WHERE e.employee_id = 125;

-- Verify Salary is above the department average
SELECT (e.salary > dept_stats.avg_salary) AS is_above_dept_avg
FROM employees e
JOIN (
    SELECT department_id, AVG(salary) AS avg_salary
    FROM employees
    GROUP BY department_id
) dept_stats 
ON e.department_id = dept_stats.department_id
WHERE e.employee_id = 125;

-- Verify Employee's department salary rank
WITH DeptRanked AS (
    SELECT 
        employee_id, 
        DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) as rank_pos
    FROM employees
)
SELECT rank_pos
FROM DeptRanked
WHERE employee_id = 125;

-- Verify Employee email is unique (No duplicate occurrences)
SELECT COUNT(*) = 1 AS is_email_unique
FROM employees
WHERE email = (SELECT email FROM employees WHERE employee_id = 125);

-- Verify Employee does not have duplicate project assignments
SELECT COUNT(project_id) = COUNT(DISTINCT project_id) AS has_no_duplicate_projects FROM employee_projects
WHERE employee_id = 125;