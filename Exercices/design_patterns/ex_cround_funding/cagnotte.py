class Cagnotte:  
    def __init__(self, objectif: float):
        self.objectif = objectif

    def est_atteint(self) -> bool:
        return self.montant >= self.objectif

  