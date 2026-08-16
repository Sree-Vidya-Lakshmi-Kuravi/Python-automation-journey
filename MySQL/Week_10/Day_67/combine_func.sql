-- Display full employee names in uppercase.
SELECT eid, UPPER(CONCAT(fname, ' ', lname)) AS full_name FROM emp;

-- Display employees grouped by joining year.
SELECT YEAR(joining_date) AS joining_year, fname, lname
FROM emp
GROUP BY YEAR(joining_date), fname, lname ORDER BY joining_year;

-- Count employees by joining year.
SELECT YEAR(joining_date) AS joining_year, COUNT(*) AS num FROM emp
GROUP BY YEAR(joining_date)
ORDER BY joining_year;

-- Calculate average salary by joining year.
SELECT YEAR(joining_date) AS joining_year, AVG(salary) AS avg_sal FROM emp
GROUP BY YEAR(joining_date)
ORDER BY joining_year;

-- Display departments with average salary above ₹70,000.
SELECT dept, AVG(salary) AS avg_sal FROM emp GROUP BY dept
HAVING AVG(salary) > 70000;

-- Display employee names and salary categories, ordered by salary descending.
SELECT fname, lname, salary,
       CASE 
           WHEN salary >= 20000 THEN 'High'
           WHEN salary BETWEEN 10000 AND 19999 THEN 'Medium'
           ELSE 'Low'
       END AS salary_category
FROM emp
ORDER BY salary DESC;


-- Display employees who joined after 2013, categorized by experience.
SELECT fname, lname, joining_date, experience_years,
       CASE 
           WHEN experience_years >= 5 THEN 'Senior'
           WHEN experience_years BETWEEN 3 AND 4 THEN 'Mid-level'
           ELSE 'Junior'
       END AS experience_category
FROM emp
WHERE joining_date > '2013-01-01';

-- Count High/Medium/Low salary employees.
SELECT 
    CASE 
        WHEN salary >= 20000 THEN 'High'
        WHEN salary BETWEEN 10000 AND 19999 THEN 'Medium'
        ELSE 'Low'
    END AS salary_category,
    COUNT(*) AS employee_count
FROM emp
GROUP BY salary_category;

-- Display the number of employees in each experience category.
SELECT 
       CASE 
           WHEN experience_years >= 5 THEN 'Senior'
           WHEN experience_years BETWEEN 3 AND 4 THEN 'Mid-level'
           ELSE 'Junior'
       END AS experience_category,
       COUNT(*) AS emp_count
FROM emp
GROUP BY experience_category;