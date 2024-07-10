CREATE DATABASE wildlife_db;

USE wildlife_db;

CREATE TABLE species (
    species_id INT PRIMARY KEY AUTO_INCREMENT,
    common_name VARCHAR(100),
    scientific_name VARCHAR(100),
    conservation_status VARCHAR(50)
);

CREATE TABLE animals (
    animal_id INT PRIMARY KEY AUTO_INCREMENT,
    species_id INT,
    name VARCHAR(100),
    birth_date DATE,
    gender CHAR(1),
    FOREIGN KEY (species_id) REFERENCES species(species_id)
);

CREATE TABLE tracking (
    tracking_id INT PRIMARY KEY AUTO_INCREMENT,
    animal_id INT,
    timestamp DATE,
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    FOREIGN KEY (animal_id) REFERENCES animals(animal_id)
);

CREATE TABLE health_records (
    record_id INT PRIMARY KEY AUTO_INCREMENT,
    animal_id INT,
    checkup_date DATE,
    health_status VARCHAR(100),
    notes TEXT,
    FOREIGN KEY (animal_id) REFERENCES animals(animal_id)
);

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50),
    password VARCHAR(255),
    role VARCHAR(50)
);

CREATE TABLE conservation_measures (
    measure_id INT PRIMARY KEY AUTO_INCREMENT,
    species_id INT,
    description TEXT,
    start_date DATE,
    end_date DATE,
    FOREIGN KEY (species_id) REFERENCES species(species_id)
);

CREATE TABLE population_statistics (
    stat_id INT PRIMARY KEY AUTO_INCREMENT,
    species_id INT,
    year INT,
    population_count INT,
    FOREIGN KEY (species_id) REFERENCES species(species_id)
);
