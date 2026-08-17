-- LEAD() - It lets you access a next row.

-- Display current salary and next salary.
SELECT eid, fname, salary,
LEAD(salary) OVER (ORDER BY salary) AS next_sal
FROM emp;

-- Display current joining date and next joining date.
SELECT eid, fname, joining_date,
LEAD(joining_date) OVER (ORDER BY joining_date) AS next_j_date
FROM emp;

-- Calculate the difference between current and next salary.
SELECT eid, fname, salary,
LEAD(salary) OVER (ORDER BY salary) AS next_sal,
LEAD(salary) OVER (ORDER BY salary) - salary as sal_diff
FROM emp;