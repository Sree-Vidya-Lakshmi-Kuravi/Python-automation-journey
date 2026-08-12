CREATE TABLE depts_test (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50));

CREATE TABLE emps_test (
    e_id INT PRIMARY KEY,
    fn VARCHAR(50),
    dept_id INT,
    FOREIGN KEY (dept_id) REFERENCES depts_test(dept_id));

-- Insert a valid department.
INSERT INTO depts_test (dept_id, dept_name)
    VALUES (101, 'ML');

-- Insert an employee referencing that department.
INSERT INTO emps_test (e_id, fn, dept_id) 
    VALUES (20, 'Shanmukha', 101);

-- Try inserting an employee with a department ID that doesn't exist.
INSERT INTO emps_test (e_id, fn, dept_id) 
    VALUES (21, 'Shan', 10); -- Throws the error as there is no such dept id.
