SELECT emp_id, first_name, salary FROM employees WHERE salary BETWEEN 50000 AND 80000;
SELECT emp_id, first_name, exp_yrs FROM employees WHERE exp_yrs BETWEEN 2 AND 5;
SELECT emp_id, first_name, joining_date FROM employees WHERE joining_date BETWEEN '2022-01-01' AND '2024-12-31';
SELECT emp_id, first_name FROM employees WHERE emp_id BETWEEN 5 AND 15;