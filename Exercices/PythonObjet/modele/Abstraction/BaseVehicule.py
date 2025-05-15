from abc import ABC, abstractmethod


class BaseVehicule(ABC):
    """
    Classe abstraite représentant un véhicule.
    """

    def __init__(self, marque: str, modele: str, annee: int):
        """
        Initialise un véhicule avec une marque, un modèle et une année.

        :param marque: La marque du véhicule.
        :param modele: Le modèle du véhicule.
        :param annee: L'année de fabrication du véhicule.
        """
        self.marque = marque
        self.modele = modele
        self.annee = annee

    @abstractmethod
    def getWeelsNeeded(self):
        """
        retourne le nombre de roues.
        """
        pass