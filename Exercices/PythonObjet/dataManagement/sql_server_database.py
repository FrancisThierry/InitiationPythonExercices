
# Concrete implementations of the database interface
import pyodbc as db
from exercices.pythonObjet.modele.abstraction.database_interface import DatabaseInterface
class SqlServerDatabase(DatabaseInterface):
    def __init__(self, server, database, username, password):
        super().__init__()
        self.__server = server
        self.__database = database
        self.__username = username
        self.__password = password  
        self.__connection = self.connect()
    def connect(self):
        self.__connectionString = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={self.__server};DATABASE={self.__database};UID={self.__username};PWD={self.__password}"
        return db.connect(self.__connectionString)
        

    def query(self, sql):
        with self.__connection:
            cursor = self.__connection.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        print(f"Executing SqlServer query: {sql}")

    def disconnect(self):
        print("Disconnecting from SqlServer database...")