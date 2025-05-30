from exercices.design_patterns.ex_cround_funding.cround_funding import CroundFunding
from exercices.design_patterns.ex_cround_funding.observer import Observer
from exercices.design_patterns.ex_cround_funding.small_amount import SmallAmount


class SmallAmountNotifier(Observer):
    def __init__(self, small_amount:SmallAmount):
        self.__small_amount = small_amount

  
    def update(self, crowfunding:CroundFunding) -> None:
        """Update method to handle notifications."""
        if(crowfunding.amount <= self.__small_amount.maxValue):
            print(f"Small amount dectected!")