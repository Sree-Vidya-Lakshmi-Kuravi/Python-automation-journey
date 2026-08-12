ALTER TABLE emp_test ADD 
    email VARCHAR(40) NOT NULL;

SELECT * FROM emp_test;

-- Insert an employee with an email.
UPDATE emp_test
SET email = 'rohit45@gmail.com' WHERE emp_id = 1;
SELECT * FROM emp_test;

-- Try inserting an employee without an email.
INSERT INTO emp_test (emp_id, emp_name, salary, email)
    VALUES (5, 'Chandana', 42000, NULL); -- It shows the error as emp_id can be NULL