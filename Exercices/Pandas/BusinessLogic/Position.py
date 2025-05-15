class Position:
    def __init__(self, lat, lon):
        self.__lat = lat
        self.__lon = lon    

    def __repr__(self):
        return f"Position({self.__lat}, {self.__lon})"
    
    @property
    def lat(self):
        return self.__lat
    @lat.setter
    def lat(self, lat):
        self.__lat = lat
    @property
    def lon(self):
        return self.__lon
    @lon.setter
    def lon(self, lon):
        self.__lon = lon
