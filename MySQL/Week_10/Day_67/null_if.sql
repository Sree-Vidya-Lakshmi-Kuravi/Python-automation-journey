-- Convert experience 0 into NULL.
SELECT NULLIF(experience_years, 0) FROM emp; -- Returns NULL if both values inside NULLIF() are equal else returns the first value. So, it returns the experience_years of all the employees

-- Prevent division-by-zero using NULLIF().
SELECT eid, fname, lname, salary,experience_years, ROUND(salary / NULLIF(experience_years, 0), 2) AS salary_per_year
FROM emp; -- NULLIF(experience_years, 0) returns NULL if experience_years = 0. This prevents dividing by zero. If experience_years is zero, the result of the division will be NULL instead of throwing an error.