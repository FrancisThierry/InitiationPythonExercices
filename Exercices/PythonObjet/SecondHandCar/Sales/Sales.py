class Sales:
    def __init__(self, car, price, date, customer=None):
        self.__car = car
        self.__price = price
        self.__date = date
        self.__customer = customer

    def __str__(self):
        return f"Sale of {self.__car} for {self.__price} on {self.__date}"
    
    @property
    def car(self):
        return self.__car
    @car.setter
    def car(self, car):
        self.__car = car
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price):
        self.__price = price
    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date):
        self.__date = date