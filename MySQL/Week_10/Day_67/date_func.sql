ALTER TABLE emp
ADD joining_date DATE;

-- Update each row with joining_date values
UPDATE emp SET joining_date = '2015-06-12' WHERE eid = 1;
UPDATE emp SET joining_date = '2012-03-08' WHERE eid = 2;
UPDATE emp SET joining_date = '2014-11-20' WHERE eid = 3;
UPDATE emp SET joining_date = '2016-07-15' WHERE eid = 4;
UPDATE emp SET joining_date = '2010-01-25' WHERE eid = 5;
UPDATE emp SET joining_date = '2008-09-10' WHERE eid = 6;
UPDATE emp SET joining_date = '2013-05-18' WHERE eid = 7;
UPDATE emp SET joining_date = '2000-02-01' WHERE eid = 8;
UPDATE emp SET joining_date = '2011-12-22' WHERE eid = 9;
UPDATE emp SET joining_date = '2005-04-30' WHERE eid = 10;

SELECT * FROM emp;

-- Display employees who joined in 2014.
SELECT eid, CONCAT(fname, ' ', lname) AS full_name FROM emp 
WHERE YEAR(joining_date) = 2014;

-- Display employees who joined in 2015.
SELECT eid, CONCAT(fname, ' ', lname) AS full_name FROM emp 
WHERE YEAR(joining_date) = 2015;

-- Display the joining year for every employee.
SELECT eid, YEAR(joining_date) AS joining_year FROM emp;

-- Display the joining month for every employee.
SELECT eid, MONTH(joining_date) AS joining_month FROM emp;

-- Find employees who joined after January 1, 2013.
SELECT eid, CONCAT(fname, ' ', lname) AS full_name, joining_date FROM emp WHERE joining_date > '2013-1-1';

-- Find employees who joined within a specified date range.
SELECT * FROM emp
WHERE joining_date BETWEEN '2012-01-01' AND '2015-12-31';

-- Calculate how many days each employee has been in the company.
SELECT eid, DATEDIFF(CURDATE(), joining_date) AS duration FROM emp;

-- Find employees who have been in the company for more than 1,000 days.
SELECT eid, fname, DATEDIFF(CURDATE(), joining_date) AS duration FROM emp
WHERE DATEDIFF(CURDATE(), joining_date) > 1000;

-- Find the earliest joining date.
SELECT MIN(joining_date) AS earliest_joining_date FROM emp;

-- Find the latest joining date.
SELECT MAX(joining_date) AS earliest_joining_date FROM emp;