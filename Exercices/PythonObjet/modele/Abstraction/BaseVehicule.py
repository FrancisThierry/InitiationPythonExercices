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
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee

    @abstractmethod
    def getWeelsNeeded(self):
        """
        retourne le nombre de roues.
        """
        pass
    @property
    def marque(self):
        return self.__marque
    @property
    def modele(self):
        return self.__modele
    @property
    def annee(self):
        return self.__annee
    @marque.setter
    def marque(self, marque):
        self.__marque = marque
    @modele.setter
    def modele(self, modele):
        self.__modele = modele
    @annee.setter
    def annee(self, annee):
        self.__annee = annee