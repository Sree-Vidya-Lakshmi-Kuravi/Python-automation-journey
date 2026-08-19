-- 21. Create a salary category:
    -- >= 80000 → High
    -- 50000–79999 → Medium
    -- < 50000 → Low
SELECT *, 
    CASE 
        WHEN salary >= 80000 THEN 'High'
        WHEN salary BETWEEN 50000 AND 79999 THEN 'Medium'  
        ELSE 'Low'
    END AS salary_category
FROM employees;

-- 22. Display each employee's joining year.
SELECT 
    employee_id,
    first_name,
    YEAR(joining_date) AS joining_year
FROM employees;

-- 23. Replace NULL city values with `Unknown`.
SELECT 
    employee_id,
    first_name,
    COALESCE(city, 'Unknown') AS city
FROM employees;

-- 24. Find the top 3 employees in each department using a window function.
WITH RankedEmployees AS (
    SELECT 
        e.*,
        DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) as dept_rank
    FROM employees e
)
SELECT *
FROM RankedEmployees
WHERE dept_rank <= 3;

-- 25. Find the second-highest salary in each department.
WITH RankedSalaries AS (
    SELECT e.*,
        DENSE_RANK() OVER (PARTITION BY department_id ORDER BY salary DESC) as rank_pos
    FROM employees e
)
SELECT *
FROM RankedSalaries
WHERE rank_pos = 2;