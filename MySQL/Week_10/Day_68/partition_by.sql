-- Partition by divides the dataset into logical groups while retaining the individual rows.

-- Rank employees by salary within each department.
SELECT eid, CONCAT(fname, ' ', lname) AS full_name, dept, salary, DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary) AS dept_wise_sal_rank FROM emp;

-- Number employees within each department.
SELECT eid, CONCAT(fname, ' ', lname) AS full_name, dept, ROW_NUMBER() OVER (PARTITION BY dept ORDER BY eid) AS count_emp FROM emp;

-- Find the highest-paid employee in every department.
SELECT * FROM (
    SELECT eid, CONCAT(fname, ' ', lname) AS full_name, dept, salary, DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS sal_rank FROM emp
) ranked WHERE sal_rank = 1;

-- Find the lowest-paid employee in every department.
SELECT * FROM (
    SELECT eid, CONCAT(fname, ' ', lname) AS full_name, dept, salary, DENSE_RANK() OVER (PARTITION BY dept ORDER BY salary ASC) AS sal_rank FROM emp
) ranked WHERE sal_rank = 1;

-- Find the top 3 employees by salary in every department.
SELECT * FROM (
    SELECT eid, CONCAT(fname, ' ', lname) AS full_name, dept, salary, RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS sal_rank FROM emp
) ranked WHERE sal_rank <= 3;