
select distinct dept from employees;
CREATE TABLE departments (
    dept_id INT,
    dept_name VARCHAR(40),
    manager VARCHAR(45)
);

INSERT INTO departments (dept_id, dept_name, manager) VALUES 
    (101, "IT", "Mallikarjun"),
    (102, "Finance", "Sulochana"),
    (103, "Marketing", "Sasi"),
    (104, "HR", "Saila");

INSERT INTO departments (dept_id, dept_name, manager) VALUES 
    (105, "Support", "Rohit");

ALTER TABLE employees ADD dept_id INT;
UPDATE employees 
SET dept_id = 101 
WHERE dept = 'IT';
UPDATE employees 
SET dept_id = 102 
WHERE dept = 'Finance';
UPDATE employees 
SET dept_id = 103 
WHERE dept = 'Marketing';
UPDATE employees 
SET dept_id = 105 
WHERE dept = 'Support';
UPDATE employees 
SET dept_id = 104 
WHERE dept = 'HR';
SELECT dept, dept_id FROM employees;
CREATE TABLE projects (
    project_id INT,
    project_name VARCHAR(100),
    emp_id INT
);

SELECT emp_id, dept FROM employees; --WHERE dept = 'Support';

INSERT INTO projects (project_id,  project_name, emp_id) VALUES
(1, 'IMS', 1),(1, 'IMS', 2),(1, 'IMS', 6),(1, 'IMS', 9),(1, 'IMS', 13), (1, 'IMS', 18), (1, 'IMS', 23), (2, 'Budgeting', 3), (2, 'Budgeting', 7), (2, 'Budgeting', 24),(2, 'Budgeting', 12), (2, 'Budgeting', 16), (2, 'Budgeting', 19), (3, 'Product Promotion', 4), (3, 'Product Promotion', 10), (3, 'Product Promotion', 15), (3, 'Product Promotion', 21), (3, 'Product Promotion', 25), (5, 'Meta Geeks', 8), (5, 'Meta Geeks', 14), (5, 'Meta Geeks', 20), (1, 'IMS', 5), (1, 'IMS', 11), (1, 'IMS', 17), (1, 'IMS', 22);   

SELECT * FROM projects;