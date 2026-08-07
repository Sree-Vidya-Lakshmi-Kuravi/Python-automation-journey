SELECT dept FROM employees
GROUP BY dept 
HAVING COUNT(*) > 3;
SELECT dept FROM employees
GROUP BY dept 
HAVING AVG(salary) > 70000;
SELECT city FROM employees
GROUP BY city 
HAVING COUNT(*) > 2;
SELECT dept FROM employees
GROUP BY dept 
HAVING SUM(salary) > 300000;
SELECT designation FROM employees
GROUP BY designation 
HAVING COUNT(*) <= 2;
SELECT dept FROM employees
GROUP BY dept 
HAVING MIN(salary) > 50000;
SELECT city FROM employees
GROUP BY city 
HAVING AVG(exp_yrs) > 4;