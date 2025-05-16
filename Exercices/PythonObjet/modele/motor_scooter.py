from exercices.pythonObjet.modele.abstraction.base_vehicule import BaseVehicule


class MotorScooter(BaseVehicule):
    """
    Classe représentant un scooter à moteur.
    Hérite de la classe Vehicule.
    """

    def __init__(self, marque, modele, annee, couleur, prix):
        super().__init__(marque, modele, annee)
        self.couleur = couleur
        self.prix = prix
    def __str__(self):
        return f"MotorScooter: {self.marque} {self.modele}, Couleur: {self.couleur}, Prix: {self.prix}"
    def getWeelsNeeded(self):
        """
        retourne le nombre de roues.
        """
        return 2