SELECT COUNT(*) AS emp_count FROM employees;
SELECT AVG(salary) AS emp_avg_sal FROM employees;
SELECT COUNT(*) AS emp_count FROM employees
WHERE dept = 'Finance';
SELECT MAX(salary) FROM employees;
SELECT dept, COUNT(*) AS emp_count FROM employees
GROUP BY dept;
SELECT COUNT(YEAR(joining_date)) AS emp_joined FROM employees
WHERE YEAR(joining_date) = '2022';
SELECT AVG(exp_yrs) AS emp_avg_yrs FROM employees;
SELECT COUNT(salary) AS sal_c,
       MIN(salary) AS min_sal,
       MAX(salary) AS max_sal,
       AVG(salary) AS avg_sal,
       SUM(salary) AS total_sal
FROM employees;