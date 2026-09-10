# ✈️ Flight Reservation Database Automation Framework

A Python + MySQL + PyTest based database automation framework for validating a flight reservation system.

The project simulates database-level testing for a fictional airline, **SkyRoute Airlines**, and focuses on data integrity, relationships, constraints, business rules, CRUD operations, state transitions, transactions, and booking workflows.

---

## 📌 Project Objective

The objective of this project is to build a maintainable database automation framework that can:

* Connect Python automation code to MySQL
* Execute and validate SQL queries using PyTest
* Validate database structure and test data
* Verify primary-key and foreign-key relationships
* Validate database constraints
* Perform CRUD operations
* Validate business rules
* Automate seat availability and reservation workflows
* Automate booking creation and confirmation
* Validate passenger-booking relationships
* Prevent invalid and duplicate bookings
* Validate database state transitions
* Test transaction rollback behavior
* Generate automated test reports
* Maintain logs for test execution

This project is designed as a practical **QA Automation / SDET database testing project**.

---

# 🛠️ Technologies Used

| Technology             | Purpose                          |
| ---------------------- | -------------------------------- |
| Python                 | Automation programming           |
| MySQL                  | Relational database              |
| mysql-connector-python | Python–MySQL connectivity        |
| PyTest                 | Test automation framework        |
| pytest-html            | HTML test reports                |
| SQL                    | Database querying and validation |
| Git                    | Version control                  |
| GitHub                 | Source code management           |

---


# 📊 Database Tables

## 1. Airlines

Stores airline information.

Important fields:

* `airline_id`
* `airline_name`
* `airline_code`

Constraints:

* Primary Key
* NOT NULL
* UNIQUE airline code

---

## 2. Airports

Stores airport information.

Important fields:

* `airport_id`
* `airport_code`
* `airport_name`
* `city`
* `country`

Example airport codes:

HYD
BLR
DEL
BOM
MAA
CCU


Constraints:

* Primary Key
* UNIQUE airport code
* Required fields

---

## 3. Aircrafts

Stores aircraft information.

Important fields:

* `aircraft_id`
* `airline_id`
* `model`
* `total_seats`

Relationships:

aircrafts.airline_id
        ↓
airlines.airline_id

Constraints:

* Primary Key
* Foreign Key
* NOT NULL
* CHECK total seats > 0

---

## 4. Customers

Stores customer information.

Important fields:

* `customer_id`
* `first_name`
* `last_name`
* `email`
* `phone`
* `date_of_birth`
* `created_at`

Constraints:

* Primary Key
* NOT NULL
* UNIQUE email
* DEFAULT timestamp

---

## 5. Flights

Stores flight information.

Important fields:

* `flight_id`
* `flight_number`
* `airline_id`
* `aircraft_id`
* `origin_airport_id`
* `destination_airport_id`
* `departure_time`
* `arrival_time`
* `base_fare`
* `status`

Flight statuses:

SCHEDULED
BOARDING
COMPLETED
CANCELLED


Relationships:

flights
 ├── airline
 ├── aircraft
 ├── origin airport
 └── destination airport

Business rules include:

* Flight number must be unique
* Origin and destination must be different
* Arrival must be after departure
* Fare must be positive
* Flight status must be valid

---

## 6. Flight Seats

Stores seat information for individual flights.

Important fields:

* `seat_id`
* `flight_id`
* `seat_number`
* `seat_class`
* `seat_status`

Seat classes:

ECONOMY
PREMIUM_ECONOMY
BUSINESS


Seat statuses:

AVAILABLE
HELD
BOOKED


Composite uniqueness:

(flight_id, seat_number)

This ensures that the same seat number cannot exist twice for the same flight.

---

## 7. Bookings

Stores customer flight bookings.

Important fields:

* `booking_id`
* `booking_reference`
* `customer_id`
* `flight_id`
* `seat_id`
* `booking_date`
* `booking_status`
* `total_amount`

Booking statuses:

PENDING
CONFIRMED
CANCELLED

Relationships:

Customer
   ↓
Booking
   ├── Flight
   └── Seat

---

## 8. Passengers

Stores passenger information associated with bookings.

Important fields:

* `passenger_id`
* `booking_id`
* `first_name`
* `last_name`
* `passport_number`
* `date_of_birth`

Constraints:

* Primary Key
* Foreign Key
* Required passenger names
* UNIQUE passport number

---

## 9. Payments

Stores payment information for bookings.

Important fields:

* `payment_id`
* `booking_id`
* `transaction_reference`
* `amount`
* `payment_method`
* `payment_status`
* `payment_date`

Payment methods:

CARD
UPI
NET_BANKING
WALLET


Payment statuses:

INITIATED
SUCCESS
FAILED

---

## 10. Refunds

Stores refund information associated with payments.

Important fields:

* `refund_id`
* `payment_id`
* `refund_reference`
* `refund_amount`
* `refund_status`
* `refund_date`

Refund statuses:

INITIATED
PROCESSED
FAILED

---

# 🔌 Database Utilities

`utils/db_utils.py` provides reusable database operations.

Current capabilities include:

* Establishing MySQL connections
* Executing SELECT queries
* Executing INSERT queries
* Executing UPDATE queries
* Executing DELETE queries
* Parameterized SQL execution
* Fetching query results
* Commit
* Rollback
* Exception handling
* Connection cleanup

---


# ✅ Testing Covered So Far

## Database Foundation

* Database connection
* Database selection
* Table existence
* Initial test-data validation
* Customer count validation
* Flight count validation

---

## Airlines

* Airline count
* Airline code uniqueness
* Required-field validation
* Duplicate airline code
* Airline lookup

---

## Airports

* Airport count
* Airport code uniqueness
* Required-field validation
* Duplicate airport code
* Airport lookup
* Airport relationship validation

---

## Aircrafts

* Aircraft count
* Aircraft → airline relationship
* Positive seat capacity
* Invalid airline foreign key
* Required aircraft model

---

## Flights

* Flight count
* Flight number uniqueness
* Airline foreign-key validation
* Aircraft foreign-key validation
* Origin airport validation
* Destination airport validation
* Flight status validation
* Positive fare validation
* Origin ≠ destination
* Arrival > departure
* Multi-table flight JOIN validation

---

## CRUD Testing

CRUD operations have been implemented and validated using Python + MySQL:
CREATE
  ↓
READ
  ↓
UPDATE
  ↓
READ
  ↓
DELETE
  ↓
VERIFY

Test data is restored or cleaned up after state-changing tests.

---

# ✈️ Seat Automation

Seat-level automation covers:

### Seat availability

Flight
   ↓
Available Seats
   ↓
Retrieve seat information

### Seat reservation

AVAILABLE
    ↓
HELD

### Seat booking

HELD
    ↓
BOOKED

### Seat release

HELD
    ↓
AVAILABLE

### Additional validation

* Seat → flight foreign key
* Duplicate seat number
* Seat class validation
* Seat status validation
* Unavailable seat protection
* BOOKED seat protection
* Invalid flight validation
* Composite uniqueness
* Seat distribution
* Transaction rollback

---

# 🎫 Booking Automation

The booking automation covers:

Customer
   ↓
Select Flight
   ↓
Find AVAILABLE Seat
   ↓
Create Booking
   ↓
Create Passenger
   ↓
Book Seat
   ↓
Confirm Booking

---

## Booking Validations

Implemented validations include:

* Booking existence
* Booking reference uniqueness
* Customer relationship
* Flight relationship
* Seat relationship
* Booking/flight/seat consistency
* Booking status validation
* Positive booking amount
* Passenger → booking relationship
* Passport uniqueness
* Invalid customer foreign key
* Invalid seat foreign key
* Negative booking amount

---

# 🚫 Double-Booking Prevention

The framework validates that an unavailable seat cannot be booked again.
This prevents multiple bookings from incorrectly using the same seat.

---

# 🔄 Booking Consistency Validation

The framework validates that:

Booking Flight
      =
Seat Flight

An invalid combination such as:

Booking → Flight A
Seat    → Flight B

must be rejected by business-rule validation.

---

# 👤 Passenger Validation

Passenger automation validates:

* Passenger existence
* Booking relationship
* Required names
* Passport uniqueness
* Passenger creation
* Passenger → booking consistency

---

# 💾 Transaction Testing

Transactions are used for state-changing workflows.

Example:

BEGIN
  ↓
Create Booking
  ↓
Reserve Seat
  ↓
Create Passenger
  ↓
Failure
  ↓
ROLLBACK
  ↓
Verify Database Restored

After rollback, the framework verifies that:

Booking does not exist
Passenger does not exist
Seat is AVAILABLE

This validates database transaction integrity.

---

# 🛡️ Negative Testing

The framework deliberately tests invalid operations such as:

* Duplicate airline code
* Duplicate airport code
* Duplicate seat
* Invalid foreign key
* Negative fare
* Negative booking amount
* Invalid customer
* Invalid seat
* Invalid flight/seat combination
* Double booking
* Invalid status values

Expected database exceptions such as `IntegrityError` are explicitly handled using PyTest.

Unexpected exceptions are allowed to fail the test.

---

# 🧹 Test Data Cleanup

State-changing tests restore the database to its original state wherever appropriate.

Typical workflow:
Original State
      ↓
Test Modification
      ↓
Verification
      ↓
Cleanup / Rollback
      ↓
Original State

This prevents tests from affecting subsequent tests.

---


# 📚 SQL Concepts Applied

The project currently applies:

* SELECT
* WHERE
* ORDER BY
* DISTINCT
* LIMIT
* LIKE
* IN
* BETWEEN
* NULL handling
* Aggregate functions
* GROUP BY
* HAVING
* INNER JOIN
* LEFT JOIN
* Multi-table JOINs
* Subqueries
* EXISTS
* UNION
* Views
* SQL functions
* CASE
* COALESCE
* Window functions
* Transactions
* COMMIT
* ROLLBACK
* SAVEPOINT
* Constraints
* Foreign keys
* Composite keys
* Normalization
* Parameterized queries

---

# 🎯 Learning Outcomes

After completing this project, the automation engineer should be able to:

* Connect Python automation frameworks to MySQL
* Write database validation tests using PyTest
* Execute parameterized SQL queries
* Validate relational database integrity
* Test primary and foreign-key constraints
* Automate CRUD operations
* Validate complex JOINs
* Test business rules
* Automate database state transitions
* Test booking workflows
* Validate transactions and rollback
* Perform negative database testing
* Build reusable database utilities
* Generate automated reports
* Implement logging
* Organize a maintainable database automation framework

---

# 👨‍💻 Project Status

**Current Progress: Day 76 completed**

The framework currently covers:

```text
Database
   ↓
Python Connectivity
   ↓
PyTest Framework
   ↓
Core Database Validation
   ↓
Flight Infrastructure
   ↓
Seat Management
   ↓
Booking Management
   ↓
Passenger Validation
   ↓
Transaction Testing
```

**Next milestone: Payment Automation**
