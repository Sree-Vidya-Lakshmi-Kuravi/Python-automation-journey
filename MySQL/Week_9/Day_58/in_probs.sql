SELECT emp_id, first_name, last_name, city FROM employees  WHERE city IN ('Hyderabad', 'Bangalore', 'Chennai');
SELECT emp_id, first_name, dept FROM employees WHERE dept IN ('IT', 'Finance');
SELECT emp_id, first_name, salary FROM employees WHERE salary IN (50000, 60000, 70000);
SELECT emp_id, first_name, designation FROM employees WHERE designation IN ('Support Engineer', 'Frontend Developer');