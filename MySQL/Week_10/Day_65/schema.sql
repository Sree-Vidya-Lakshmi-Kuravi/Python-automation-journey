DROP VIEW IF EXISTS hr_dashboard;
CREATE TABLE Departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(20) UNIQUE NOT NULL,
    location VARCHAR(20) DEFAULT 'Headquarters' 
);

CREATE TABLE Employees (
    emp_id INT PRIMARY KEY,
    full_name VARCHAR(45) NOT NULL,
    email VARCHAR(45) UNIQUE,
    salary DECIMAL(10, 2) CHECK (salary > 0),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES Departments (dept_id) ON DELETE SET NULL,
    manager_id INT,
    FOREIGN KEY (manager_id) REFERENCES Employees (emp_id),
    hire_date DATE);

CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(40),
    budget DECIMAL(10, 2)
);

CREATE TABLE employee_projects (
    emp_id INT,
    FOREIGN KEY (emp_id) REFERENCES Employees (emp_id) ON DELETE CASCADE,
    project_id INT,
    FOREIGN KEY (project_id) REFERENCES Projects (project_id) ON DELETE CASCADE,
    hours_worked DECIMAL(10, 2) DEFAULT 0,
    PRIMARY KEY (emp_id, project_id));

INSERT INTO Departments (dept_id, dept_name, location) VALUES
(1, 'HR', 'Headquarters'),
(2, 'IT', 'Bangalore'),
(3, 'Finance', 'Mumbai'),
(4, 'Marketing', 'Delhi'),
(5, 'Operations', 'Chennai');

INSERT INTO Employees (emp_id, full_name, email, salary, dept_id, manager_id, hire_date) VALUES
(101, 'MS Dhoni', 'ms.dhoni@example.com', 990000.00, 1, NULL, '2021-03-10'), -- HR
(102, 'Virat Kohli', 'virat.kohli@example.com', 95000.00, 2, 101, '2020-01-15'), -- IT Manager
(103, 'Rohit Sharma', 'rohit.sharma@example.com', 88000.00, 3, 101, '2022-07-01'), -- Finance
(104, 'Anirudh Ravichander', 'anirudh.r@example.com', 85000.00, 4, 101, '2023-05-20'), -- Marketing
(105, 'Rajinikanth', 'rajinikanth@example.com', 80000.00, 5, 101, '2024-02-12'), -- Operations
(106, 'Kajal Aggarwal', 'kajal.aggarwal@example.com', 75000.00, 4, 104, '2021-11-05'), -- Marketing under Anirudh
(107, 'Hardik Pandya', 'hardik.pandya@example.com', 72000.00, 2, 101, '2022-09-18'), -- IT under Virat
(108, 'Deepika Padukone', 'deepika.padukone@example.com', 70000.00, 3, 103, '2023-04-25'), -- Finance under Rohit
(109, 'Allu Arjun', 'allu.arjun@example.com', 68000.00, 5, 105, '2024-06-30'), -- Operations under Rajini
(110, 'Shreya Ghoshal', 'shreya.ghoshal@example.com', 66000.00, 1, 102, '2022-12-10'); -- HR under Dhoni


INSERT INTO Projects (project_id, project_name, budget) VALUES
(201, 'Website Revamp', 150000.00),
(202, 'Payroll Automation', 80000.00),
(203, 'Marketing Campaign', 120000.00),
(204, 'ERP Implementation', 200000.00),
(205, 'Customer Support Portal', 95000.00);


INSERT INTO Employee_projects (emp_id, project_id, hours_worked) VALUES
(101, 201, 120.50), -- Virat on Website Revamp
(102, 202, 95.00),  -- Dhoni on Payroll Automation
(103, 202, 110.75), -- Rohit on Payroll Automation
(104, 203, 80.00),  -- Anirudh on Marketing Campaign
(105, 204, 100.00), -- Rajini on ERP Implementation
(106, 203, 65.00),  -- Kajal on Marketing Campaign
(107, 201, 70.50),  -- Hardik on Website Revamp
(108, 202, 85.00),  -- Deepika on Payroll Automation
(109, 205, 90.00),  -- Allu Arjun on Customer Support Portal
(110, 204, 75.00);  -- Shreya on ERP Implementation

SELECT * FROM Departments;
SELECT * FROM Employees;
SELECT * FROM Projects;
SELECT * FROM Employee_projects;