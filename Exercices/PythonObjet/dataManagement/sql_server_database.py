
# Concrete implementations of the database interface
import pyodbc as db
from exercices.pythonObjet.modele.abstraction.database_interface import DatabaseInterface
class SqlServerDatabase(DatabaseInterface):
    def __init__(self, server, database, username=None, password=None):
        super().__init__()
        self.__server = server
        self.__database = database
        ## Optional parameters for SQL Server authentication
        ## If username and password are provided, use them for authentication
        self.__username = username
        self.__password = password  
        self.__connection = self.connect()
    def connect(self):
        self.__connectionString = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.__server};DATABASE={self.__database};Trusted_Connection=yes"
        return db.connect(self.__connectionString)
        

    def query(self, sql, params=None):
        print(f"Executing SqlServer query: {sql}")
        # The 'with self.__connection:' block implies __connection is a context manager.
        # Ensure your connection object supports this (e.g., it has __enter__ and __exit__ methods),
        # or manage transactions explicitly.
        # For simplicity and robust error handling, it's often better to manage cursor and commit/rollback explicitly.

        cursor = None # Initialize cursor outside try block
        try:
            # Ensure connection is active if not using a context manager around cursor.execute
            if not self.__connection:
                self.connect() # Reconnect if connection is lost, or raise an error

            cursor = self.__connection.cursor()
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)

            # Check if the query is a SELECT statement
            # This is a simple check; a more robust way might involve tracking query types
            # or having separate methods for DML (INSERT/UPDATE/DELETE) and DQL (SELECT).
            if sql.strip().upper().startswith("SELECT"):
                result = cursor.fetchall()
                return result
            else:
                # For INSERT, UPDATE, DELETE, you need to commit the changes
                self.__connection.commit()
                # You might want to return the number of affected rows for DML operations
                return cursor.rowcount
        except Exception as e:
            if self.__connection:
                self.__connection.rollback() # Rollback changes on error for DML operations
            print(f"Error executing query: {e}")
            raise # Re-raise the exception after printing, so the caller can handle it
        finally:
            if cursor:
                cursor.close() # Always close the cursor
            # You might choose to disconnect here, or let the calling code manage connection lifecycle
            # self.disconnect() # Uncomment if you want to close connection after every query

    def disconnect(self):
        print("Disconnecting from SqlServer database...")