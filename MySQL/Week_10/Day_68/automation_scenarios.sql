-- The HR dashboard displays the **top 3 employees in every department**
-- Write the query to validate it.

SELECT * FROM (
    SELECT *,
        RANK() OVER (PARTITION BY dept ORDER BY salary) AS top_emp
FROM emp) ranked
WHERE top_emp <= 3;

-- The application displays the **second-highest salary in each department**.
-- Validate it.
SELECT * FROM (
    SELECT *,
        DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary) AS emp_sal_rank
FROM emp) ranked
WHERE emp_sal_rank = 2;

-- The API returns an employee's rank within their department.
-- Calculate the rank from the database.
SELECT eid, fname, lname, dept, salary,
       RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS dept_rank
FROM emp;

-- The dashboard displays department average salary beside every employee.
-- Validate it.
SELECT eid, fname, lname, dept, salary,
       AVG(salary) OVER (PARTITION BY dept) AS dept_avg_salary
FROM emp;

-- The application displays salary change compared with the previous employee.
-- Use `LAG()`.
SELECT eid, fname, lname, salary,
       LAG(salary) OVER (ORDER BY salary DESC) AS prev_salary,
       salary - LAG(salary) OVER (ORDER BY salary DESC) AS salary_diff
FROM emp;

-- The application displays the next employee's joining date.
-- Use `LEAD()`.
SELECT eid, fname, lname, joining_date,
       LEAD(joining_date) OVER (ORDER BY joining_date ASC) AS next_joining_date
FROM emp;
