CREATE TABLE employee_projects (
    employee_id INT,
    project_id INT,
    assigned_date DATE,
    PRIMARY KEY (employee_id, project_id));

-- Insert a unique employee-project combination
INSERT INTO employee_projects (employee_id, project_id, assigned_date)
VALUES (101, 201, '2026-08-13');

SELECT * FROM employee_projects;

-- Try inserting the exact same combination again
INSERT INTO employee_projects (employee_id, project_id, assigned_date)
VALUES (101, 201, '2026-08-13'); -- Duplicate employee_id, project_id are not allowed since it is primary key

-- Insert the same employee with a different project
INSERT INTO employee_projects (employee_id, project_id, assigned_date)
VALUES (101, 202, '2026-08-13');