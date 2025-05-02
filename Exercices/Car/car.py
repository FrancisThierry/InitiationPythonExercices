# Exercice à partir du fichier car.txt
# Ecrire par marque, générer un fichier contenant la marque et le prix remisé pour les modèle du second trimestre

# 0. Importer les modules nécessaires

from functions.readFunctions import read_file_without_header
from functions.writeFunction import write_data_to_directory
from functions.marqueFunctions import extract_unique_brands
from functions.filterListeFunction import filter_second_quarter

# 1. Importer les données de carInput.txt
carFilePath = "C:\\data\\carInput.txt"

carData = read_file_without_header(carFilePath)

# 2. Filtrer les données pour ne conserver que celles du second trimestre
carData = filter_second_quarter(carData)

# 2. Ecrire par marque, générer un fichier contenant la marque et le prix remisé pour les modèles du second trimestre


# pour chaque ligne ecrire dans un répertoire de la marque
for data in carData:
    brand = data[0]
    savePath = "C:\\data\\"+brand.split()[0] # Assuming brand is at index 0

    price = data[1] # Assuming price is at index 1
    # Créer le répertoire de la marque s'il n'existe pas  
    write_data_to_directory(carData, directory=savePath, filename="output.txt", marque=brand.split()[0])


   