-- 1. Verify that an employee created through the application exists in the database
SELECT * FROM employees WHERE emp_id = 2;

-- 2. Verify that the employee belongs to the correct department.
SELECT e.emp_id, 
    CONCAT(e.first_name, ' ', e.last_name) AS emp_name, 
    e.dept, d.dept_name
FROM employees e
INNER JOIN departments d ON e.dept = d.dept_name
WHERE e.emp_id = 10;

-- 3. Verify that the employee's salary is correct
SELECT emp_id, 
    CONCAT(first_name, ' ', last_name) AS employee_name, 
    salary 
FROM employees WHERE emp_id = 4;

-- 4. Verify that the employee has been assigned to a project
SELECT e.emp_id, 
    CONCAT(e.first_name, ' ', e.last_name) AS emp_name, 
    p.project_id, p.project_name
FROM employees e
INNER JOIN projects p ON e.emp_id = p.emp_id
WHERE e.emp_id = 3;

-- 5. Verify that employees without project assignments are correctly identified
SELECT e.emp_id, 
    CONCAT(e.first_name, ' ', e.last_name) AS unassigned_emp_name, e.dept
FROM employees e
LEFT JOIN projects p ON e.emp_id = p.emp_id
WHERE p.emp_id IS NULL;

-- 6. Verify that the employee belongs to the department with the expected manager
SELECT e.emp_id, 
    CONCAT(e.first_name, ' ', e.last_name) AS emp_name, 
    e.dept AS dept_name, d.manager AS expected_mgr
FROM employees e
INNER JOIN departments d ON e.dept = d.dept_name
WHERE e.emp_id = 7;

-- 7. Find employees whose database salary differs from an expected value
SELECT emp_id, first_name, salary FROM employees 
WHERE salary IS NULL OR salary <= 0;

-- 8. Find employees whose department assignment is missing
SELECT e.emp_id, e.first_name, e.last_name, e.dept
FROM employees e
LEFT JOIN departments d ON e.dept = d.dept_name
WHERE e.dept IS NULL 
   OR d.dept_name IS NULL;