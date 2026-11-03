CREATE TABLE IF NOT EXISTS nasa_neo (
    id TEXT PRIMARY KEY,
    name TEXT,
    nasa_jpl_url TEXT,
    absolute_magnitude FLOAT,
    is_potentially_hazardous BOOLEAN,
    estimated_diameter_min FLOAT,
    estimated_diameter_max FLOAT,
    close_approach_date DATE,
    relative_velocity FLOAT,
    miss_distance FLOAT
);
