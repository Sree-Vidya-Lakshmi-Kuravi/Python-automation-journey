SELECT emp_id, first_name, last_name FROM employees LIMIT 5;
SELECT emp_id, first_name, last_name, salary FROM employees ORDER BY salary DESC LIMIT 3;
SELECT emp_id, first_name, last_name, joining_date FROM employees ORDER BY joining_date DESC LIMIT 3;
SELECT emp_id, first_name, last_name, dept FROM employees WHERE dept = 'IT' LIMIT 10;  