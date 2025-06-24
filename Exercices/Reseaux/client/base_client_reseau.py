class BaseClientReseau:
    def __init__(self, host: str, port: int):
        self.__host = host
        self.__port = port
    def envoyer(self, message: str):
        raise NotImplementedError("La méthode envoyer doit être implémentée dans la sous-classe.")
    
@property
def host(self):
    return self.__host
@property
def port(self):
    return self.__port
# les setter
@host.setter
def host(self, value: str):
    self.__host = value
    print(f"Hôte mis à jour : {self.__host}")
@port.setter
def port(self, value: int):
    self.__port = value
    print(f"Port mis à jour : {self.__port}")
        