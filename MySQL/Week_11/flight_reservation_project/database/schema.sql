-- Active: 1787849158880@@127.0.0.1@3306@flight_reservation
CREATE DATABASE flight_reservation;
USE flight_reservation;
SELECT DATABASE();

-- Table 1
CREATE TABLE IF NOT EXISTS airlines (
    airline_id INT PRIMARY KEY,
    airline_name VARCHAR(50) NOT NULL,
    airline_code VARCHAR(40) UNIQUE NOT NULL);

-- Table 2
CREATE TABLE IF NOT EXISTS airports (
    airport_id INT PRIMARY KEY,
    airport_code VARCHAR(40) UNIQUE NOT NULL,
    airport_name VARCHAR(50) NOT NULL,
    city VARCHAR(40),
    country VARCHAR(40));

-- Table 3
CREATE TABLE IF NOT EXISTS aircrafts (
    aircraft_id INT PRIMARY KEY,
    airline_id INT,
    model VARCHAR(40) NOT NULL,
    total_seats INT CHECK (total_seats > 0),
    FOREIGN KEY (airline_id) REFERENCES airlines(airline_id));

-- Table 4
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    first_name VARCHAR(40) NOT NULL,
    last_name VARCHAR(40) NOT NULL,
    email VARCHAR(40) UNIQUE NOT NULL,
    phone VARCHAR(10) NOT NULL,
    date_of_birth DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

-- Table 5
CREATE TABLE flights (
    flight_id INT PRIMARY KEY,
    flight_number VARCHAR(20) UNIQUE NOT NULL,
    airline_id INT NOT NULL,
    aircraft_id INT NOT NULL,
    origin_airport_id INT NOT NULL,
    destination_airport_id INT NOT NULL,
    departure_time TIMESTAMP NOT NULL,
    arrival_time TIMESTAMP NOT NULL,
    base_fare DECIMAL(10,2) CHECK (base_fare > 0),
    status VARCHAR(20) NOT NULL CHECK (status IN ('SCHEDULED','BOARDING','COMPLETED','CANCELLED')),
    FOREIGN KEY (airline_id) REFERENCES airlines(airline_id),
    FOREIGN KEY (aircraft_id) REFERENCES aircrafts(aircraft_id),
    FOREIGN KEY (origin_airport_id) REFERENCES airports(airport_id),
    FOREIGN KEY (destination_airport_id) REFERENCES airports(airport_id));

-- Table 6
CREATE TABLE flight_seats (
    seat_id INT PRIMARY KEY,
    flight_id INT NOT NULL,
    seat_number VARCHAR(20) NOT NULL,
    seat_class VARCHAR(40) NOT NULL CHECK (seat_class IN ('ECONOMY', 'PREMIUM_ECONOMY', 'BUSINESS')),
    seat_status VARCHAR(40) NOT NULL CHECK (seat_status IN ('AVAILABLE', 'HELD', 'BOOKED')),
    FOREIGN KEY (flight_id) REFERENCES flights (flight_id),
    CONSTRAINT unique_flight_seat UNIQUE (flight_id, seat_number));

-- Table 7
CREATE TABLE bookings (
    booking_id INT PRIMARY KEY,
    booking_reference VARCHAR(20) UNIQUE NOT NULL,
    customer_id INT NOT NULL,
    flight_id INT NOT NULL,
    seat_id INT NOT NULL,
    booking_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    booking_status VARCHAR(20) NOT NULL CHECK (booking_status IN ('PENDING','CONFIRMED','CANCELLED')),
    total_amount DECIMAL(10,2) CHECK (total_amount > 0),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (flight_id) REFERENCES flights(flight_id),
    FOREIGN KEY (seat_id) REFERENCES flight_seats(seat_id));

-- Table 8
CREATE TABLE passengers (
    passenger_id INT PRIMARY KEY,
    booking_id INT NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    passport_number VARCHAR(20) UNIQUE NOT NULL,
    date_of_birth DATE NOT NULL,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id));

-- Table 9
CREATE TABLE payments (
    payment_id INT PRIMARY KEY,
    booking_id INT NOT NULL,
    transaction_reference VARCHAR(30) UNIQUE NOT NULL,
    amount DECIMAL(10,2) CHECK (amount > 0),
    payment_method VARCHAR(20) NOT NULL CHECK (payment_method IN ('CARD','UPI','NET_BANKING','WALLET')),
    payment_status VARCHAR(20) NOT NULL CHECK (payment_status IN ('INITIATED','SUCCESS','FAILED')),
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES bookings(booking_id));

-- Table 10
CREATE TABLE refunds (
    refund_id INT PRIMARY KEY,
    payment_id INT NOT NULL,
    refund_reference VARCHAR(30) UNIQUE NOT NULL,
    refund_amount DECIMAL(10,2) CHECK (refund_amount > 0),
    refund_status VARCHAR(20) NOT NULL CHECK (refund_status IN ('INITIATED','PROCESSED','FAILED')),
    refund_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (payment_id) REFERENCES payments(payment_id));