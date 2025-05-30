from exercices.design_patterns.ex_cround_funding.mailer import Mailer
from exercices.design_patterns.ex_cround_funding.cagnotte import Cagnotte
from exercices.design_patterns.ex_cround_funding.cround_funding import CroundFunding
from exercices.design_patterns.ex_cround_funding.observer import Observer
from exercices.design_patterns.ex_cround_funding.user import User


class CagnotteNotifier(Observer):
    def __init__(self, cagnotte:Cagnotte, user:User, mailer:Mailer) -> None:
        self.cagnottes = cagnotte
        self.user = user
        self.mailer = mailer

  
    def update(self, crowfunding:CroundFunding) -> None:
        """Update method to handle notifications."""
        if(crowfunding.get_total_funds() >= self.cagnottes.goal):
            print(f"Goal reached for {crowfunding.project}! Total funds: {crowfunding.get_total_funds()} ")
            self.mailer.send(
                subject=f"Goal reached for {crowfunding.project}!",
                body=f"Congratulations {self.user.name}  ! The goal of {self.cagnottes.goal} has been reached with a total of {crowfunding.get_total_funds()}."
            )