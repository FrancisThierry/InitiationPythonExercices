from functions.dateFunctions import is_date_in_quarter

def filter_second_quarter(carData):
    """
    Filtre une liste de données pour ne conserver que celles dont la date (carData[3]) est dans le second trimestre.

    :param carData: Liste de données où chaque élément contient une date au 4e index (carData[3]).
    :return: Liste filtrée contenant uniquement les éléments dont la date est dans le second trimestre.
    """
    return [data for data in carData if is_date_in_quarter(data[3], 2)]