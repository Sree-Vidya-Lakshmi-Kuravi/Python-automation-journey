-- Number all employees according to salary from highest to lowest.
SELECT eid, CONCAT(fname, ' ', lname) AS full_name, salary, ROW_NUMBER() OVER (ORDER BY salary DESC) AS salary_row FROM emp; -- Based on salary arranged in descending order and gave the row numbers from 1

-- Number employees according to joining date.
SELECT eid, fname, joining_date, ROW_NUMBER() OVER (ORDER BY (YEAR(joining_date))) AS joining_date FROM emp; -- Employees are arranged based on their earliest joining dates

-- Number employees according to employee ID.
SELECT eid, fname, ROW_NUMBER() OVER (ORDER BY eid) AS eid_rank FROM emp;

-- Number employees separately within each department.
SELECT eid, CONCAT(fname, ' ', lname) AS full_name, dept, ROW_NUMBER() OVER (PARTITION BY dept ORDER BY salary) AS department FROM emp; -- Each department gets its own ranking list, ordered by salary.