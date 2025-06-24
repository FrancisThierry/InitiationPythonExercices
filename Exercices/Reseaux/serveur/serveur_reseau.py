import socket
import json
class ServeurReseau:
    def __init__(self,host, port, save_path="data.json"):
        self.__port = port
        self.__host = host  
        self.__save_path = save_path
        pass
    
    def appendTofile(data, path="data.json"):
        with open(path, "a") as file:
            file.write(json.dumps(data) + "\n")
            print(f"Données ajoutées au fichier : {data}")
    
    
    def demarrer(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.__host, self.__port))
            server_socket.listen()

            print("Serveur en attente de connexion...")

            while True:
                client_socket, addr = server_socket.accept()
                with client_socket:
                    print(f"Connexion de {addr}")
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    message = data.decode()
                    
                    # parser en json
                    messageJson = json.loads(message)  
                    print(f"Message JSON reçu : {messageJson}")     
                
                    print(f"Reçu du client : {message}")
                    response = f"Message reçu : {message}"
                    client_socket.sendall(response.encode())
                    self.appendTofile(messageJson, self.__save_path)
                
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