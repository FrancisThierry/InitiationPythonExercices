# A high-level module that uses the database
from exercices.pythonObjet.modele.abstraction.database_interface import DatabaseInterface
from exercices.pythonObjet.modele.abstraction.base_data_manager import BaseDataManager
from exercices.pythonObjet.modele.car import Car

class CarDataProcessor(BaseDataManager):
    def __init__(self, db: DatabaseInterface): # Dependency injection
        self.db = db
        super().__init__()

    def add(self, car: Car):
        try:
            # Établir la connexion à la base de données au début de l'opération
            # Cela garantit que la connexion est ouverte avant toute exécution de requête.
            self.db.connect()

            query = "INSERT INTO Car (name, year, selling_price, km_driven, fuel, seller_type, transmission, owner) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            params = (car.name, car.year, car.selling_price, car.km_driven, car.fuel, car.seller_type, car.transmission, car.owner)

            # Exécuter la requête, en passant à la fois la chaîne SQL et les paramètres
            # Votre méthode self.db.query() s'occupera maintenant de l'exécution sécurisée et du commit.
            self.db.query(query, params)


        except Exception as e:
            # Gérer toute erreur qui pourrait survenir pendant l'opération
            print(f"Erreur lors de l'ajout de la voiture : {e}")

        finally:
            # Toujours s'assurer que la connexion est fermée, même en cas d'erreur
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
    