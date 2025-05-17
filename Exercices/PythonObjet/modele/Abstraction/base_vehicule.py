from abc import ABC, abstractmethod


class BaseVehicule(ABC):
    """
    Classe abstraite représentant un véhicule.
    """

    def __init__(self, name: str, year: int, price: int):
        """
        Initialise un véhicule avec une marque, un modèle et une année.

        :param marque: La marque du véhicule.
        :param modele: Le modèle du véhicule.
        :param annee: L'année de fabrication du véhicule.
        """
        self.__name = name
        self.__year = year
        self.__price = price

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

    # Ajout des nouvelles propriétés pour respecter les entêtes demandées

    @property
    def name(self):
        return f"{self.__name} "

    @name.setter
    def name(self, value):
    # Suppose value is "marque modele"
        parts = value.split(' ', 1)
        if len(parts) == 2:
            self.__marque, self.__modele = parts
        else:
            self.__marque = value
            self.__modele = ""

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__annee = value

    @property
    def selling_price(self):
        return getattr(self, '_selling_price', None)

    @selling_price.setter
    def selling_price(self, value):
        self._selling_price = value

   