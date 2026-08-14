SELECT * FROM Employees;

-- Find the top 3 highest-paid employees in department 1. Display their full_name and salary.
SELECT full_name, salary FROM Employees
WHERE dept_id = 1 ORDER BY salary DESC
LIMIT 3;

-- Difference between INNER JOIN and LEFT JOIN
-- INNER JOIN: Returns only the rows where there is a match in both joined tables.
-- LEFT JOIN: Returns all rows from the left table and matched rows from the right table. For non-matching rows from the right table, all its column values in the result set are filled with NULL.

-- Write a query to retrieve all employees whose email ends with `'@example.com'` and whose salary is between `$50,000` and `$90,000`.
SELECT * FROM Employees WHERE email LIKE '%@example.com' AND salary BETWEEN 50000 AND 90000;

-- Find all department IDs where the average employee salary is greater than $75,000.
SELECT dept_id FROM employees 
GROUP BY dept_id HAVING AVG(salary) > 75000;

-- What is First Normal Form (1NF)? What two main violations keep an unnormalized table from meeting 1NF?
-- A table is in 1NF if:
    -- Every column contains atomic (indivisible) values (no multi-value lists or CSVs in a single cell).
    -- There are no repeating groups of similar columns (e.g., phone1, phone2, phone3).
    -- Each record is uniquely identifiable (has a primary key).

-- Write a query using EXISTS to list all departments that currently have at least one employee assigned to them.
SELECT d.dept_id, d.dept_name FROM Departments d
WHERE EXISTS (
    SELECT 1 FROM Employees e 
    WHERE e.dept_id = d.dept_id);

-- Display the total number of employees and the average salary across the entire company. Alias the columns as Total_Staff and Average_Pay.
SELECT COUNT(emp_id) AS Total_Staff,
       ROUND(AVG(salary), 2) AS Average_Pay 
FROM employees;

-- What happens when you execute a DELETE statement on a parent table row if the child table's Foreign Key constraint is configured with ON DELETE CASCADE vs. ON DELETE RESTRICT?
-- ON DELETE CASCADE: When the parent record is deleted, all associated child records referencing it are automatically deleted.
-- ON DELETE RESTRICT (or NO ACTION): Prevents deletion of the parent record as long as child records reference it, throwing a foreign key violation error.

-- Find all employees who do not have a manager assigned (manager_id is missing).
SELECT emp_id, full_name FROM Employees WHERE manager_id IS NULL;

UPDATE Employees SET salary = 99000 WHERE emp_id = 101;

-- Find all employees whose salary is higher than the average salary of their own department (Correlated Subquery).
SELECT * FROM Employees e1 WHERE salary > (SELECT AVG(salary) FROM Employees e2 WHERE e1.dept_id = e2.dept_id);

-- Create a View named vw_ProjectAllocations that shows emp_id, full_name, project_name, and hours_worked.
CREATE VIEW vw_ProjectAllocations AS
SELECT 
    e.emp_id,
    e.full_name,
    p.project_name,
    ep.hours_worked
FROM Employees e
JOIN Employee_Projects ep ON e.emp_id = ep.emp_id
JOIN Projects p ON ep.project_id = p.project_id;
SELECT * FROM vw_projectallocations;

-- Why does the query SELECT * FROM Employees WHERE manager_id = NULL; fail to return rows? What is the correct syntax?
-- In SQL, NULL represents an unknown/missing state. Standard comparison operators (=, !=, <>) return UNKNOWN when compared to NULL. The correct syntax requires the IS NULL or IS NOT NULL predicate:
-- SELECT * FROM Employees WHERE manager_id IS NULL;

-- List all projects along with the total hours worked on each project. Include projects that currently have zero hours or no assigned employees.
SELECT p.project_id, p.project_name, ep.hours_worked FROM Projects p
LEFT JOIN Employee_projects ep 
ON p.project_id = ep.project_id;

-- What is a Composite Primary Key? Give a practical reason why Employee_Projects uses a composite key instead of a single auto-incrementing ID.
-- A Composite Primary Key is a primary key composed of two or more columns that together uniquely identify a record. In Employee_Projects, (emp_id, project_id) ensures an employee cannot be assigned to the exact same project multiple times, while avoiding duplicate artificial surrogate keys.

-- Write a query to list all distinct locations where departments are located, excluding NULL values, sorted alphabetically.
SELECT DISTINCT location FROM Departments 
WHERE location IS NOT NULL 
ORDER BY location ASC;

-- Find the employee(s) with the absolute lowest salary in the company using a scalar subquery.
-- A scalar subquery is a nested query inside a larger SQL statement that returns exactly one value (one row and one column). 
SELECT emp_id, full_name, salary FROM Employees WHERE salary = (
    SELECT MIN(salary) FROM Employees);

-- Explain the concept of Referential Integrity. Which SQL key enforces it?
-- Referential Integrity is a database property ensuring relationships between tables remain consistent. It prevents child tables from having invalid foreign keys pointing to nonexistent parent records. It is enforced using Foreign Keys (FOREIGN KEY).

-- Retrieve all employees hired between '2020-01-01' and '2020-12-31' who work in either department 1, 2, or 5.
SELECT * FROM Employees 
WHERE hire_date BETWEEN '2020-01-01' AND '2020-12-31'
AND dept_id IN (1, 2, 5);

-- Write a query that displays each department name and the count of projects assigned to employees in that department.
SELECT d.dept_id, d.dept_name, 
       COUNT(DISTINCT ep.project_id) AS project_count
FROM Departments d
LEFT JOIN Employees e ON e.dept_id = d.dept_id
LEFT JOIN Employee_Projects ep ON e.emp_id = ep.emp_id
GROUP BY d.dept_id, d.dept_name;

-- What is Second Normal Form (2NF)? Which key structural issue does 2NF aim to eliminate?
-- A table is in 2NF if:
    -- It is already in 1NF.
    -- It has no partial dependency — all non-key attributes must be fully functionally dependent on the entire primary key (relevant when tables have composite keys).

-- List all employees who are not currently assigned to any project in the Employee_Projects table using NOT IN or NOT EXISTS.
SELECT * FROM Employee_projects ep 
WHERE NOT EXISTS (
    SELECT 1 FROM Employees e WHERE
    e.emp_id = ep.emp_id);

-- Combine a list of current project names and department names into a single column result set, **keeping** all duplicate names if any exist.
SELECT project_name AS names FROM projects
UNION ALL
SELECT dept_name AS names FROM departments;