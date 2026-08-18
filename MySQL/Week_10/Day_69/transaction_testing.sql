-- Employee Creation
-- Create employee -> Create project assignment -> Both succeed -> COMMIT
--  Employee creation should be rolled back if the operation is designed as one atomic transaction.

START TRANSACTION;
CREATE TABLE project_assign (emp_id INT, project_id INT);
INSERT INTO accounts (account_id, holder_name) VALUES (30, 'Mahi');
INSERT INTO project_assign (emp_id, project_id) VALUES (30, 501);
COMMIT;
ROLLBACK;