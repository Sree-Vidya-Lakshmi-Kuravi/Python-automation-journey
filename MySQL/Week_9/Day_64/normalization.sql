-- 1. Departments Table (Master data for departments)
CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL,
    manager_name VARCHAR(50));

-- 2. Projects Table (Master data for projects)
CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(50) NOT NULL);

-- 3. Employees Table (Master data for employees)
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50) NOT NULL,
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES departments(dept_id));

-- 4. Employee_Projects Table (Junction table for many-to-many relationship)
CREATE TABLE employee_projects (
    emp_id INT,
    project_id INT,
    PRIMARY KEY (emp_id, project_id),
    FOREIGN KEY (emp_id) REFERENCES employees(emp_id) ON DELETE CASCADE,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE);

-- 1. Insert Departments
INSERT INTO departments (dept_id, dept_name, manager_name) VALUES
(10, 'IT', 'Rohit'),
(20, 'Finance', 'Suresh'),
(30, 'HR', 'Priya');

-- 2. Insert Projects
INSERT INTO projects (project_id, project_name) VALUES
(101, 'IMS'),
(102, 'Budgeting'),
(103, 'Payroll System');

-- 3. Insert Employees
INSERT INTO employees (emp_id, emp_name, dept_id) VALUES
(1, 'Alice', 10),
(2, 'Bob', 10),
(3, 'Charlie', 20),
(4, 'David', 30);

-- 4. Assign Employees to Projects
INSERT INTO employee_projects (emp_id, project_id) VALUES
(1, 101), -- Alice on IMS
(1, 102), -- Alice on Budgeting
(2, 101), -- Bob on IMS
(3, 102); -- Charlie on Budgeting

SELECT 
    e.emp_id,
    e.emp_name,
    d.dept_name,
    d.manager_name,
    p.project_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id
LEFT JOIN employee_projects ep ON e.emp_id = ep.emp_id
LEFT JOIN projects p ON ep.project_id = p.project_id
ORDER BY e.emp_id;