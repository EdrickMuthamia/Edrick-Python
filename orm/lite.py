import sqlite3
import os

class LITE:
    def __init__(self, db_name="employee.db"):
        # Create database in the orm folder
        self.db_path = os.path.join(os.path.dirname(__file__), db_name)
        self.connection = sqlite3.connect(self.db_path, check_same_thread=False)
    
    def lite_query(self, query, params=()):
        """Execute query and return results"""
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        
        # Try to fetch results (for SELECT queries)
        result = None
        try:
            result = cursor.fetchall()
        except Exception:
            pass
        
        self.connection.commit()
        cursor.close()
        return result
    
    def close(self):
        """Close database connection"""
        self.connection.close()