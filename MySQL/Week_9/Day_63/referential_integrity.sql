-- Referential Integrity
-- Guarantees that every child record is linked correctly with its parent records.
-- Prevents the orphan data

-- Try deleting a department that has employees.
DELETE FROM depts_test WHERE dept_id = 101; -- Throws the error because the database safeguards your data by preventing accidental deletion of parent records that still have child dependencies.

-- RESTRICT - Throws the error if child exists and blocks the operation.
-- SET NULL - Leaves the child rows as it is and updates the foreign key as NULL.
-- CASCADE - Automatically deletes or updates all matching child records.