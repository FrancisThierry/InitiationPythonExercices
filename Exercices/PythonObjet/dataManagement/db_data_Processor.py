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
    def update(self, car: Car):
        try:
            self.db.connect()
            query = "UPDATE Car SET name = ?, year = ?, selling_price = ?, km_driven = ?, fuel = ?, seller_type = ?, transmission = ?, owner = ? WHERE id = ?"
            params = (
            car.name,
            car.year,
            car.selling_price,
            car.km_driven,
            car.fuel,
            car.seller_type,
            car.transmission,
            car.owner,
            car.id
            )
            self.db.query(query, params)
        except Exception as e:
            print(f"Erreur lors de la mise à jour de la voiture : {e}")
        finally:
            self.db.disconnect()
    def remove(self, car_id):
        try:
            self.db.connect()
            query = "DELETE FROM Car WHERE id = ?"
            params = (car_id,)
            self.db.query(query, params)
        except Exception as e:
            print(f"Erreur lors de la suppression de la voiture : {e}")
        finally:
            self.db.disconnect()
    def get(self):
        # self.db.connect()
        cars = self.db.query("SELECT name, year, selling_price, km_driven, fuel, seller_type, transmission, owner FROM Car")
        all_cars = []
        for car_row in cars:
            # On utilise les champs explicitement pour correspondre au constructeur Car
            my_car = Car(
            name=car_row[0],
            year=car_row[1],
            selling_price=car_row[2],
            km_driven=car_row[3],
            fuel=car_row[4],
            seller_type=car_row[5],
            transmission=car_row[6],
            owner=car_row[7]
            )
            all_cars.append(my_car)
        return all_cars
    


    def getByName(self, car_name):
        def getByName(self, car_name):
            query = "SELECT name, year, selling_price, km_driven, fuel, seller_type, transmission, owner FROM Car WHERE name = ?"
            result = self.db.query(query, (car_name,))
            if result:
                car_row = result[0]
            return Car(
                name=car_row[0],
                year=car_row[1],
                selling_price=car_row[2],
                km_driven=car_row[3],
                fuel=car_row[4],
                seller_type=car_row[5],
                transmission=car_row[6],
                owner=car_row[7]
            )
            return None

    def getById(self):
        # Suppose que l'ID est passé en argument
        def getById(self, car_id):
            query = "SELECT name, year, selling_price, km_driven, fuel, seller_type, transmission, owner FROM Car WHERE id = ?"
            result = self.db.query(query, (car_id,))
            if result:
                car_row = result[0]
            return Car(
                name=car_row[0],
                year=car_row[1],
                selling_price=car_row[2],
                km_driven=car_row[3],
                fuel=car_row[4],
                seller_type=car_row[5],
                transmission=car_row[6],
                owner=car_row[7]
            )
            return None

    