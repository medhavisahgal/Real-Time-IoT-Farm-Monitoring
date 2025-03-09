CREATE TABLE SensorData (
    id INT PRIMARY KEY IDENTITY(1, 1),
    sensor_id NVARCHAR(50),
    soil_moisture INT,
    temperature INT,
    timestamp DATETIME DEFAULT GETDATE()
);