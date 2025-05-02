from datetime import datetime

def is_date_in_quarter(date, quarter):
    """
    Vérifie si une date donnée appartient à un trimestre donné.

    :param date: datetime, la date à vérifier
    :param quarter: int, le trimestre (1, 2, 3 ou 4)
    :return: bool, True si la date appartient au trimestre, sinon False
    """

    # transformer date de str en datetime
    if isinstance(date, str):
        try:
            date = datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("La date doit être au format 'YYYY-MM-DD'.")
    elif not isinstance(date, datetime):
        raise TypeError("La date doit être de type datetime ou str.")
    

    if not (1 <= quarter <= 4):
        raise ValueError("Le trimestre doit être entre 1 et 4.")

    year = date.year
    if quarter == 1:
        start = datetime(year, 1, 1)
        end = datetime(year, 3, 31)
    elif quarter == 2:
        start = datetime(year, 4, 1)
        end = datetime(year, 6, 30)
    elif quarter == 3:
        start = datetime(year, 7, 1)
        end = datetime(year, 9, 30)
    else:  # quarter == 4
        start = datetime(year, 10, 1)
        end = datetime(year, 12, 31)

    return start <= date <= end