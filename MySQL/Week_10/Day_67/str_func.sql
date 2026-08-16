CREATE TABLE emp (
    eid INT, fname VARCHAR(35), lname VARCHAR(35), email VARCHAR(45), dept VARCHAR(20), city VARCHAR(20));

INSERT INTO emp (eid, fname, lname, email, dept, city) VALUES
(1, 'Allu', 'Arjun', 'allu.arjun@cinema.com', 'Acting', 'Hyderabad'),
(2, 'Nayanthara', 'Kurian', 'nayan.kurian@cinema.com', 'Acting', 'Chennai'),
(3, 'Anirudh', 'Ravichander', 'anirudh.r@music.com', 'Music', 'Chennai'),
(4, 'Keerthy', 'Suresh', 'keerthy.s@cinema.com', 'Acting', 'Chennai'),
(5, 'Devi', 'Sri Prasad', 'dsp@music.com', 'Music', 'Hyderabad'),
(6, 'Mahesh', 'Babu', 'mahesh.b@cinema.com', 'Acting', 'Hyderabad'),
(7, 'Samantha', 'Ruth Prabhu', 'samantha.rp@cinema.com', 'Acting', 'Chennai'),
(8, 'Ilaiyaraaja', '', 'ilaiyaraaja@music.com', 'Music', 'Chennai'),
(9, 'Ram', 'Charan', 'ram.charan@cinema.com', 'Acting', 'Hyderabad'),
(10, 'A.R.', 'Rahman', 'ar.rahman@music.com', 'Music', 'Chennai');

SELECT * FROM emp;

-- Display employees' full names by combining first and last names.
SELECT eid, CONCAT(fname, ' ', lname) AS full_name FROM emp;

-- Display all employee names in uppercase.
SELECT UPPER(fname), UPPER(lname) FROM emp;

-- Display all employee emails in lowercase.
SELECT LOWER(email) FROM emp;

-- Display each employee's name and the number of characters in their first name.
SELECT fname, LENGTH(fname) AS num_char FROM emp;

-- Find employees whose first name contains more than 5 characters.
SELECT fname FROM emp WHERE LENGTH(fname) > 5;

-- Extract the first 3 characters of every employee's first name.
-- SUBSTRING(string, start_position, length)
-- Note: SQL index numbering starts at 1, NOT 0!
SELECT fname, SUBSTRING(fname, 1, 3) FROM emp;

-- Extract the first 5 characters of every employee's email.
SELECT email, SUBSTRING(email, 1, 5) FROM emp;

-- Replace a particular domain in employee emails with another domain.
SELECT email, REPLACE(email, 'cinema.com', 'movie.com') FROM emp;

-- Remove leading/trailing spaces from employee city names.
SELECT city, TRIM(city) FROM emp;

-- Display a formatted employee string such as:
-- Employee: Rahul Sharma | Department: QA | City: Hyderabad
SELECT CONCAT('Employee: ', fname, 
              ' | Department: ', dept,
              ' | City: ', city) AS emp_details 
FROM emp;