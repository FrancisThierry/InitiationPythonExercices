import socket
import time

class ClientReseau:
    def __init__(self, host, port):
        self.__host = host
        self.__port = port
        pass
    def envoyer(self, message):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.__host, self.__port))
            s.sendall(message.encode())
            data = s.recv(1024)
            time.sleep(1)  # Pause de 1 seconde entre les envois
            
            
    @property
    def host(self):
        return self.__host
    @property
    def port(self):
        return self.__port