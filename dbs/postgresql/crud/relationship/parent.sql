
-- DROP TABLE IF EXISTS parent ;
CREATE TABLE IF NOT EXISTS parent(
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(250) NOT NULL UNIQUE
    
);

--DROP TABLE IF EXISTS parent_address ;
CREATE TABLE IF NOT EXISTS parent_address(
    id BIGSERIAL PRIMARY KEY,
    parent_email VARCHAR(250) REFERENCES parent(email) ,
    county_name VARCHAR(250) ,
    town VARCHAR(250),
    longitude REAL,
    latitude REAL,
    house_no VARCHAR(200)
);

