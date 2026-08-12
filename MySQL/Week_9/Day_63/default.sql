ALTER TABLE emp_test
ADD status VARCHAR(35) DEFAULT 'Active';

-- Insert an employee without specifying status.
INSERT INTO emp_test (emp_id, emp_name, salary, email)
    VALUES (5, 'Vijay', 41000, 'vijjulu@gmail.com');
INSERT INTO emp_test (emp_id, emp_name, salary, email)
    VALUES (7, 'Kanna', 31000, 'kanna@gmail.com');
SELECT * FROM emp_test;

-- Verify the default value.
SELECT status FROM emp_test;

-- Insert an employee with an explicit status.
INSERT INTO emp_test (emp_id, emp_name, salary, email, status)
    VALUES (11, 'Jon Snow', 8000, 'jon@gmail.com', 'Inactive');
SELECT * FROM emp_test;