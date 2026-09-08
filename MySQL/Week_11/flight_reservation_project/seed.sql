SET FOREIGN_KEY_CHECKS = 0;
DROP TABLE IF EXISTS flights;
DROP TABLE IF EXISTS aircrafts;
DROP TABLE IF EXISTS airports;
DROP TABLE IF EXISTS airlines;
SET FOREIGN_KEY_CHECKS = 1;


CREATE TABLE airlines (
    airline_id INT PRIMARY KEY AUTO_INCREMENT,
    airline_code VARCHAR(10) UNIQUE NOT NULL,
    airline_name VARCHAR(100) NOT NULL
);

CREATE TABLE airports (
    airport_id INT PRIMARY KEY AUTO_INCREMENT,
    airport_code VARCHAR(10) UNIQUE NOT NULL,
    airport_name VARCHAR(100) NOT NULL,
    city VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL
);

CREATE TABLE aircrafts (
    aircraft_id INT PRIMARY KEY AUTO_INCREMENT,
    aircraft_model VARCHAR(100) NOT NULL,
    total_seats INT NOT NULL CHECK (total_seats > 0),
    airline_id INT NOT NULL,
    FOREIGN KEY (airline_id) REFERENCES airlines(airline_id)
);

CREATE TABLE flights (
    flight_id INT PRIMARY KEY AUTO_INCREMENT,
    flight_number VARCHAR(20) UNIQUE NOT NULL,
    airline_id INT NOT NULL,
    aircraft_id INT NOT NULL,
    origin_airport_id INT NOT NULL,
    destination_airport_id INT NOT NULL,
    departure_time DATETIME NOT NULL,
    arrival_time DATETIME NOT NULL,
    base_fare DECIMAL(10,2) NOT NULL CHECK (base_fare > 0),
    status ENUM('SCHEDULED','BOARDING','COMPLETED','CANCELLED') NOT NULL,
    FOREIGN KEY (airline_id) REFERENCES airlines(airline_id),
    FOREIGN KEY (aircraft_id) REFERENCES aircrafts(aircraft_id),
    FOREIGN KEY (origin_airport_id) REFERENCES airports(airport_id),
    FOREIGN KEY (destination_airport_id) REFERENCES airports(airport_id)
);

-- Seed data
INSERT INTO airlines (airline_code, airline_name) VALUES
('AI','Air India'),('6E','IndiGo'),('SG','SpiceJet');

INSERT INTO airports (airport_code, airport_name, city, country) VALUES
('HYD','Rajiv Gandhi Intl','Hyderabad','India'),
('DEL','Indira Gandhi Intl','New Delhi','India'),
('BLR','Kempegowda Intl','Bengaluru','India'),
('BOM','Chhatrapati Shivaji Intl','Mumbai','India'),
('MAA','Chennai Intl','Chennai','India'),
('CCU','Netaji Subhas Intl','Kolkata','India');
