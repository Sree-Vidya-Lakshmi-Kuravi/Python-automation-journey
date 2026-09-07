-- =========================
-- Airlines
-- =========================
INSERT INTO airlines (airline_id, airline_name, airline_code) VALUES
(1, 'Delta Air Lines', 'DL'),
(2, 'Emirates', 'EK'),
(3, 'Singapore Airlines', 'SQ');
SELECT * FROM airlines;

-- =========================
-- Airports
-- =========================
INSERT INTO airports (airport_id, airport_code, airport_name, city, country) VALUES
(1, 'HYD', 'Rajiv Gandhi International Airport', 'Hyderabad', 'India'),
(2, 'BLR', 'Kempegowda International Airport', 'Bengaluru', 'India'),
(3, 'DEL', 'Indira Gandhi International Airport', 'New Delhi', 'India'),
(4, 'BOM', 'Chhatrapati Shivaji Maharaj International Airport', 'Mumbai', 'India'),
(5, 'MAA', 'Chennai International Airport', 'Chennai', 'India'),
(6, 'CCU', 'Netaji Subhas Chandra Bose International Airport', 'Kolkata', 'India');
SELECT * FROM airports;


-- =========================
-- Aircrafts
-- =========================
INSERT INTO aircrafts (aircraft_id, airline_id, model, total_seats) VALUES
(1, 1, 'Boeing 737-800', 160),
(2, 1, 'Airbus A321', 190),
(3, 2, 'Airbus A380', 489),
(4, 2, 'Boeing 777-300ER', 354),
(5, 3, 'Airbus A350-900', 325);
SELECT * FROM aircrafts;

-- =========================
-- Customers
-- =========================
INSERT INTO customers (customer_id, first_name, last_name, email, phone, date_of_birth) VALUES
(1, 'Amit', 'Sharma', 'amit.sharma@example.com', '9876543210', '1985-03-12'),
(2, 'Priya', 'Reddy', 'priya.reddy@example.com', '9123456780', '1990-07-25'),
(3, 'Rahul', 'Mehta', 'rahul.mehta@example.com', '9988776655', '1988-11-05'),
(4, 'Sneha', 'Patel', 'sneha.patel@example.com', '9765432109', '1992-01-18'),
(5, 'Vikram', 'Singh', 'vikram.singh@example.com', '9345678901', '1983-09-30'),
(6, 'Ananya', 'Nair', 'ananya.nair@example.com', '9456123789', '1995-04-14'),
(7, 'Karan', 'Kapoor', 'karan.kapoor@example.com', '9567890123', '1987-06-22'),
(8, 'Meera', 'Iyer', 'meera.iyer@example.com', '9234567890', '1993-12-09'),
(9, 'Arjun', 'Desai', 'arjun.desai@example.com', '9789012345', '1989-02-27'),
(10, 'Neha', 'Gupta', 'neha.gupta@example.com', '9654321098', '1991-08-16');
SELECT * FROM customers;

-- =========================
-- Flights (10 varied flights)
-- =========================
INSERT INTO flights (flight_id, flight_number, airline_id, aircraft_id, origin_airport_id, destination_airport_id, departure_time, arrival_time, base_fare, status) VALUES
(1, 'DL101', 1, 1, 3, 4, '2026-09-10 08:00:00', '2026-09-10 10:30:00', 250.00, 'SCHEDULED'),
(2, 'EK202', 2, 3, 4, 3, '2026-09-11 14:00:00', '2026-09-11 16:45:00', 450.00, 'BOARDING'),
(3, 'SQ303', 3, 5, 5, 6, '2026-09-12 09:15:00', '2026-09-12 11:50:00', 320.00, 'SCHEDULED'),
(4, 'DL404', 1, 2, 6, 1, '2026-09-13 07:00:00', '2026-09-13 09:30:00', 280.00, 'COMPLETED'),
(5, 'EK505', 2, 4, 2, 5, '2026-09-14 18:00:00', '2026-09-14 20:40:00', 390.00, 'CANCELLED'),
(6, 'SQ606', 3, 5, 1, 2, '2026-09-15 06:30:00', '2026-09-15 08:00:00', 210.00, 'SCHEDULED'),
(7, 'DL707', 1, 1, 2, 3, '2026-09-16 12:00:00', '2026-09-16 14:15:00', 260.00, 'BOARDING'),
(8, 'EK808', 2, 4, 5, 4, '2026-09-17 09:45:00', '2026-09-17 12:30:00', 410.00, 'SCHEDULED'),
(9, 'SQ909', 3, 5, 6, 3, '2026-09-18 15:00:00', '2026-09-18 17:30:00', 330.00, 'CANCELLED'),
(10, 'DL010', 1, 2, 4, 6, '2026-09-19 20:00:00', '2026-09-19 22:45:00', 295.00, 'SCHEDULED');
SELECT * FROM flights;

-- =========================
-- Flight Seats (10–20 seats across flights)
-- =========================
INSERT INTO flight_seats (seat_id, flight_id, seat_number, seat_class, seat_status) VALUES
(1, 1, '12A', 'ECONOMY', 'AVAILABLE'),
(2, 1, '12B', 'ECONOMY', 'BOOKED'),
(3, 1, '14C', 'PREMIUM_ECONOMY', 'AVAILABLE'),
(4, 2, '1A', 'BUSINESS', 'HELD'),
(5, 2, '1B', 'BUSINESS', 'BOOKED'),
(6, 2, '20C', 'ECONOMY', 'AVAILABLE'),
(7, 3, '5D', 'PREMIUM_ECONOMY', 'AVAILABLE'),
(8, 3, '6A', 'ECONOMY', 'BOOKED'),
(9, 4, '2A', 'BUSINESS', 'AVAILABLE'),
(10, 5, '15F', 'ECONOMY', 'AVAILABLE'),
(11, 6, '10A', 'ECONOMY', 'AVAILABLE'),
(12, 6, '10B', 'ECONOMY', 'BOOKED'),
(13, 7, '3C', 'BUSINESS', 'AVAILABLE'),
(14, 8, '8D', 'ECONOMY', 'HELD'),
(15, 9, '9E', 'ECONOMY', 'BOOKED'),
(16, 10, '11F', 'PREMIUM_ECONOMY', 'AVAILABLE');
SELECT * FROM flight_seats;


-- =========================
-- Bookings (10 bookings with varied statuses)
-- =========================
INSERT INTO bookings (booking_id, booking_reference, customer_id, flight_id, seat_id, booking_date, booking_status, total_amount) VALUES
(1, 'BR001', 1, 1, 2, '2026-09-01 10:00:00', 'CONFIRMED', 250.00),
(2, 'BR002', 3, 2, 4, '2026-09-02 11:30:00', 'PENDING', 450.00),
(3, 'BR003', 5, 3, 7, '2026-09-03 09:45:00', 'CONFIRMED', 320.00),
(4, 'BR004', 7, 4, 9, '2026-09-04 14:20:00', 'CANCELLED', 280.00),
(5, 'BR005', 2, 5, 10, '2026-09-05 16:10:00', 'CONFIRMED', 390.00),
(6, 'BR006', 8, 6, 11, '2026-09-06 08:00:00', 'PENDING', 210.00),
(7, 'BR007', 4, 7, 13, '2026-09-06 12:15:00', 'CONFIRMED', 260.00),
(8, 'BR008', 6, 8, 14, '2026-09-07 09:00:00', 'CONFIRMED', 410.00),
(9, 'BR009', 9, 9, 15, '2026-09-07 15:30:00', 'CANCELLED', 330.00),
(10, 'BR010', 10, 10, 16, '2026-09-07 18:45:00', 'CONFIRMED', 295.00);
SELECT * FROM bookings;


-- =========================
-- Passengers (10 passengers)
-- =========================
INSERT INTO passengers (passenger_id, booking_id, first_name, last_name, passport_number, date_of_birth) VALUES
(1, 1, 'Rohit', 'Kumar', 'P1234567', '1990-05-14'),
(2, 2, 'Anjali', 'Menon', 'P2345678', '1988-11-22'),
(3, 3, 'Suresh', 'Rao', 'P3456789', '1979-03-09'),
(4, 4, 'Meena', 'Shah', 'P4567890', '1995-07-30'),
(5, 5, 'Arvind', 'Joshi', 'P5678901', '1982-01-17'),
(6, 6, 'Divya', 'Kapoor', 'P6789012', '1993-09-25'),
(7, 7, 'Nikhil', 'Patel', 'P7890123', '1987-04-11'),
(8, 8, 'Sneha', 'Iyer', 'P8901234', '1996-12-05'),
(9, 9, 'Vivek', 'Gupta', 'P9012345', '1984-02-28'),
(10, 10, 'Kavita', 'Desai', 'P0123456', '1991-08-19');
SELECT * FROM passengers;


-- =========================
-- Payments (10 payments with varied states)
-- =========================
INSERT INTO payments (payment_id, booking_id, transaction_reference, amount, payment_method, payment_status, payment_date) VALUES
(1, 1, 'TXN1001', 250.00, 'CARD', 'SUCCESS', '2026-09-01 10:15:00'),
(2, 2, 'TXN1002', 450.00, 'UPI', 'INITIATED', '2026-09-02 11:45:00'),
(3, 3, 'TXN1003', 320.00, 'NET_BANKING', 'SUCCESS', '2026-09-03 10:00:00'),
(4, 4, 'TXN1004', 280.00, 'CARD', 'FAILED', '2026-09-04 14:35:00'),
(5, 5, 'TXN1005', 390.00, 'WALLET', 'SUCCESS', '2026-09-05 16:20:00'),
(6, 6, 'TXN1006', 210.00, 'UPI', 'SUCCESS', '2026-09-06 08:10:00'),
(7, 7, 'TXN1007', 260.00, 'NET_BANKING', 'SUCCESS', '2026-09-06 12:30:00'),
(8, 8, 'TXN1008', 410.00, 'CARD', 'INITIATED', '2026-09-07 09:10:00'),
(9, 9, 'TXN1009', 330.00, 'WALLET', 'FAILED', '2026-09-07 15:45:00'),
(10, 10, 'TXN1010', 295.00, 'UPI', 'SUCCESS', '2026-09-07 19:00:00');
SELECT * FROM payments;


-- =========================
-- Refunds (for cancelled/failed bookings)
-- =========================
INSERT INTO refunds (refund_id, payment_id, refund_reference, refund_amount, refund_status, refund_date) VALUES
(1, 4, 'RFN2001', 280.00, 'PROCESSED', '2026-09-04 15:00:00'), -- Booking 4 cancelled
(2, 9, 'RFN2002', 330.00, 'FAILED', '2026-09-07 16:00:00'),     -- Booking 9 cancelled
(3, 2, 'RFN2003', 450.00, 'INITIATED', '2026-09-02 12:00:00');  -- Booking 2 still pending
SELECT * FROM refunds;