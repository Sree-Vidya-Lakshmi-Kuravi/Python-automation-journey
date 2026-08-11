CREATE VIEW emp_details AS
    SELECT emp_id, CONCAT(first_name, " ", last_name) AS emp_name, dept, salary FROM employees;

CREATE VIEW emp_ws AS
    SELECT e.emp_id, CONCAT(e.first_name, " ", e.last_name) AS emp_name, e.dept FROM employees e
    LEFT JOIN departments d  ON e.dept = d.dept_name
    LEFT JOIN projects p ON e.emp_id = p.emp_id;

-- Find IT Employees from View
SELECT * FROM emp_details WHERE dept = 'IT';

-- Find Employees Earning More than ₹70,000 from View
SELECT * FROM emp_details WHERE salary > 70000;

-- View for HR Dashboard Summary
CREATE VIEW hr_dashboard AS
    SELECT d.dept_name,
    COUNT(e.emp_id) AS total_emp,
    SUM(e.salary) AS total_salary,
    ROUND(AVG(e.salary), 2) AS avg_salary,
    ROUND(AVG(e.exp_yrs), 2) AS avg_exp_yrs
FROM departments d
LEFT JOIN employees e ON d.dept_name = e.dept
GROUP BY d.dept_id, d.dept_name, d.manager;

SELECT * FROM hr_dashboard;
