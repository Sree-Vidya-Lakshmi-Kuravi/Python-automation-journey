CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    holder_name VARCHAR(50),
    balance DECIMAL(10, 2) CHECK (balance >= 0)
);

INSERT INTO accounts (account_id, holder_name, balance) VALUES
(1, 'Ramesh Babu', 25000.50),
(2, 'Sravani Devi', 18000.00),
(3, 'Venkatesh Rao', 32000.75),
(4, 'Lakshmi Priya', 45000.00),
(5, 'Anil Kumar', 15000.25),
(6, 'Harika Reddy', 27500.00),
(7, 'Chaitanya Varma', 60000.10),
(8, 'Padmaja N', 22000.00),
(9, 'Suresh Yadav', 51000.80),
(10, 'Bhavana K', 34000.00);

SELECT * FROM accounts;
DROP TABLE accounts;