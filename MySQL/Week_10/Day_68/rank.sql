-- Rank all employees by salary.
SELECT eid, CONCAT(fname, ' ', lname) AS full_name, salary, RANK() OVER (ORDER BY salary) AS salary_rank 
FROM emp; -- Employee with same salary gets the same rank and the next rank will skip accordingly.

-- Rank employees by salary within each department.
SELECT eid, CONCAT(fname, ' ', lname) AS full_name, dept, salary, RANK() OVER (PARTITION BY dept ORDER BY salary) AS dept_salary_rank 
FROM emp; -- Each department gets its own ranking list, ordered by salary.

-- Find employees with the highest salary rank.
SELECT * FROM (
    SELECT eid, fname, lname, salary,
           RANK() OVER (ORDER BY salary DESC) AS salary_rank
    FROM emp) ranked
WHERE salary_rank = 1; -- Returns the top earners (if multiple employees share the highest salary, they all appear).

-- Find employees having the second salary rank.
SELECT * FROM (
    SELECT eid, fname, lname, salary,
           RANK() OVER (ORDER BY salary DESC) AS salary_rank
    FROM emp) ranked
WHERE salary_rank = 2; -- Returns the second top earners