

CREATE TABLE IF NOT EXISTS student(
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    dob DATE,
    phone INTEGER,
    marks REAL,
    is_married BOOLEAN,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO student (name, email, dob, phone, marks) 
VALUES ('John Doe', 'john.doe@example.com', '1990-01-01', 1234567890, 85.5);

SELECT * FROM student;