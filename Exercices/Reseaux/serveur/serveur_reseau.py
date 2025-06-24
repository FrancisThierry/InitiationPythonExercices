import socket
import json
import threading

class ServeurReseau:
    def __init__(self, host, port, save_path="data.json"):
        self.__port = port
        self.__host = host
        self.__save_path = save_path

    @staticmethod
    def appendTofile(data, path="data.json"):
        with open(path, "a") as file:
            file.write(json.dumps(data) + "\n")
            print(f"Données ajoutées au fichier : {data}")

    def handle_client(self, client_socket, addr):
        with client_socket:
            print(f"Connexion de {addr}")
            data = client_socket.recv(1024)
            if not data:
                return
            message = data.decode()
            try:
                messageJson = json.loads(message)
                print(f"Message JSON reçu : {messageJson}")
            except json.JSONDecodeError:
                print("Erreur de décodage JSON")
                messageJson = None

            print(f"Reçu du client : {message}")
            response = f"Message reçu : {message}"
            client_socket.sendall(response.encode())
            if messageJson is not None:
                thread = threading.Thread(target=self.appendTofile, args=(messageJson, self.__save_path))
                thread.daemon = True
                thread.start()

    def demarrer(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.__host, self.__port))
            server_socket.listen()
            print("Serveur en attente de connexion...")

            while True:
                client_socket, addr = server_socket.accept()
                thread = threading.Thread(target=self.handle_client, args=(client_socket, addr))
                thread.daemon = True
                thread.start()

    @property
    def port(self):
        return self.__port

    @property
    def host(self):
        return self.__host

    @property
    def save_path(self):
        return self.__save_path

    @save_path.setter
    def save_path(self, value):
        self.__save_path = value
        print(f"Chemin de sauvegarde mis à jour : {self.__save_path}")