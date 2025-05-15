from uuid import uuid4

from Exercices.PythonObjet.modele.Abstraction.BaseVehicule import BaseVehicule


class Car(BaseVehicule):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)
        self.__id = uuid4()    
        self.__energyType = None
   
    
    def getWeelsNeeded(self):
        """
        retourne le nombre de roues.
        """
        return 4