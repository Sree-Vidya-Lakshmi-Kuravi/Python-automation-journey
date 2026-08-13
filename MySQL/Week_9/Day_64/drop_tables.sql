-- Drop child / junction tables first
DROP TABLE IF EXISTS employee_projects;
DROP TABLE IF EXISTS employees;

-- Then drop parent tables
DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS departments;

DROP TABLE IF EXISTS departments_sandbox;