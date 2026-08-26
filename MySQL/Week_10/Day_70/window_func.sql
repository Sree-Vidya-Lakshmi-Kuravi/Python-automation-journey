-- Assign a row number to employees ordered by salary.
SELECT *, ROW_NUMBER() OVER (ORDER BY salary) AS row_num FROM employees;

-- Rank employees by salary within each department.
SELECT *, RANK() OVER (PARTITION BY department_id ORDER BY salary) AS rank_sal FROM employees;

-- Display each employee's department average salary beside their individual salary.
SELECT employee_id, first_name, department_id, salary,
    AVG(salary) OVER (PARTITION BY department_id) AS dept_avg_salary FROM employees;

-- Display the previous employee's salary using `LAG()`.
SELECT salary, LAG(salary) OVER (ORDER BY salary) AS prev_sal FROM employees;

-- Calculate the difference between current and previous salary.
SELECT employee_id, first_name, salary, salary - LAG(salary, 1) OVER (ORDER BY salary) AS salary_diff FROM employees;