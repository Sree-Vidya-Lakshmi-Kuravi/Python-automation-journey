-- A window frame specifies exactly which rows around the current row should be used in the calculation.

-- Calculate running salary total.
SELECT eid, fname, lname, salary,
SUM(salary) OVER (ORDER BY eid
                    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS total_sal
FROM emp;

-- Calculate running employee count.
SELECT eid, fname, lname, 
COUNT(*) OVER (ORDER BY eid
                ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS total_emp_count
FROM emp;

-- Calculate cumulative salary by department.
SELECT eid, fname, lname, salary, dept,
SUM(salary) OVER (PARTITION BY dept
                    ORDER BY salary
                    ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_dept_sal
FROM emp;