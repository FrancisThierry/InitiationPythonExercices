class SmallAmount:
    def __init__(self, maxValue):
        self.__maxValue = maxValue
        pass
    @property
    def maxValue(self) -> float:
        """Getter for the maximum value."""
        return self.__maxValue