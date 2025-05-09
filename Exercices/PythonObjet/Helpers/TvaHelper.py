class TvaHelper:
    @staticmethod
    def calcule_prix_ttc(prix_ht, taux_tva):
        """
        Calcule le prix toutes taxes comprises (TTC) à partir du prix hors taxe et du taux de TVA.

        :param prix_ht: Prix hors taxe
        :param taux_tva: Taux de TVA (en pourcentage)
        :return: Prix TTC
        """
        return prix_ht * (1 + (taux_tva / 100))
    @staticmethod
    def calcule_tva(prix_ht, taux_tva):
        """
        Calcule le montant de la TVA à partir du prix hors taxe et du taux de TVA.

        :param prix_ht: Prix hors taxe
        :param taux_tva: Taux de TVA (en pourcentage)
        :return: Montant de la TVA
        """
        return prix_ht * (taux_tva / 100) 