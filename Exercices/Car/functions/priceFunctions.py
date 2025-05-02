def calculate_discounted_price(original_price, discount_rate):
    """
    Calcule le prix remisé en fonction du taux de remise.

    :param original_price: float, le prix initial
    :param discount_rate: float, le taux de remise en pourcentage (0-100)
    :return: float, le prix après remise
    """
    if not (0 <= discount_rate <= 100):
        raise ValueError("Le taux de remise doit être compris entre 0 et 100.")
    discounted_price = original_price * (1 - discount_rate / 100)
    return discounted_price