from abc import ABC, abstractmethod
class BaseDataManager(ABC):
    """
    Base class for data managers.
    """

    def __init__(self):
        """
        Initialize the BaseDataManager.
        """
        pass
    @abstractmethod
    def add(self):
        """
        Get data from the data manager.
        """
        pass
    @abstractmethod
    def remove(self):
        """
        Remove data from the data manager.
        """
        pass
    @abstractmethod
    def update(self):
        """
        Update data in the data manager.
        """
        pass
    @abstractmethod
    def get(self):
        """
        Get data from the data manager.
        """
        pass
    @abstractmethod
    def getByName(self):
        """
        Get all data from the data manager.
        """
        pass