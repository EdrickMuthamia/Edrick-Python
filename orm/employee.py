from db import PG

class Employee():

    def __init__(self):
        self.pg = PG()
        
        query="""
            CREATE TABLE IF NOT EXISTS employee(
              id BIGSERIAL PRIMARY KEY,
              name TEXT NOT NULL,
              email TEXT NOT NULL UNIQUE
            )
        """
        self.pg.pg_query(query=query)
    
    def add(self, name, email):
        query="""
          INSERT INTO employee
          (name, email)
          VALUES (%s, %s)
        """
        self.pg.pg_query(query=query, params=(name, email))

    def all(self):
        query="""
          SELECT * FROM employee
        """
        results = self.pg.pg_query(query=query)
        for employee in results:
            print(employee)
        return results
    

emp1=Employee()

## CREATE OTHER CLASSES
## CRUD ->  Create Read Update Delete

#create an employee (C)
#all employees (R)
#Update 
#Delete
# emp1.add(name="Marry",email="marry@gmail.com")

# while True:
#     name=input("Enter employee name:")
#     email=input("Enter employee email:")
#     emp1.add(name=name,email=email)

#     print("Employee added ")
#     print("")
#     another=input("Enter y to add another ?:")
#     if another=="y" or another=="Y":
#         continue
#     break

# READ, READ. UPDATE()

emp1.all()