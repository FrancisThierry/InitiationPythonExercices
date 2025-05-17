from abc import ABC, abstractmethod

# Define an abstract interface for a database
class DatabaseInterface(ABC):
    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def query(self, sql, params=None):
        pass

    @abstractmethod
    def disconnect(self):
        pass