SELECT COUNT(*) FROM employees;
SELECT SUM(salary) FROM employees;
SELECT AVG(salary) FROM employees;
SELECT MAX(salary) FROM employees;
SELECT MIN(salary) FROM employees;
SELECT dept, COUNT(*) as emp FROM employees
GROUP BY dept
ORDER BY emp DESC
LIMIT 1;
SELECT city, COUNT(*) as emp FROM employees
GROUP BY city
ORDER BY emp DESC
LIMIT 1;
SELECT dept, AVG(exp_yrs) as exp FROM employees
GROUP BY dept;
SELECT dept, COUNT(*) as count FROM employees
GROUP BY dept
HAVING count > 3;
SELECT dept, AVG(salary) as avg FROM employees
GROUP BY dept
HAVING avg > 70000;