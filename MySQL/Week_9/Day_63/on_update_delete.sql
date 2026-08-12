-- Parent Table
CREATE TABLE departments_sandbox (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);
-- Child Table with Cascading Actions
CREATE TABLE employees_sandbox (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    department_id INT,
    FOREIGN KEY (department_id) 
        REFERENCES departments_sandbox(department_id) 
        ON DELETE CASCADE 
        ON UPDATE CASCADE
);

-- Insert Sample Data
INSERT INTO departments_sandbox VALUES (10, 'Engineering');
INSERT INTO employees_sandbox VALUES (101, 'Alex', 10), (102, 'Sam', 10);

-- Update a Parent Key (ON UPDATE CASCADE)
UPDATE departments_sandbox 
SET department_id = 500 
WHERE department_id = 10;

SELECT * FROM employees_sandbox;

-- Delete a Parent Record (ON DELETE CASCADE)
DELETE FROM departments_sandbox WHERE department_id = 500;

SELECT * FROM employees_sandbox; -- Empty tables