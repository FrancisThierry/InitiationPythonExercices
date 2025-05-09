class ShowRoom:
    def __init__(self, maxCapacity: int = 50):
        self.__maxCapacity = maxCapacity
        self._cars = []

    def add_car(self, car):
        if len(self._cars) >= self.__maxCapacity:
            raise Exception("Showroom is full")
        if car in self._cars:
            raise Exception("Car already in showroom")
        
        self._cars.append(car)

    def remove_car(self, car):
        if car in self._cars:
            self._cars.remove(car)
        else:
            raise Exception("Car not found in showroom")

    def show_cars(self):
        for car in self._cars:
            print(car)

    @property
    def _cars(self):
        return self.__cars
    @_cars.setter
    def _cars(self, cars: list):
        self.__cars = cars
    
    @property
    def maxCapacity(self):
        return self.__maxCapacity
    @maxCapacity.setter
    def maxCapacity(self, maxCapacity: int):
        self.__maxCapacity = maxCapacity
   