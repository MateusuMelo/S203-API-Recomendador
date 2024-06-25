import sqlite3
from sqlite3 import Error

class Database:
    def __init__(self, db_file):
        self.connection = None
        try:
            self.connection = self.connect(db_file)
            print(f"Successfully connected to the database '{db_file}'")
        except Error as e:
            print(f"Error connecting to the database: {e}")
            raise

    def connect(self, db_file):
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(f"Error connecting to the database: {e}")
            raise

    def execute_query(self, query, params=None):
        if self.connection is None:
            print("No connection to the database.")
            return
        
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            self.connection.commit()
            print("Query executed successfully.")

            return cursor.fetchall()
        except Error as e:
            print(f"Error executing query: {e}")
            return None

    def close(self):
        if self.connection is not None:
            self.connection.close()
