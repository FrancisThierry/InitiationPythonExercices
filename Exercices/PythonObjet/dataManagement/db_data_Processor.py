# A high-level module that uses the database
from exercices.pythonObjet.modele.abstraction.database_interface import DatabaseInterface
from exercices.pythonObjet.modele.abstraction.base_data_manager import BaseDataManager
from exercices.pythonObjet.modele.car import Car

class CarDataProcessor(BaseDataManager):
    def __init__(self, db: DatabaseInterface): # Dependency injection
        self.db = db
        super().__init__()

    def add(self):
        self.db.connect()
        self.db.query("SELECT * FROM users")
        self.db.disconnect()
    def update(self):
        self.db.connect()
        self.db.query("SELECT * FROM users")
        self.db.disconnect()
    def remove(self):
        self.db.connect()
        self.db.query("SELECT * FROM users")
        self.db.disconnect()
    def get(self):
        # self.db.connect()
        cars = self.db.query("SELECT * FROM car")
        allcars = []
        for car in cars:
            myCar = Car(car[0], car[1], car[2])
            allcars.append(myCar)
        return allcars


        self.db.disconnect()
    def getByName(self):
        self.db.connect()
        self.db.query("SELECT * FROM users")
        self.db.disconnect()
    