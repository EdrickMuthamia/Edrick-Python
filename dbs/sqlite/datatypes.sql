

CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    dob TEXT,
    phone INTEGER,
    marks REAL
    

)

-- INSERT INTO student (name, email, dob, phone, marks) 
--VALUES ('John Doe', 'john.doe@example.com', '1990-01-01', 1234567890, 85.5);)

-- SELECT * FROM student