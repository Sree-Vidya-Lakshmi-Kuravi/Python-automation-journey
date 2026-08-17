-- Dense rank ranks the duplicates the same rank, but doesnot skip the next rank like row_number() or rank()

-- Rank employees using DENSE_RANK().
SELECT eid, CONCAT(fname, ' ', lname) AS full_name, salary, dept, 
DENSE_RANK() OVER (ORDER BY salary) as sal_drank 
FROM emp;

-- Find the second-highest salary.
SELECT * FROM (SELECT eid, CONCAT(fname, ' ', lname) AS full_name, salary, dept, 
DENSE_RANK() OVER (ORDER BY salary DESC) as sal_drank 
FROM emp) ranked
WHERE sal_drank = 2;

-- Find the third-highest salary.
SELECT * FROM (SELECT eid, CONCAT(fname, ' ', lname) AS full_name, salary, dept, 
DENSE_RANK() OVER (ORDER BY salary DESC) as sal_drank 
FROM emp) ranked
WHERE sal_drank = 3;

-- Find the second-highest salary in every department.
SELECT * FROM (SELECT eid, CONCAT(fname, ' ', lname) AS full_name, salary, dept, 
DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC) as dept_sal_denserank 
FROM emp) ranked
WHERE dept_sal_denserank = 2;