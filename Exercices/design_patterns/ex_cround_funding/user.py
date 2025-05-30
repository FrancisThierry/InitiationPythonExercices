class User:
    def __init__(self, name: str, email: str = None):
        self.name = name
        self.email = email

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"User(name={self.name})"