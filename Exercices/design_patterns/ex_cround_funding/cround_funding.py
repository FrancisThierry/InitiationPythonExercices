class CroundFunding:
    def __init__(self,project:str, goal: float) :
        self.__amount = 0.0
        self.project = project
        self.goal = goal
        self.total_funds = 0.0
        self._observers = [] # Liste pour stocker les observateurs
    def add_observer(self, observer) -> None:
        """Ajoute un observateur à la liste des observateurs."""
        if observer not in self._observers:
            self._observers.append(observer)
    def remove_observer(self, observer) -> None:
        """Retire un observateur de la liste des observateurs."""
        if observer in self._observers:
            self._observers.remove(observer)
    def notify_observers(self) -> None:
        """Notifie tous les observateurs avec un message."""
        for observer in self._observers:
            observer.update(self)

    def contribute(self, amount: float) -> None:
        self.__amount = amount
        if amount <= 0:
            raise ValueError("Contribution must be greater than zero.")
        self.total_funds += amount
        self.notify_observers()

    def is_goal_reached(self) -> bool:
        self.notify_observers()
        return self.total_funds >= self.goal


    def get_total_funds(self) -> float:
        return self.total_funds
    
    
    @property
    def amount(self) -> float:
        return self.__amount