from sqlite_db import SQLiteDB

class EmployeeSQLite:
    def __init__(self):
        self.db = SQLiteDB()
        
        # SQLite uses INTEGER PRIMARY KEY AUTOINCREMENT instead of BIGSERIAL
        query = """
            CREATE TABLE IF NOT EXISTS employee(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              email TEXT NOT NULL UNIQUE
            )
        """
        self.db.execute_query(query)
    
    def add(self, name, email):
        # SQLite uses ? placeholders instead of %s
        query = """
          INSERT INTO employee
          (name, email)
          VALUES (?, ?)
        """
        self.db.execute_query(query, params=(name, email))
        print(f"Added employee: {name} ({email})")

    def all(self):
        query = """
          SELECT * FROM employee
        """
        results = self.db.execute_query(query)
        print("All employees:")
        for employee in results:
            print(f"ID: {employee['id']}, Name: {employee['name']}, Email: {employee['email']}")
        return results
    
    def update(self, employee_id, name=None, email=None):
        if name:
            query = "UPDATE employee SET name = ? WHERE id = ?"
            self.db.execute_query(query, (name, employee_id))
        if email:
            query = "UPDATE employee SET email = ? WHERE id = ?"
            self.db.execute_query(query, (email, employee_id))
        print(f"Updated employee ID: {employee_id}")
    
    def delete(self, employee_id):
        query = "DELETE FROM employee WHERE id = ?"
        self.db.execute_query(query, (employee_id,))
        print(f"Deleted employee ID: {employee_id}")
    
    def close(self):
        self.db.close()

# Test the SQLite version
if __name__ == "__main__":
    emp = EmployeeSQLite()
    
    # Add some employees
    emp.add("John Doe", "john@example.com")
    emp.add("Jane Smith", "jane@example.com")
    
    # Show all employees
    emp.all()
    
    # Update an employee
    emp.update(1, name="John Updated")
    
    # Show all again
    emp.all()
    
    # Close connection
    emp.close()