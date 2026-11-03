CREATE TABLE IF NOT EXISTS spacex_launches (
    id TEXT PRIMARY KEY,
    name TEXT,
    date_utc TEXT,
    success BOOLEAN,
    rocket TEXT,
    details TEXT,
    flight_number INT,
    upcoming BOOLEAN
);
