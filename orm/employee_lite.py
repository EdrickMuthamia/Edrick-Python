from lite import LITE

class Employee():

    def __init__(self):
        self.lite = LITE()
        
        query="""
            CREATE TABLE IF NOT EXISTS employee(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              email TEXT NOT NULL UNIQUE
            )
        """
        self.lite.lite_query(query=query)
    
    def add(self, name, email):
        query="""
          INSERT INTO employee
          (name, email)
          VALUES (?, ?)
        """
        self.lite.lite_query(query=query, params=(name, email))

    def all(self):
        query="""
          SELECT * FROM employee
        """
        results = self.lite.lite_query(query=query)
        for employee in results:
            print(f"ID: {employee[0]}, Name: {employee[1]}, Email: {employee[2]}")
        return results
    

emp1 = Employee()

## CREATE OTHER CLASSES
## CRUD ->  Create Read Update Delete
## sqlite

#create an employee (C)
#all employees (R)
#Update 
#Delete
# emp1.add(name="Marry",email="marry@gmail.com")

while True:
    name = input("Enter employee name: ")
    email = input("Enter employee email: ")
    emp1.add(name=name, email=email)

    print("Employee added ")
    print("")
    print("ALL EMPLOYEES")
    emp1.all()
    print("---------")
    another = input("Enter y to add another ?: ")
    if another == "y" or another == "Y":
        continue
    break

# READ, READ. UPDATE()

# emp1.all()