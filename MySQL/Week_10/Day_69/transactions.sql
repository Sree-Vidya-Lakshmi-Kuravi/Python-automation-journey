-- 1. Start a transaction and insert an employee.
    -- Verify the record exists.
    -- Then:
    -- ROLLBACK;
    -- Verify that the employee disappeared.

SET autocommit = 0;
SELECT * FROM accounts;
INSERT INTO accounts (account_id, holder_name, balance) VALUES (11, 'Odinson', 28000);
SELECT * FROM accounts WHERE account_id = 11;
ROLLBACK;
SELECT * FROM accounts WHERE account_id = 11;

-- 2. Insert an employee and:
-- COMMIT;
-- Verify that the record remains after the transaction.
INSERT INTO accounts (account_id, holder_name, balance) VALUES (11, 'Odinson', 28000);
SELECT * FROM accounts;
COMMIT;
SELECT * FROM accounts;

-- 3. Perform multiple operations and use:
-- SAVEPOINT sp1;
-- Then:
-- ROLLBACK TO SAVEPOINT sp1;
-- Observe which changes remain.

BEGIN;
INSERT INTO accounts (account_id, holder_name, balance)
VALUES (18, 'Madhavi Latha', 30000.00);
INSERT INTO accounts (account_id, holder_name, balance)
VALUES (19, 'Prasad Reddy', 45000.00);
SELECT * FROM accounts;
SAVEPOINT sp1;
INSERT INTO accounts (account_id, holder_name, balance)
VALUES (22, 'Rajeshwari Devi', 22000.00);
UPDATE accounts
SET balance = balance + 5000
WHERE account_id = 12;
ROLLBACK TO SAVEPOINT sp1;