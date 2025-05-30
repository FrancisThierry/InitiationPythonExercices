from abc import ABC, abstractmethod


class Observer(ABC):
    """Observer interface for the observer pattern."""

    @abstractmethod
    def update(self, *args, **kwargs):
        """Update method to be implemented by concrete observers."""
        pass