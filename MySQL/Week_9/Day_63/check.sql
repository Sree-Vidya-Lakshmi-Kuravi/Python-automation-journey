ALTER TABLE emp_test
MODIFY salary DECIMAL(10,2) CHECK (salary>0);

-- Insert a valid salary.
SELECT * FROM emp_test;
INSERT INTO emp_test (emp_id, emp_name, salary, email) VALUES (13, 'Mahi', 90000, 'mahi@gmail.com');
SELECT * FROM emp_test;

-- Try inserting salary 0.
INSERT INTO emp_test (emp_id, emp_name, salary, email) VALUES (17, 'Loki', 0, 'loki@gmail.com'); -- Throws an error because it violates the constraint salary > 0

-- Try inserting salary < 0.
INSERT INTO emp_test (emp_id, emp_name, salary, email) VALUES (19, 'Srinivasa', -3, 'srini@gmail.com'); -- Throws an error because it violates the constraint salary > 0