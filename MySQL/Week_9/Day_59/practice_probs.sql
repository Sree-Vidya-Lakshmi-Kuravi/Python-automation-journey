SELECT AVG(salary) AS avg_sal FROM employees 
WHERE dept = 'Marketing'
GROUP BY city;
SELECT dept, COUNT(*) AS emp_count FROM employees
GROUP BY dept
ORDER BY emp_count DESC;
SELECT dept, AVG(salary) AS avg_salary FROM employees
GROUP BY dept
HAVING AVG(salary) > 60000
ORDER BY avg_salary DESC;
SELECT city FROM employees
GROUP BY city
HAVING COUNT(*) > 2
ORDER BY city ASC;
SELECT dept, SUM(salary) AS total_salary FROM employees
GROUP BY dept
ORDER BY total_salary DESC;
SELECT dept, AVG(exp_yrs) AS avg_exp_yrs FROM employees
GROUP BY dept
ORDER BY avg_exp_yrs DESC;
SELECT city, COUNT(*) FROM employees
WHERE salary > 50000
GROUP BY city;
