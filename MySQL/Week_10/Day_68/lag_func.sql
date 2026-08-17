-- LAG() - Helps you to access a previous row

-- Display each employee's salary and the previous employee's salary.
SELECT eid, fname, salary,
LAG(salary) OVER (ORDER BY salary) AS previous_emp_sal
FROM emp;

-- Display each employee's joining date and the previous joining date.
SELECT eid, fname, joining_date,
LAG(joining_date) OVER (ORDER BY joining_date) AS previous_j_date
FROM emp;

-- Calculate the salary difference between the current and previous employee.
SELECT eid, fname, salary,
LAG(salary) OVER (ORDER BY salary) AS prev_sal,
salary - LAG(salary) OVER (ORDER BY salary) AS sal_diff
FROM emp;