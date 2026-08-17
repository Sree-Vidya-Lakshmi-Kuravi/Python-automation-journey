-- Display every employee along with the company's total salary.
SELECT eid, fname, lname, salary,
    SUM(salary) OVER() AS company_total_salary
FROM emp;

-- Display every employee along with the average company salary.
SELECT eid, fname, lname, salary,
    ROUND(AVG(salary) OVER(), 2) AS company_avg_salary
FROM emp;

-- Display every employee along with the average salary of their department.
SELECT eid, fname, lname, salary, dept,
    AVG(salary) OVER(PARTITION BY dept) AS dept_avg_salary
FROM emp;

-- Display every employee along with the total salary of their department.
SELECT eid, fname, lname, salary, dept,
    SUM(salary) OVER(PARTITION BY dept) AS dept_total_salary
FROM emp;

-- Display the employee count of their department beside every employee.
SELECT eid, fname, lname, salary, dept,
    COUNT(*) OVER (PARTITION BY dept) AS emp_count
FROM emp;

-- Display the maximum salary in each employee's department.
SELECT eid, fname, lname, salary, dept,
    MAX(salary) OVER (PARTITION BY dept) AS emp_max_sal
FROM emp;