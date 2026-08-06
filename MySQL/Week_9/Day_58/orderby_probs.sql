use automation_testing;
-- ORDER BY
SELECT emp_id, first_name, last_name, salary FROM employees ORDER BY salary DESC;
SELECT emp_id, first_name, last_name, salary FROM employees ORDER BY salary ASC;
SELECT emp_id, first_name, last_name, exp_yrs FROM employees ORDER BY exp_yrs;
SELECT emp_id, first_name, last_name, dept, salary FROM employees ORDER BY dept ASC, salary DESC;
SELECT emp_id, first_name, last_name, joining_date FROM employees ORDER BY joining_date DESC;