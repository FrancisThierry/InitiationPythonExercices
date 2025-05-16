from exercices.pythonObjet.modele.abstraction.base_data_manager import BaseDataManager
from exercices.pythonObjet.modele.car import Car
import pandas as pd
class PandaCarManagement(BaseDataManager):
    """
    Classe de gestion des données de véhicules utilisant pandas.
    """

    def __init__(self, dataFrame=None):
        """
        Initialise le gestionnaire de données de véhicules.
        """
        self.data = dataFrame

        super().__init__()
    def add(self, car:Car):
        # ajout d'une voiture marque pour name
        self.FromCarToRow(car)
        self.data.to_csv(r"C:\data\datasets\cars.csv", index=False)
        """ 
        Ajoute un véhicule au gestionnaire de données.
        :param car: Le véhicule à ajouter.
        """

    def FromCarToRow(self, car:Car):
        # Nouvelle ligne à ajouter
        new_line = {'name': car.marque+ " "+car.modele, 'year': car.annee}

        # Méthode 1 (recommandée) : utiliser pd.concat
        self.data = pd.concat([self.data, pd.DataFrame([new_line])], ignore_index=True)
    def remove(self, car):
        """
        Supprime un véhicule du gestionnaire de données.
        :param car: Le véhicule à supprimer.
        """
        pass
    def update(self, car):
        """
        Met à jour un véhicule dans le gestionnaire de données.
        :param car: Le véhicule à mettre à jour.
        """
        pass
    def get(self):
        """     
        Récupère tous les véhicules du gestionnaire de données.
        :return: Un DataFrame contenant tous les véhicules.
        """
        return self.data
    def getByName(self, name):
        """
        Récupère un véhicule par son nom.
        :param name: Le nom du véhicule à récupérer.
        :return: Un DataFrame contenant le véhicule correspondant au nom.
        """
        listCar = []

        # cars = self.data[self.data["name"] == name]
        cars = self.data[self.data["name"].str.contains(name, case=False, na=False)]
        for index, row in cars.iterrows():
            car = self.buildCar(row)
            # car.mileage = row["mileage"]
            # car.price = row["price"]
            # car.energyType = row["energyType"]
            listCar.append(car)
        return listCar

    def buildCar(self, row):
        car = Car(row["name"], (str(row["name"]).split(' '))[1], row["year"])
        return car



    

    