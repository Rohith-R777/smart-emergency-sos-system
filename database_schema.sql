-- Emergency SOS System Database Schema

CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone_number VARCHAR(15) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Emergencies (
    emergency_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    emergency_type VARCHAR(100) NOT NULL,
    description TEXT,
    location VARCHAR(255) NOT NULL,
    status ENUM('reported', 'in_progress', 'resolved') DEFAULT 'reported',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

CREATE TABLE Alerts (
    alert_id INT AUTO_INCREMENT PRIMARY KEY,
    emergency_id INT NOT NULL,
    alert_message TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (emergency_id) REFERENCES Emergencies(emergency_id) ON DELETE CASCADE
);

CREATE TABLE Responders (
    responder_id INT AUTO_INCREMENT PRIMARY KEY,
    responder_name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(15) NOT NULL,
    status ENUM('available', 'busy') DEFAULT 'available'
);

CREATE TABLE Response_Assignments (
    assignment_id INT AUTO_INCREMENT PRIMARY KEY,
    emergency_id INT NOT NULL,
    responder_id INT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (emergency_id) REFERENCES Emergencies(emergency_id) ON DELETE CASCADE,
    FOREIGN KEY (responder_id) REFERENCES Responders(responder_id) ON DELETE CASCADE
);