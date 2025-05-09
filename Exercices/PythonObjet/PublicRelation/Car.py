from uuid import uuid4


class Car:
    def __init__(self, brand, model, year):
        self.__id = uuid4()
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__mileage = 0
        self.__price = 0.0  
        self.__is_sold = False
        self.__is_available = True  
        self.__energyType = None
        self.__isElectric = False

    @property
    def id(self):
        return self.__id

    @property
    def brand(self):
        return self.__brand