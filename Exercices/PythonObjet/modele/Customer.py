class Customer:
    def __init__(self, lastName, email, firstName=None):
        self.__firstName = firstName
        self.__lastName = lastName
        self.email = email
        self.__phone = None
        self.__address = None


    @property
    def firstName(self):
        return self.__firstName
    @property
    def lastName(self):
        return self.__lastName
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def name(self):
        return f"{self.__firstName} {self.__lastName}"


    def __str__(self):
        return f"Customer(name={self.name}, email={self.email})"