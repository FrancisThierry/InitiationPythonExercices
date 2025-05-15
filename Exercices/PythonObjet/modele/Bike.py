from Exercices.PythonObjet.modele.Abstraction import BaseVehicule


class Bike(BaseVehicule):
    def __init__(self, id, marque, modele, couleur, prix, type_roue):
        super().__init__(id, marque, modele, couleur, prix)
        self.type_roue = type_roue

    def __str__(self):
        return f"Bike: {self.marque} {self.modele}, Couleur: {self.couleur}, Prix: {self.prix}, Type de roue: {self.type_roue}"
    
    def getWeelsNeeded(self):
        """
        retourne le nombre de roues.
        """
        return 2