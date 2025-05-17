from exercices.pythonObjet.dataManagement.sql_server_database import SqlServerDatabase
from exercices.pythonObjet.dataManagement.sqlite_database import SqliteDatabase
from exercices.pythonObjet.modele.bike import Bike
from exercices.pythonObjet.modele.car import Car
import pandas as pd
from exercices.pythonObjet.dataManagement.pandas_car_management import PandaCarManagement

from exercices.pythonObjet.modele.customer import Customer
from exercices.pythonObjet.secondHandCar.garage import Garage
from exercices.pythonObjet.secondHandCar.sales import Sales
from exercices.pythonObjet.secondHandCar.showRoom import ShowRoom

from exercices.pythonObjet.dataManagement.db_data_Processor import CarDataProcessor
class Application:
    def __init__(self, name):
        self.name = name

    def testSqlServer(self): 

        # utilisation de sqlServerDb       
        sqlServerDb = SqlServerDatabase("DESKTOP-NLDCTVE", "databaseCar")
        processor = CarDataProcessor(sqlServerDb)

        # utilisation de pandas
        filepath = r"C:\data\datasets\cars.csv"
        dfCar = pd.read_csv(filepath)
        car_manager = PandaCarManagement(dfCar)

        # parcours des voitures
        carsFromPandas = car_manager.get()
        for car in carsFromPandas:
            print(f"Car Name: {car.name}, year: {car.year}")
            # insertion avec sqlServerDb
            processor.add(car)




        # cars = processor.get()

    def testSqlite(self):
        dataBasePath = r"C:\data\dataDBB\CarDb.db"
        sqlite_db = SqliteDatabase(dataBasePath)
        processor = CarDataProcessor(sqlite_db)



        
        cars = processor.get()
        for car in cars:
            print(f"Car Name: {car.name}, Model: {car.year}")

    def testPandaCars(self):
        """
        Test de la classe PandaCarManagement.
        """
        filepath = r"C:\data\datasets\cars.csv"
        dfCar = pd.read_csv(filepath)
        car_manager = PandaCarManagement(dfCar)

        try:
        # ajout d'une voiture
            car_manager.add(Car("DeLorean", "RVF", 2020), filepath)
        except Exception as e:
            print(f"Erreur lors de l'ajout de la voiture : {e}")

            
        data = car_manager.getByName("DeLorean")

        for car in data:
            print(f"Car Name: {car.marque}, Model: {car.modele}, Year: {car.year}")
            # car_manager.add(car)
            # car_manager.remove(car)
            # car_manager.update(car)
        # print(data)
        # car_manager.add("Toyota", "Corolla", 2020)
        # car_manager.add("Honda", "Civic", 2019)
        # print(car_manager.get())
        # print(car_manager.getByName("Toyota"))

    def run(self):
        print(f"Lancement de {self.name}...")
# définition des espaces de vente et de réparation
        garage, showroom = self.SpaceDefinition()

        # creation d'un vélo
        print("Création d'un vélo")
        bike = Bike("Giant", "Escape 3", 2022)
        bike.annee = 2022
        bike.modele = "Escape 3"
        print(f"Vélo créé : {bike}")
        


        print("Création d'une voiture")
        corolla = Car("Toyota", "Corolla", 2020)
        print(f"Voiture créée : {corolla}")

        # creation d'une liste de véhicules
        vehicles = []
        vehicles.append(corolla)
        vehicles.append(bike)

        

        for vehicle in vehicles:
            print(f"Véhicule  {type(vehicle)} : {vehicle.getWeelsNeeded()} roues ")




        # corolla.mileage = 15000
        # corolla.price = 20000
        # print(f"Voiture mise à jour : {corolla}")
        # tesla = Car("Tesla", "Model S", 2021)
        # print(f"Voiture créée : {tesla}")
        # tesla.mileage = 5000
        # tesla.price = 80000     
        # print(f"Voiture mise à jour : {tesla}")

        # print("Ajout de la voiture au garage")
        # garage.add_car(corolla)

        # print(f"Voiture ajoutée au garage : {corolla}")
        # print("Ajout de la voiture à la salle d'exposition")
        # showroom.add_car(tesla)
        # print(f"Voiture ajoutée à la salle d'exposition : {tesla}")
        # print("Création d'un client")
        # customer = Customer("Dupont", "test@domain.com", "Pierre")
        # print(f"Client créé : {customer.name}")

        # print("Création d'une vente")
        # sale = Sales(tesla, 20000, "2023-10-01", customer)
        # print(f"Vente créée : {sale}")
        # print("retrait de la voiture du showroom")
        # showroom.remove_car(tesla)
        # print(f"Voiture retirée de la salle d'exposition : {tesla}")

        # # Saisie d'une voiture à vendre
        # print("Création d'une voiture à vendre")

        # golf = self.fillCar()
        # print(f"Voiture à vendre créée : {golf}")

    def SpaceDefinition(self):
        print("Création du garage")
        garage = Garage("Garage de la ville", 50)

        print(f"Garage créé : {garage.name} avec une capacité de {garage.maxCapacity} voitures.")
        showroom = ShowRoom(100)
        print("Création de la salle d'exposition")

        print(f"Salle d'exposition créée avec une capacité de {ShowRoom.maxCapacity} voitures.")
        return garage,showroom


        
    def fillCar(self):
        car_to_sell = input("Entrez la marque de la voiture : ")
        car_model = input("Entrez le modèle de la voiture : ")  
        car_year = int(input("Entrez l'année de la voiture : "))
        car_mileage = int(input("Entrez le kilométrage de la voiture : "))
        car_price = float(input("Entrez le prix de la voiture : "))
        car_energy_type = input("Entrez le type d'énergie de la voiture : ")
        car_is_electric = input("La voiture est-elle électrique ? (oui/non) : ").lower() == "oui"
        car_is_sold = input("La voiture est-elle vendue ? (oui/non) : ").lower() == "oui"

        new_car = Car(car_to_sell, car_model, car_year)
        new_car.km_driven = car_mileage
        new_car.selling_price = car_price
        new_car.fuel = car_energy_type
        # new_car.isElectric = car_is_electric
        # new_car.is_sold = car_is_sold
        return new_car


def main():
    app = Application("Programme de gestion de garage")
    # app.testSqlite()
    app.testSqlServer()
if __name__ == "__main__":
    main()

