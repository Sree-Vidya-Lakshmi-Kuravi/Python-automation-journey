-- Duplicate airline code.
INSERT INTO airlines (airline_id, airline_name, airline_code) VALUES (4, 'Singapore Airlines', 'SQ');

-- Duplicate airport code.
INSERT INTO airports (airport_id, airport_code, airport_name, city, country) VALUES
(11, 'HYD', 'Rajiv Gandhi International Airport', 'Hyderabad', 'India');

-- Duplicate customer email.
INSERT INTO customers (customer_id, first_name, last_name, email, phone, date_of_birth) VALUES
(21, 'Amit', 'Sharma', 'amit.sharma@example.com', '9876543210', '1985-03-12');

-- Invalid airline ID in aircraft.
INSERT INTO aircrafts (aircraft_id, airline_id, model, total_seats)
VALUES (6, 99, 'Boeing 747', 400);

-- Invalid airport ID in flight.
INSERT INTO flights (flight_id, flight_number, airline_id, aircraft_id, origin_airport_id, destination_airport_id, departure_time, arrival_time, base_fare, status)
VALUES (11, 'DL999', 1, 1, 99, 4, '2026-09-20 08:00:00', '2026-09-20 10:00:00', 200.00, 'SCHEDULED');

-- Invalid customer ID in booking
INSERT INTO bookings (booking_id, booking_reference, customer_id, flight_id, seat_id, booking_date, booking_status, total_amount) VALUES (11, 'BR011', 99, 1, 1, '2026-09-08 09:00:00', 'CONFIRMED', 250.00);

-- Duplicate seat number for the same flight
INSERT INTO flight_seats (seat_id, flight_id, seat_number, seat_class, seat_status)
VALUES (17, 1, '12A', 'ECONOMY', 'AVAILABLE');

-- Negative fare
INSERT INTO flights (flight_id, flight_number, airline_id, aircraft_id, origin_airport_id, destination_airport_id, departure_time, arrival_time, base_fare, status) VALUES (12, 'SQ999', 3, 5, 1, 2, '2026-09-21 07:00:00', '2026-09-21 09:00:00', -100.00, 'SCHEDULED');

-- Negative booking amount
INSERT INTO bookings (booking_id, booking_reference, customer_id, flight_id, seat_id, booking_date, booking_status, total_amount) VALUES (12, 'BR012', 1, 1, 1, '2026-09-08 10:00:00', 'CONFIRMED', -250.00);

-- Negative payment amount
INSERT INTO payments (payment_id, booking_id, transaction_reference, amount, payment_method, payment_status, payment_date) VALUES (11, 1, 'TXN1011', -300.00, 'CARD', 'INITIATED', '2026-09-08 11:00:00');