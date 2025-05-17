from uuid import uuid4

from exercices.pythonObjet.modele.abstraction.base_vehicule import BaseVehicule


class Car(BaseVehicule):
    def __init__(self, name, year, price):
        super().__init__(name, year, price)
        self.__id = uuid4()    
        self.__energyType = None
        self._selling_price = price
   
    
    def getWeelsNeeded(self):
        """
        retourne le nombre de roues.
        """
        return 4
    @property
    def km_driven(self):
        return getattr(self, '_km_driven', None)

    @km_driven.setter
    def km_driven(self, value):
        self._km_driven = value

    @property
    def fuel(self):
        return getattr(self, '_fuel', None)

    @fuel.setter
    def fuel(self, value):
        self._fuel = value

    @property
    def seller_type(self):
        return getattr(self, '_seller_type', None)

    @seller_type.setter
    def seller_type(self, value):
        self._seller_type = value

    @property
    def transmission(self):
        return getattr(self, '_transmission', None)

    @transmission.setter
    def transmission(self, value):
        self._transmission = value

    @property
    def owner(self):
        return getattr(self, '_owner', None)

    @owner.setter
    def owner(self, value):
        self._owner = value
