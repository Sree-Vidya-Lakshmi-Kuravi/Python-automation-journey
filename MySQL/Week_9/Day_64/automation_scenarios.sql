CREATE TABLE users (
    user_id INT, email VARCHAR(25) UNIQUE, full_name VARCHAR(40));

-- Registration requires a unique email.
INSERT INTO users (user_id, email, full_name) 
VALUES (1, 'tester@company.com', 'Valid User');
INSERT INTO users (user_id, email, full_name) 
VALUES (2, 'tester@company.com', 'Duplicate User'); -- Throws error for duplicate email due to unique constraint 

-- Every employee must belong to a valid department.
-- verify foreign-key relationship.
-- Negative Assertion Test (Must throw Foreign Key Violation Exception)
INSERT INTO employees (emp_id, emp_name, dept_id) 
VALUES (501, 'Invalid Dept Test', 9999); -- Throws the foreign key violation 

SELECT * FROM employees;

-- Salary cannot be negative. verify the constraint.
ALTER TABLE users 
ADD salary INT CHECK (salary > 0);

INSERT INTO users (user_id, email, full_name, salary) 
VALUES (505, 'invalid.sal@gmail.com', 'Invalid Salary Test', -45000); -- Throws an error as it violates the salary's check constraint

-- New employees should automatically be Active. Verify DEFAULT.
ALTER TABLE users ADD status VARCHAR(20) DEFAULT 'Active';
INSERT INTO users (user_id, email, full_name,  salary) 
VALUES (400, 'status@gmail.com', 'Status Active', 89999);
SELECT * FROM users;

-- Employee Cannot Be Created Without an ID
-- Test 1: NULL Primary Key 
INSERT INTO employees (emp_id, emp_name, dept_id) 
VALUES (NULL, 'Null ID Test', 10); -- Throws an error that shows emp_id is NULL

-- Test 2: Duplicate Primary Key (Must throw Duplicate Entry Exception)
INSERT INTO employees (emp_id, emp_name, dept_id) 
VALUES (1, 'Duplicate ID Test', 10); -- Throws the error as the emp_id is duplicate and the primary key doesnot allow the duplicates

-- An employee-project assignment cannot be duplicated.verify composite key.
SELECT * FROM employee_projects;
INSERT INTO projects (project_id, project_name) 
VALUES (104, 'Project K');
SELECT * FROM projects;
-- Step 1: First Assignment (Succeeds)
INSERT INTO employee_projects (emp_id, project_id) 
VALUES (4, 103);

-- Step 2: Duplicate Pair Attempt (Must throw Composite Primary Key Exception)
INSERT INTO employee_projects (emp_id, project_id) 
VALUES (4, 103); -- Throws the error due to duplicate pair

-- Step 3: Different Project Pair (Succeeds)
INSERT INTO employee_projects (emp_id, project_id) 
VALUES (4, 104);