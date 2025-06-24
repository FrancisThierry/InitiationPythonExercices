import socket
import json


def appendTofile(data, path="data.json"):
    with open(path, "a") as file:
        file.write(json.dumps(data) + "\n")
        print(f"Données ajoutées au fichier : {data}")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind(('localhost', 12345))
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
            # messageJson = json.loads(message)  
            # print(f"Message JSON reçu : {messageJson}")          
            
             
            print(f"Reçu du client : {message}")
            response = f"Message reçu : {message}"
            client_socket.sendall(response.encode())
            # appendTofile(messageJson, r"C:\data\exSocket.txt")           