-- smart_home/init.sql
CREATE TABLE IF NOT EXISTS sensors (
    id SERIAL PRIMARY KEY,
    location VARCHAR(100) NOT NULL,
    serial_number VARCHAR(50) UNIQUE NOT NULL,
    type VARCHAR(50) NOT NULL
);

INSERT INTO sensors (location, serial_number, type) VALUES
('Living Room', 'SN-LR-001', 'Temperature'),
('Kitchen', 'SN-KT-002', 'Light Switch')
ON CONFLICT (serial_number) DO NOTHING;
