class Garage:
    def __init__(self, name: str, capacity: int = 50):
        self.__name = name
        self.__cars = []
        self.__maxCapacity = 50  # Default capacity
        self.__capacity = self.__maxCapacity  # Current capacity


    def add_car(self, car):
        if self.__capacity <= 0:
            raise Exception("Garage is full")
        self.cars.append(car)
        self.__capacity -= 1

    def remove_car(self, car):
        self.__cars.remove(car)

    def list_cars(self):
        for car in self.__cars:
            print(car)

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cars(self):
        return self.__cars
    @cars.setter
    def cars(self, cars: list):
        self.__cars = cars
    @property
    def maxCapacity(self):
        return self.__maxCapacity
    @maxCapacity.setter
    def maxCapacity(self, maxCapacity: int):
        self.__maxCapacity = maxCapacity