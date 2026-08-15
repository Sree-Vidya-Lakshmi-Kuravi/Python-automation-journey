-- Find all employees whose name contains the substring 'son' or starts with 'J' (case-insensitive).
SELECT * FROM Employees 
WHERE full_name LIKE '%an%' OR 
      full_name LIKE 'R%';

-- Write a query using GROUP BY to calculate the minimum, maximum, and average hours_worked per project.
SELECT project_id, MIN(hours_worked), MAX(hours_worked), AVG(hours_worked) FROM employee_projects
GROUP BY project_id;

-- Query your View vw_ProjectAllocations to find all employees who have worked more than 40 hours on a single project.
CREATE VIEW vw_ProjectAllocations AS
    SELECT * FROM Employee_Projects WHERE hours_worked > 40;
SELECT * FROM vw_ProjectAllocations;

-- Explain the difference between WHERE and HAVING. Can you use HAVING without a GROUP BY clause?
-- WHERE: Filters rows before any aggregation (GROUP BY) is computed. Cannot contain aggregate functions (like SUM(), AVG()).
-- HAVING: Filters groups after aggregation has occurred.
-- Can HAVING be used without GROUP BY? Yes, it acts on the entire query result as a single group (e.g., SELECT AVG(salary) FROM Employees HAVING AVG(salary) > 50000;).

-- Find all department names that have more than 5 employees.
SELECT d.dept_name, COUNT(e.emp_id) AS total_emps
FROM Departments d
INNER JOIN Employees e ON d.dept_id = e.dept_id
GROUP BY d.dept_id, d.dept_name
HAVING COUNT(e.emp_id) > 1;

-- Write a self-join query to display each employee's full_name alongside their manager's full_name. Alias the manager column as Manager_Name.
SELECT 
    e.full_name AS full_name,
    m.full_name AS Manager_Name
FROM Employees e
LEFT JOIN Employees m ON e.manager_id = m.emp_id;

-- What is a Foreign Key? Can a Foreign Key reference a column that is marked UNIQUE instead of a PRIMARY KEY?
-- A Foreign Key is a column or combination of columns that establishes a link between data in two tables.
-- Yes, a Foreign Key can reference any column that has a UNIQUE constraint, not just a PRIMARY KEY.

-- Select all employees whose salary is strictly greater than the maximum salary of department 3.
SELECT * FROM Employees WHERE salary > (
    SELECT MAX(salary) FROM Employees WHERE dept_id = 3);

-- What is Third Normal Form (3NF)? Explain what a Transitive Dependency is with a quick example.
-- A table is in 3NF if it is in 2NF and contains no transitive dependencies (non-key attributes depending on other non-key attributes: A -> B -> C).
-- Example: If Employees has (emp_id, zip_code, city), city depends on zip_code, which depends on emp_id. To satisfy 3NF, move zip_code and city to a separate ZipCodes table.

-- Write a query to retrieve the 5 most recently hired employees, skipping the single newest hire (i.e., rows 2 through 6).
SELECT emp_id, full_name FROM Employees 
ORDER BY hire_date DESC LIMIT 5 OFFSET 1;

-- List all projects where the total budget spent on employee salaries (calculated from assigned project hours or salary proportion) exceeds $100,000.
SELECT p.project_id, p.project_name, SUM(e.salary) FROM projects p
INNER JOIN 
employee_projects ep on ep.project_id = p.project_id
INNER JOIN
employees e on e.emp_id = ep.emp_id
GROUP BY p.project_id HAVING SUM(e.salary) > 100000;

-- Explain the difference between UNION and UNION ALL in terms of performance and output set handling.
-- UNION: Combines datasets and performs an internal distinct/sort operation to remove duplicates, which requires higher memory and CPU cost.
-- UNION ALL: Combines datasets without checking for duplicates, making it substantially faster.

-- Write a query to find all employees who work in the 'Headquarters' location by joining Employees and Departments.
SELECT e.emp_id, e.full_name, d.location FROM Employees e
INNER JOIN Departments d ON
e.dept_id = d.dept_id WHERE d.location = 'Headquarters';

-- Create a CHECK constraint concept: Write the SQL snippet to alter the Projects table so that budget cannot be negative or zero.
ALTER TABLE Projects 
MODIFY budget DECIMAL(10, 2) CHECK (budget > 0);

-- Find all departments that have no employees assigned to them using a LEFT JOIN.
SELECT d.dept_id, d.dept_name
FROM Departments d
LEFT JOIN Employees e ON d.dept_id = e.dept_id
WHERE e.emp_id IS NULL;

-- Display the total number of projects each employee is assigned to. Include the employee's full_name and order the output by project count descending.
SELECT 
    e.emp_id,
    e.full_name,
    COUNT(ep.project_id) AS project_count
FROM Employees e
LEFT JOIN Employee_Projects ep ON e.emp_id = ep.emp_id
GROUP BY e.emp_id, e.full_name
ORDER BY project_count DESC;

-- What is the purpose of the DEFAULT constraint? What value gets inserted if no explicit value or DEFAULT keyword is supplied during an INSERT statement?
-- The DEFAULT constraint provides a predefined value for a column when no value is provided during an INSERT. If omitted and no default is defined, the column receives NULL (or an error if marked NOT NULL).

-- Write a query using a subquery in the FROM clause (derived table) to calculate the average of department salary averages.
SELECT ROUND(AVG(dept_avg), 2) AS overall_dept_avg
FROM (
    SELECT dept_id, AVG(salary) AS dept_avg
    FROM Employees
    GROUP BY dept_id
) AS DeptWiseSal;
SELECT ROUND(AVG(s.AVG_salary), 2) as AVG_salary from (SELECT AVG(salary) as AVG_salary FROM employees e
INNER JOIN departments d on d.dept_id = e.dept_id) s;

-- Identify any employees who share the exact same `salary` as at least one other employee in a different department.
SELECT e1.emp_id, e1.full_name, e1.dept_id, e1.salary FROM Employees e1
INNER JOIN Employees e2 
ON e1.salary = e2.salary
AND e1.dept_id <> e2.dept_id;
SELECT e1.emp_id, e1.full_name, e1.dept_id, e1.salary
FROM Employees e1
WHERE EXISTS (
    SELECT 1 FROM Employees e2 WHERE e1.salary = e2.salary
      AND e1.dept_id <> e2.dept_id);
SELECT e1.emp_id, e1.full_name, e1.dept_id, e1.salary
FROM Employees e1
WHERE (
    SELECT COUNT(*) FROM Employees e2
    WHERE e1.salary = e2.salary AND e1.dept_id <> e2.dept_id) >= 1;

-- What happens to child table records when a parent record is deleted if the foreign key specifies ON DELETE SET NULL? What rule must the child column follow for this to work?
-- When the parent row is deleted, the foreign key column in the corresponding child records is set to NULL.
-- Rule: The child table column must allow NULL values (cannot have a NOT NULL constraint).

-- Find all projects whose name starts with 'Alpha' or ends with 'Beta'.
SELECT project_id, project_name FROM projects 
WHERE project_name LIKE 'Alpha%' OR 'Beta%';

-- Write a query to count the total number of distinct managers currently supervising at least one employee.
SELECT COUNT(DISTINCT manager_id) FROM Employees WHERE
manager_id IS NOT NULL;
SELECT COUNT(DISTINCT e1.emp_id) AS active_manager_count
FROM Employees e1
WHERE EXISTS (
    SELECT 1 FROM Employees e2 WHERE e2.manager_id = e1.emp_id);