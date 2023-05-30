-- Creating a table


-- 1. `Subscribers` table:

CREATE TABLE Subscribers (
  subscriber_id INT PRIMARY KEY,
  last_name VARCHAR(50),
  first_name VARCHAR(50),
  patronymic VARCHAR(50),
  phone_number VARCHAR(20),
  home_address VARCHAR(100),
  passport_series VARCHAR(10),
  passport_number VARCHAR(20)
);


-- 2. `Cities` table:

CREATE TABLE Cities (
  city_id INT PRIMARY KEY,
  city_code VARCHAR(10),
  city_name VARCHAR(50),
  tariff DECIMAL(8, 2)
);


-- 3. `Conversations` table:

CREATE TABLE Conversations (
  conversation_id INT PRIMARY KEY,
  subscriber_id INT,
  city_id INT,
  conversation_date DATE,
  conversation_time TIME,
  duration_minutes INT,
  FOREIGN KEY (subscriber_id) REFERENCES Subscribers(subscriber_id),
  FOREIGN KEY (city_id) REFERENCES Cities(city_id)
);

-- Now, lets populate the tables with sample data:

-- 1. Insert data into the "Subscribers" table:

INSERT INTO Subscribers (subscriber_id, last_name, first_name, patronymic, phone_number, home_address, passport_series, passport_number)
VALUES
  (1, 'Smith', 'John', 'David', '1234567890', '123 Main St', 'AB', '123456789'),
  (2, 'Johnson', 'Emma', 'Grace', '0987654321', '456 Elm St', 'CD', '987654321'),
  (3, 'Williams', 'Michael', 'James', '5551112222', '789 Oak St', 'EF', '654987321'),
  (4, 'Brown', 'Olivia', 'Sophia', '7778889999', '321 Pine St', 'GH', '987321654'),
  (5, 'Jones', 'William', 'Alexander', '4445556666', '654 Birch St', 'IJ', '159753468');


-- 2. Insert data into the `Cities` table:

INSERT INTO Cities (city_id, city_code, city_name, tariff)
VALUES
  (1, 'CITY1', 'City 1', 0.50),
  (2, 'CITY2', 'City 2', 0.75),
  (3, 'CITY3', 'City 3', 0.60),
  (4, 'CITY4', 'City 4', 0.80),
  (5, 'CITY5', 'City 5', 0.70);


-- 3. Insert data into the `Conversations` table:

INSERT INTO Conversations (conversation_id, subscriber_id, city_id, conversation_date, conversation_time, duration_minutes)
VALUES
  (1, 1, 1, '2023-05-01', '09:15:00', 10),
  (2, 1, 2, '2023-05-02', '14:30:00', 7),
  (3, 2, 3, '2023-05-03', '17:45:00', 15),
  (4, 2, 4, '2023-05-04', '11:00:00', 5),
  (5, 3, 5, '2023-05-05', '13:20:00', 12),
  (6, 3, 1, '2023-05-06', '16:10:00', 8),
  (7, 4, 2, '2023-05-07', '10:45:00', 9),
  (8, 4, 3, '2023-05-08', '19:30:00', 6),
  (9, 5, 4, '2023-05-09', '12:05:00', 11),
  (10, 5, 5, '2023-05-10', '15:40:00', 14);


-- This setup ensures that there are 10 subscribers and 5 cities in the database, 
-- and each of the 5 subscribers makes at least 2 phone calls to different cities. 