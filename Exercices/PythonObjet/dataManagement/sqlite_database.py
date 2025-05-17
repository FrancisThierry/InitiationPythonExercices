
# Concrete implementations of the database interface
import sqlite3
from exercices.pythonObjet.modele.abstraction.database_interface import DatabaseInterface
class SqliteDatabase(DatabaseInterface):
    def __init__(self, dataPath):
        super().__init__()
        self.__dataPath = dataPath
        self.__connection = self.connect()
    def connect(self):
        return sqlite3.connect(self.__dataPath)
        

    def query(self, sql):
        with self.__connection:
            cursor = self.__connection.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
        print(f"Executing Sqlite query: {sql}")

    def disconnect(self):
        print("Disconnecting from Sqlite database...")