CREATE TABLE emp_test (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(20),
    salary DECIMAL(10, 2)
);

-- Insert a valid employee
INSERT INTO emp_test (emp_id, emp_name, salary)
    VALUES (1, 'Rohit', 89000);
SELECT * FROM emp_test;

-- Try inserting another employee with the same ID.
INSERT INTO emp_test (emp_id, emp_name, salary)
    VALUES (1, 'Surya', 40000); -- It shows the error as duplicate emp_id cannot be created

-- Try inserting NULL as the ID.
INSERT INTO emp_test (emp_id, emp_name, salary)
    VALUES (NULL, 'Ashwin', 50000); -- It shows the error as emp_id can be NULL