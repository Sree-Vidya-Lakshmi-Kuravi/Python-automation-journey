SELECT dept, COUNT(*) FROM employees
GROUP BY dept;
SELECT city, COUNT(*) FROM employees
GROUP BY city;
SELECT dept, AVG(salary) FROM employees
GROUP BY dept;
SELECT dept, MIN(salary) FROM employees
GROUP BY dept;
SELECT dept, MAX(salary) FROM employees
GROUP BY dept;
SELECT dept, SUM(salary) FROM employees
GROUP BY dept;
SELECT AVG(exp_yrs) FROM employees
GROUP BY dept;
SELECT designation, COUNT(emp_id) FROM employees
GROUP BY designation;
SELECT city, COUNT(emp_id) FROM employees
GROUP BY city;
SELECT city, SUM(salary) FROM employees
GROUP BY city;