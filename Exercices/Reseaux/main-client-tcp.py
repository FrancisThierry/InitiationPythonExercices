# serveur.py
import threading
from client.client_reseau import ClientReseau
from serveur.serveur_reseau import ServeurReseau

def lancer_serveur():
    serveur = ServeurReseau(host='localhost', port=12345)
    serveur.save_path = "dataWithThread.json"  # Chemin du fichier de sauvegarde
    serveur.demarrer()  # Méthode qui lance le serveur et accepte les connexions

# Lancer le serveur dans un thread
serveur_thread = threading.Thread(target=lancer_serveur, daemon=True)
serveur_thread.start()

def envoyer_message(client, message):
    client.envoyer(message)

client = ClientReseau(host='localhost', port=12345)
threads = []
for i in range(5):  # Envoyer 5 messages dans des threads séparés
    message = '{"type": "test", "content": "Hello, World! ' + str(i) + '"}'
    t = threading.Thread(target=envoyer_message, args=(client, message))
    t.start()
    threads.append(t)

for t in threads:
    t.join()