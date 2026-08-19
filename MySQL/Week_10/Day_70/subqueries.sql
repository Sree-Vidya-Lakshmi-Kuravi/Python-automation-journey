-- 16. Find employees earning more than the company average salary.
SELECT *
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- 17. Find employees earning more than their department average.
SELECT e1.*
FROM employees e1
WHERE e1.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.department_id = e1.department_id);

-- 18. Find the second-highest salary.
SELECT MAX(salary) AS second_highest_salary
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- 19. Find departments having at least one employee earning above ₹90,000.
SELECT *
FROM departments
WHERE department_id IN (
    SELECT DISTINCT department_id
    FROM employees
    WHERE salary > 90000);

-- 20. Find employees who aren't assigned to any project.
SELECT *
FROM employees
WHERE employee_id NOT IN (
    SELECT employee_id 
    FROM employee_projects);