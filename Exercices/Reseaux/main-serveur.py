from client.client_reseau import ClientReseau
from serveur.serveur_reseau import ServeurReseau

def main():
    # Démarrer le serveur
    serveur = ServeurReseau("localhost", 12345)  # Port du serveur
    serveur.save_path = r"c:\data\data.json"  # Chemin de sauvegarde des données
    serveur.demarrer()

  
main()