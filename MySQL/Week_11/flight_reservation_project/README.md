# ✈️ Flight Reservation Database Automation

## 📌 Overview

A Python-based **database automation testing framework** for a flight reservation system.

The project uses **Python, PyTest, MySQL, and SQL** to validate database functionality, business rules, data integrity, and transaction behavior.

---

## 🛠️ Technologies

* Python
* MySQL
* SQL
* PyTest
* mysql-connector-python
* pytest-html
* python-dotenv
* Git & GitHub

---

## 🏗️ Project Structure

flight-reservation-db-automation/
│
├── config/
│   └── db_config.py
├── database/
│   ├── schema.sql
│   └── test_data.sql
├── utils/
│   ├── db_utils.py
│   └── db_assertions.py
├── test_data/
│   └── booking_data.py
├── tests/
│   ├── test_connection.py
│   ├── test_customers.py
│   ├── test_flights.py
│   ├── test_seats.py
│   ├── test_bookings.py
│   ├── test_payments.py
│   ├── test_cancellations.py
│   ├── test_transactions.py
│   ├── test_data_integrity.py
│   └── test_advanced_sql.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## 🗄️ Database

The database contains 10 related tables:

```text
Airlines
Airports
Aircrafts
Customers
Flights
Flight Seats
Bookings
Passengers
Payments
Refunds
```

The main relationships are:

```text
Airline → Flight → Seat
Customer → Booking → Payment → Refund
Booking → Passenger
Flight → Booking
```

---

## 🧪 What Is Tested?

### Flight & Airport

* Flight and airport validation
* Unique flight/airport codes
* Foreign-key relationships
* Flight data validation

### Seats

* Seat availability
* Seat reservation
* Seat release
* Duplicate seats
* Seat-to-flight consistency

### Bookings

* Booking creation
* Booking status
* Booking references
* Customer/flight/seat relationships
* Double-booking validation

### Payments

* Payment creation
* Payment status
* Payment amount validation
* Booking/payment consistency
* Failed payments

### Cancellation & Refund

* Booking cancellation
* Seat release
* Refund creation
* Refund validation
* Refund/payment consistency

### Transactions

* COMMIT
* ROLLBACK
* SAVEPOINT
* Successful and failed transaction scenarios

### Advanced SQL

* JOINs
* Subqueries
* EXISTS / NOT EXISTS
* CTEs
* CASE
* Aggregations
* Window functions

---

## ⚙️ Framework Features

* PyTest fixtures
* Parameterized tests
* Smoke, sanity and regression markers
* Reusable database utilities
* Assertions
* Exception handling
* Logging
* HTML reports
* Test cleanup and isolation
* Environment-based configuration

---

## 🚨 Negative Testing

The framework also validates invalid scenarios such as:

* Duplicate records
* Invalid foreign keys
* Negative amounts
* Duplicate seats
* Double booking
* Invalid payment/booking combinations
* Invalid refunds

---

## ▶️ Setup

### 1. Clone the repository

git clone <repository-url>
cd flight-reservation-db-automation

### 2. Create a virtual environment

python -m venv .venv

Activate the environment and install dependencies:

pip install -r requirements.txt

### 3. Configure the database

Create the MySQL database using:

database/schema.sql

Insert test data using:

database/test_data.sql


Configure your database credentials in `.env`.

---

## ▶️ Run Tests

Run all tests:

pytest -v

Run smoke tests:

pytest -m smoke -v

Run sanity tests:

pytest -m sanity -v

Run regression tests:

pytest -m regression -v

Generate an HTML report:

pytest -v --html=reports/test_report.html


---

## 📊 Reporting

Test execution results are available through **PyTest HTML reports**.

Logs are generated to help with debugging and failure analysis.

---

## 🎯 Key Learning

This project demonstrates practical experience in:

* Python database automation
* SQL testing
* MySQL
* PyTest
* Database validation
* Transaction testing
* Negative testing
* Test data management
* Logging and reporting
* Automation framework development

---

## 📌 Project Status

**Completed ✅**

Built as a portfolio project to demonstrate **Python QA Automation and Database Testing** skills.

---
