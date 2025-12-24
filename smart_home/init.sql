-- smart_home/init.sql
--CREATE TABLE IF NOT EXISTS sensors (
--    id SERIAL PRIMARY KEY,
--    location VARCHAR(100) NOT NULL,
--    serial_number VARCHAR(50) UNIQUE NOT NULL,
--    type VARCHAR(50) NOT NULL
--);

--INSERT INTO sensors (location, serial_number, type) VALUES
--('Living Room', 'SN-LR-001', 'Temperature'),
--('Kitchen', 'SN-KT-002', 'Light Switch')
--ON CONFLICT (serial_number) DO NOTHING;
--****************
    -- smart_home/init.sql
--    CREATE TABLE IF NOT EXISTS devices (
--       id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        type VARCHAR(50) NOT NULL,
        settings JSONB
    );

--    CREATE TABLE IF NOT EXISTS device_states (
--        device_id INTEGER PRIMARY KEY,
--        state VARCHAR(50),
--        current_temp REAL,
--       target_temp REAL,
--        FOREIGN KEY (device_id) REFERENCES devices(id)
--    );

--    -- Можно добавить начальные данные, если нужно
--    INSERT INTO devices (name, type, settings) VALUES
--    ('Main Heater', 'HEATING_MOD', '{"min_temp": 15, "max_temp": 30}');

--    INSERT INTO device_states (device_id, state, current_temp, target_temp) VALUES
--    (1, 'ON', 22.0, 24.0);
--**************


-- architecture-warmhouse/smart_home/init.sql

CREATE TABLE IF NOT EXISTS sensors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(100) NOT NULL,
    location VARCHAR(100) NOT NULL,
    unit VARCHAR(20) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO sensors (name, type, location, unit) 
VALUES ('Living Room Sensor', 'temperature', 'Living Room', '°C');
