from exercices.pythonObjet.modele.abstraction.base_vehicule import BaseVehicule


class Bike(BaseVehicule):
    def __init__(self,marque, modele, annee):
        super().__init__(marque, modele, annee)

    def __str__(self):
        return f"Bike: {self.marque} {self.modele}, Year: {self.annee}"
    
    def getWeelsNeeded(self):
        """
        retourne le nombre de roues.
        """
        return 2
    