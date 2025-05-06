from Exercices.PythonObjet.SecondHandCar.Garage.Garage import Garage
class Application:
    def __init__(self, name):
        self.name = name

    def run(self):
        print(f"Lancement de {self.name}...")

def main():
    app = Application("Programme de gestion de garage")
    app.run()

if __name__ == "__main__":
    main()

