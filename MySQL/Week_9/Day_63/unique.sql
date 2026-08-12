ALTER TABLE emp_test
    ADD UNIQUE (email);

SELECT * FROM emp_test;

-- Insert two employees with different emails.
INSERT INTO emp_test (emp_id, emp_name, salary, email)
VALUES 
    (9, 'Vaishu', 72000, 'vaishu@gmail.com'),
    (10, 'Kavya', 42000, 'kavya@gmail.com');
SELECT * FROM emp_test;

-- Try inserting duplicate email addresses.
INSERT INTO emp_test (emp_id, emp_name, salary, email)
VALUES (8, 'Venky', 45000, 'vaishu@gmail.com'); -- Shows the error as duplicate email cannot be used