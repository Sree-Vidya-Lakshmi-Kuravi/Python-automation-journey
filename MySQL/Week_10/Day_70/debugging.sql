-- SELECT department, AVG(salary) FROM employees;
SELECT department_id, AVG(salary) AS avg_sal FROM employees GROUP BY department_id;

-- SELECT * FROM employees WHERE salary = NULL;
SELECT * FROM employees WHERE salary IS NULL;

-- SELECT department, COUNT(*) FROM employees WHERE COUNT(*) > 3 GROUP BY department;
SELECT department_id, COUNT(*) AS emp_count FROM employees GROUP BY department_id HAVING COUNT(*) > 3;

-- SELECT e.first_name, d.department_name FROM employees e JOIN departments d;
SELECT e.first_name, d.department_name FROM employees e
JOIN departments d ON e.department_id = d.department_id;

-- SELECT * FROM employees WHERE department_id IN SELECT department_id FROM departments;
SELECT * FROM employees
WHERE department_id IN (
    SELECT department_id FROM departments);