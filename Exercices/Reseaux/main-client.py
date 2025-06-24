from client.client_reseau import ClientReseau

def main():
    # Démarrer le serveur

    # Créer un client et envoyer un message
    client = ClientReseau(host='localhost', port=12345)
    message = '{"type": "test", "content": "Hello, World!"}'
    # message = "test"
    
    # message = f'{{"capteur": "{capteur}", "temperature": {temp}}}'
    
    
    # for _ in range(5):  # Envoyer 5 messages
    client.envoyer(message)
main()