-- Employee exists.
SELECT * FROM emp WHERE eid = 2;

-- Name is correct.
SELECT * FROM emp WHERE fname = 'Anirudh' AND lname = 'Ravichander';

-- Department is correct.
SELECT * FROM emp WHERE dept = 'Music';

-- Salary is correct.
SELECT * FROM emp WHERE salary = 20000;

-- Employee belongs to the correct department.
SELECT * FROM emp WHERE dept = 'Acting';

-- Employee's salary is above department average.
SELECT e.eid, e.fname, e.salary, dept_avg
FROM (
    SELECT eid, fname, dept, salary,
           AVG(salary) OVER (PARTITION BY dept) AS dept_avg
    FROM emp
) e
WHERE e.eid = 12 
  AND e.salary > e.dept_avg;

-- Employee's department rank is correct.
SELECT eid, fname, dept, salary,
       RANK() OVER (PARTITION BY dept ORDER BY salary DESC) AS dept_rank
FROM emp
WHERE dept = 'Acting';

-- No duplicate employee email exists.
SELECT email, COUNT(*) AS occurrences
FROM emp
GROUP BY email
HAVING COUNT(*) > 1;
