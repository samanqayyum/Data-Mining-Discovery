# Let's adjust the previous Python code to incorporate primary and foreign key constraints and store the data in an SQLite database.
import pandas as pd
import numpy as np
from faker import Faker
import sqlite3

# Initialize Faker for synthetic data creation
fake = Faker()

# Setup for synthetic climate data generation
NUM_STATIONS = 50
NUM_OBSERVATIONS = 1000
NUM_CLIMATE_INDICATORS = 10

# Initialize Faker for data generation
fake = Faker()

# Database setup
conn = sqlite3.connect('climate_data.db')  # Database connection
c = conn.cursor()  # Cursor for executing SQL commands

# Create tables with SQL commands
c.execute('''
CREATE TABLE IF NOT EXISTS Stations (
    StationID INTEGER PRIMARY KEY AUTOINCREMENT,
    StationName TEXT,
    Latitude REAL,
    Longitude REAL,
    Elevation INTEGER
);
''')

c.execute('''
CREATE TABLE IF NOT EXISTS ClimateIndicators (
    IndicatorID INTEGER PRIMARY KEY AUTOINCREMENT,
    IndicatorName TEXT
);
''')

c.execute('''
CREATE TABLE IF NOT EXISTS Observations (
    ObservationID INTEGER PRIMARY KEY AUTOINCREMENT,
    IndicatorID INTEGER,
    Value REAL,
    ObservationDate DATE,
    FOREIGN KEY (IndicatorID) REFERENCES ClimateIndicators(IndicatorID)
);
''')

c.execute('''
CREATE TABLE IF NOT EXISTS Recordings (
    RecordingID INTEGER PRIMARY KEY AUTOINCREMENT,
    StationID INTEGER,
    ObservationID INTEGER,
    FOREIGN KEY (StationID) REFERENCES Stations(StationID),
    FOREIGN KEY (ObservationID) REFERENCES Observations(ObservationID)
);
''')



# Insert synthetic data into the database
for _ in range(NUM_STATIONS):
    c.execute('INSERT INTO Stations (StationName, Latitude, Longitude, Elevation) VALUES (?, ?, ?, ?)', 
              (fake.city(), float(fake.latitude()), float(fake.longitude()), fake.random_int(min=0, max=5000)))

indicator_names = ['Temperature', 'Humidity', 'Precipitation', 'Wind Speed', 'Air Pressure', 'Solar Radiation', 'Snowfall', 'Visibility', 'Frost Days', 'Thunder Days']
for name in indicator_names:
    c.execute('INSERT INTO ClimateIndicators (IndicatorName) VALUES (?)', (name,))

for _ in range(NUM_OBSERVATIONS):
    c.execute('INSERT INTO Observations (IndicatorID, Value, ObservationDate) VALUES (?, ?, ?)', 
              (fake.random_int(min=1, max=NUM_CLIMATE_INDICATORS), fake.random_number(), fake.date_between(start_date='-5y', end_date='today')))

for _ in range(NUM_OBSERVATIONS):
    c.execute('INSERT INTO Recordings (StationID, ObservationID) VALUES (?, ?)', 
              (fake.random_int(min=1, max=NUM_STATIONS), _ + 1))



# Commit the transactions and close the connection
conn.commit()
conn.close()

# Output the path to the SQLite database
'climate_data.db'
# After setting up your database connection and cursor

# Example for creating one table with primary and foreign keys





