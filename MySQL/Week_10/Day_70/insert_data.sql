-- 1. Insert Departments (including an empty one for Section C)
INSERT INTO departments (department_id, department_name, manager_id) VALUES
(1, 'QA', 101),
(2, 'Engineering', 102),
(3, 'HR', 103),
(4, 'Marketing', NULL); -- Department with no employees

-- 2. Insert Projects
INSERT INTO projects (project_id, project_name) VALUES
(201, 'Automation Framework'),
(202, 'Cloud Migration'),
(203, 'Mobile App'),
(204, 'Internal Tooling');

-- 3. Insert Employees
INSERT INTO employees (employee_id, first_name, last_name, email, job_title, salary, city, joining_date, department_id, manager_id) VALUES
-- Managers
(101, 'Amit', 'Verma', 'amit.verma@company.com', 'QA Lead', 95000, 'Hyderabad', '2021-03-15', 1, NULL),
(102, 'Ananya', 'Rao', 'ananya.rao@company.com', 'Dev Manager', 110000, 'Bangalore', '2020-01-10', 2, NULL),
(103, 'Suresh', 'Nair', 'suresh.nair@company.com', 'HR Lead', 65000, 'Hyderabad', '2022-06-01', 3, NULL);

-- Target Record for Automation Scenario
INSERT INTO employees (employee_id, first_name, last_name, email, job_title, salary, city, joining_date, department_id, manager_id) VALUES 
(125, 'Rahul', 'Sharma', 'rahul.sharma@company.com', 'QA Engineer', 75000, 'Hyderabad', '2024-02-15', 1, 101),
-- QA Team (to make QA department count > 3)
(104, 'Aakash', 'Gupta', 'aakash.gupta@company.com', 'QA Engineer', 62000, 'Bangalore', '2023-04-12', 1, 101),
(105, 'Pooja', 'Hegde', 'pooja.hegde@company.com', 'QA Engineer', 48000, 'Hyderabad', '2025-01-20', 1, 101),
-- Engineering Team (to test cities, NULL values, and salary bands)
(106, 'Vikram', 'Singh', 'vikram.singh@company.com', 'Backend Dev', 85000, 'Bangalore', '2022-11-05', 2, 102),
(107, 'Sneha', 'Patil', 'sneha.patil@company.com', 'Frontend Dev', 55000, NULL, '2023-08-18', 2, 102),
(108, 'Arjun', 'Reddy', 'arjun.reddy@company.com', 'DevOps Engineer', 92000, 'Hyderabad', '2021-09-01', 2, 102),
-- HR / Unassigned Employee (to test employees without projects)
(109, 'Meera', 'Iyer', 'meera.iyer@company.com', 'HR Associate', 42000, 'Chennai', '2024-05-10', 3, 103);

-- 4. Assign Employees to Projects
INSERT INTO employee_projects (employee_id, project_id) VALUES
(125, 201), -- Rahul Sharma -> Automation Framework
(101, 201), -- Amit Verma -> Automation Framework
(104, 201), -- Aakash Gupta -> Automation Framework
(106, 202), -- Vikram Singh -> Cloud Migration
(108, 202), -- Arjun Reddy -> Cloud Migration
(107, 203); -- Sneha Patil -> Mobile App
-- Note: Employees 103, 105, and 109 have no project assigned.

SELECT * FROM departments;
SELECT * FROM projects;
SELECT * FROM employees;
SELECT * FROM employee_projects;