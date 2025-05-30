class Contact:
    __instance = None # Initialiser la variable de classe pour l'instance

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Contact, cls).__new__(cls)
            # L'initialisation doit être gérée ici ou dans __init__ avec une logique pour ne s'exécuter qu'une fois
        return cls.__instance

    def __init__(self, name=None, email=None, firstname=None):
        # Cette partie est délicate pour un singleton si vous voulez que les attributs
        # soient définis une seule fois.
        # Une approche est de ne les initialiser que si l'instance n'a pas déjà ces attributs.
        if not hasattr(self, '_Contact__name'): # Vérifie si l'attribut privé est déjà défini
            self.__name = name
            self.__firstname = firstname
            self.__email = email
        # elif name is not None and self.__name != name:
        #     # Si vous voulez permettre la modification des attributs sur l'instance existante
        #     # mais toujours via la "création" de l'instance
        #     self.__name = name
        #     self.__firstname = firstname
        #     self.__email = email


    def __str__(self):
        return f"Contact(name={self.name}, email={self.email})"

    def __repr__(self):
        return self.__str__()

    @property
    def name(self):
        return self.__name
    @property
    def firstname(self):
        return self.__firstname
    @property
    def email(self):
        return self.__email
    @name.setter
    def name(self, name):
        self.__name = name
    @firstname.setter
    def firstname(self, firstname):
        self.__firstname = firstname
    @email.setter
    def email(self, email):
        self.__email = email