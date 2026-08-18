-- Find the top 3 highest-paid employees in each department.
-- Use:
-- - `PARTITION BY`
-- - `DENSE_RANK()`
SELECT *,
DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary) AS emp_rank FROM emp;

-- Find departments whose average salary is above the company average. Use:
    -- - `GROUP BY`
    -- - aggregate function
    -- - subquery
SELECT dept, AVG(salary) AS dept_avg_salary
FROM emp
GROUP BY dept
HAVING AVG(salary) > (
    SELECT AVG(salary) FROM emp
);

-- Find employees earning more than their department average.
-- Use:
-- - JOIN/window function/subquery
-- Try solving it **two different ways**.
SELECT e.eid, e.dept, e.salary
FROM emp e
WHERE e.salary > (
    SELECT AVG(salary) FROM emp WHERE dept = e.dept);
SELECT eid, dept, salary, dept_avg
FROM (SELECT eid, dept, salary, AVG(salary) OVER (PARTITION BY dept) AS dept_avg FROM emp
) t WHERE salary > dept_avg;

-- Find departments with no employees.
-- Use:
-- - `LEFT JOIN`
-- - `IS NULL`
SELECT d.dept_id, d.dept_name
FROM departments d
LEFT JOIN emp e
    ON d.dept_id = e.dept
WHERE e.eid IS NULL;

-- Find employees who aren't assigned to any project.
-- Use:
-- - `NOT EXISTS` or `LEFT JOIN`
SELECT e.eid, e.fname, e.dept
FROM emp e
WHERE NOT EXISTS (
    SELECT 1 FROM project_assign pa
    WHERE pa.emp_id = e.eid);

-- Find the second-highest salary in every department.
-- Use:
-- - window function
SELECT dept, eid, salary
FROM (
    SELECT eid, dept, salary,
           DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS rnk
    FROM emp) t
WHERE rnk = 2;

-- Find duplicate email addresses.
-- Use:
-- - `GROUP BY`
-- - `HAVING`
SELECT email, COUNT(*) AS occurrences
FROM employees
GROUP BY email
HAVING COUNT(*) > 1;

-- Find employees who joined in the same year as another employee.
-- Use:
-- - date function
-- - subquery/self-join
SELECT DISTINCT e1.eid, e1.fname, e1.joining_date
FROM emp e1
JOIN emp e2
    ON e1.eid <> e2.eid AND YEAR(e1.joining_date) = YEAR(e2.joining_date);

-- Create a report containing:
-- - Employee
-- - Department
-- - Salary
-- - Salary category
-- - Department rank
-- - Department average salary
-- Use:
-- - JOIN
-- - CASE
-- - window functions

SELECT 
    e.eid,
    e.fname AS employee,
    e.dept AS department,
    e.salary,
    CASE 
        WHEN e.salary < 10000 THEN 'Low'
        WHEN e.salary BETWEEN 10000 AND 20000 THEN 'Medium'
        ELSE 'High'
    END AS salary_category,
    RANK() OVER (PARTITION BY e.dept ORDER BY e.salary DESC) AS dept_rank,
    AVG(e.salary) OVER (PARTITION BY e.dept) AS dept_avg_salary
FROM emp e;

-- Find employees whose salary is greater than the previous employee's salary.
-- Use:
-- - `LAG()`
SELECT eid, fname, dept, salary, prev_salary
FROM (
    SELECT eid, fname, dept, salary,
           LAG(salary) OVER (PARTITION BY dept ORDER BY salary) AS prev_salary
    FROM emp
) t
WHERE salary > prev_salary; 