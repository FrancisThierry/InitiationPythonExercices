import os

def write_data_to_directory(data_list, directory="données", filename="output.txt", marque=""):
    """
    Écrit les données dans un fichier situé dans un répertoire donné.

    :param data_list: Liste de tuples contenant les données (marque, prix).
    :param directory: Nom du répertoire où écrire les données.
    :param filename: Nom du fichier où écrire les données.
    """
    # Créer le répertoire s'il n'existe pas
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Construire le chemin complet du fichier
    file_path = os.path.join(directory, filename)

    # Écrire les données dans le fichier
    with open(file_path, "w", encoding="utf-8") as file:
        for data in data_list:
            if data[0].split()[0] == marque:
                # Écrire la marque et le prix dans le fichier
                file.write(f"{data[0]}, {data[1]}\n")

