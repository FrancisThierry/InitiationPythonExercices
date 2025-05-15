from Exercices.Pandas.BusinessLogic.Position import Position
class Geo:
    """
    Class to handle geographical data.
    """
    def __init__(self):
        """
        Initialize the Geo class with data.

        :param data: DataFrame containing geographical data.
        """
        

    def distanceBetweenPositions(self, startposition:Position, endPosition:Position):
        """
        Calculate the distance between two geographical positions.

        :param startposition: Starting position (Position object).
        :param endPosition: Ending position (Position object).
        :return: Distance in kilometers.
        """
        # Haversine formula to calculate the distance between two points on the Earth
        from math import radians, sin, cos, sqrt, atan2

        R = 6371.0
        lat1 = radians(startposition.lat)
        lon1 = radians(startposition.lon)   
        lat2 = radians(endPosition.lat)
        lon2 = radians(endPosition.lon)
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c
        return distance
        