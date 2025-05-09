from Exercices.PythonObjet.Helpers import TvaHelper
from Exercices.PythonObjet.modele.Car import Car
from Exercices.PythonObjet.PublicRelation.Car import Car as PublicCar   

from Exercices.PythonObjet.modele.Customer import Customer
from Exercices.PythonObjet.SecondHandCar.Garage.Garage import Garage
from Exercices.PythonObjet.SecondHandCar.Sales.Sales import Sales
from Exercices.PythonObjet.SecondHandCar.ShowRoom.ShowRoom import ShowRoom
class Application:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"Lancement de {self.name}...")

        print("Création du garage")
        garage = Garage("Garage de la ville", 50)

        print(f"Garage créé : {garage.name} avec une capacité de {garage.maxCapacity} voitures.")
        showroom = ShowRoom(100)
        print("Création de la salle d'exposition")

        print(f"Salle d'exposition créée avec une capacité de {ShowRoom.maxCapacity} voitures.")
        print("Création d'une voiture")
        corolla = Car("Toyota", "Corolla", 2020)
        print(f"Voiture créée : {corolla}")

        corolla.mileage = 15000
        corolla.price = 20000
        print(f"Voiture mise à jour : {corolla}")
        tesla = Car("Tesla", "Model S", 2021)
        print(f"Voiture créée : {tesla}")
        tesla.mileage = 5000
        tesla.price = 80000     
        print(f"Voiture mise à jour : {tesla}")

        print("Ajout de la voiture au garage")
        garage.add_car(corolla)

        print(f"Voiture ajoutée au garage : {corolla}")
        print("Ajout de la voiture à la salle d'exposition")
        showroom.add_car(tesla)
        print(f"Voiture ajoutée à la salle d'exposition : {tesla}")
        print("Création d'un client")
        customer = Customer("Dupont", "test@domain.com", "Pierre")
        print(f"Client créé : {customer.name}")

        print("Création d'une vente")
        sale = Sales(tesla, 20000, "2023-10-01", customer)
        print(f"Vente créée : {sale}")
        print("retrait de la voiture du showroom")
        showroom.remove_car(tesla)
        print(f"Voiture retirée de la salle d'exposition : {tesla}")

        # Saisie d'une voiture à vendre
        print("Création d'une voiture à vendre")

        golf = self.fillCar()
        print(f"Voiture à vendre créée : {golf}")


        
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
        new_car.mileage = car_mileage
        new_car.price = car_price
        new_car.energyType = car_energy_type
        new_car.isElectric = car_is_electric
        new_car.is_sold = car_is_sold
        return new_car


def main():
    app = Application("Programme de gestion de garage")
    app.run()

if __name__ == "__main__":
    main()

