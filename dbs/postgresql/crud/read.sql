
--SELECT <columns || *> 
--FROM <table> 
--WHERE <READ CONSTRAINS> 
--ORDER <> LIMIT <> 

--REad all columns and

-- SELECT * FROM student;

--REad only name and email
-- SELECT name,email from student;

-- SELECT * from student
-- WHERE email='sam@gmail.com'
-- OR
-- email='alice@gmail.com'

--on my own ---

--1 select all records--
-- SELECT * FROM student;

--2 read specifc fields--
-- SELECT name, email,have_father FROM student;

--3 where--
-- SELECT * FROM student
-- where email='paul@gmail.com'
-- OR
-- email='virginia@gmail.com';

--4 using AND instead of OR--- ==>NO DATA <===
-- SELECT * FROM student
-- where email='paul@gmail.com'
-- AND
-- email='virginia@gmail.com'

--5---
-- SELECT * FROM student
-- WHERE have_father=TRUE
-- OR
-- is_married=TRUE

--6  And--
-- SELECT * FROM student
-- WHERE pocket_money >2000
-- AND pocket_money <5000

--7 order=>> default is ID  ==ASCENDING ORDER--
-- SELECT *  FROM student
-- ORDER BY name ASC 

--8--LIMIT--MOSTLY COMBINE ORDER WITH LIMIT
-- SELECT * FROM student
-- ORDER BY name ASC 
-- LIMIT 3

--9 ORDER IN DESCENDING ORDER--
SELECT * FROM student
ORDER BY name DESC
LIMIT 3