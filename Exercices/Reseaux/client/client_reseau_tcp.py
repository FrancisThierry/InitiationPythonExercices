from client.base_client_reseau import BaseClientReseau


class ClientReseauTCP(BaseClientReseau):
    def __init__(self, host: str, port: int):
        super().__init__(host, port)
        self.__host = host
        self.__port = port

    def envoyer(self, message: str):
        import socket
        import json

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((self.__host, self.__port))
            print(f"Connecté au serveur {self.__host}:{self.__port}")

            # Convertir le message en JSON
            message_json = json.dumps(message)
            client_socket.sendall(message_json.encode())
            print(f"Message envoyé : {message_json}")

            # Recevoir la réponse du serveur
            response = client_socket.recv(1024).decode()
            print(f"Réponse du serveur : {response}")