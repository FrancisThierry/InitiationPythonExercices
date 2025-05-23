# Exercice à partir du fichier car.txt
# Écrire par marque, générer un fichier contenant la marque et le prix remisé pour les modèles du second trimestre

from csv import DictReader, DictWriter
from datetime import date
from os.path import dirname, realpath, join as pathJoin


class Car():
    FIELD_NAMES = ["make", "reducedPrice"]

    def __init__(self, make: str, ecoBonus: float, price: float, creationDate: date):
        self.make = make
        self.ecoBonus = ecoBonus
        self.price = price
        self.creationDate = creationDate

    def is2ndQuarter(self) -> bool:
        month = self.creationDate.month
        return month >= 4 and month <= 6

    def getReducedPrice(self) -> float:
        return self.price * (1.0 - self.ecoBonus / 100.0)


def getCars(fileName: str) -> list[Car]:
    cars = []  # type: list[Car]

    with open(fileName) as csvFile:
        reader = DictReader(csvFile)

        for row in reader:
            car = Car(
                make=row["marque"],
                ecoBonus=float(row["bonus"]),
                price=float(row["prixHT"]),
                creationDate=date.fromisoformat(row["dateModele"])
            )
            cars.append(car)

    return cars


def writeCar(fullFilePath: str, car: Car, createNew: bool) -> None:
    with open(fullFilePath, "w" if createNew else "a") as csvFile:
        writer = DictWriter(csvFile, fieldnames=Car.FIELD_NAMES)

        if createNew:
            writer.writeheader()

        reducedPrice = car.getReducedPrice()
        writer.writerow({"make": car.make, "reducedPrice": reducedPrice})


def writeCars(cars: list[Car], outDir: str) -> None:
    makes = set()  # type: set[str]

    for car in cars:
        if not car.is2ndQuarter():
            continue

        make = car.make
        fullFilePath = pathJoin(outDir, make + ".csv")

        if make in makes:
            writeCar(fullFilePath, car, False)
            continue

        makes.add(make)
        writeCar(fullFilePath, car, True)


def main() -> None:
    scriptDir = dirname(realpath(__file__))
    srcFileName = pathJoin(scriptDir, "..", "carInput.txt")
    outDir = pathJoin(scriptDir, "output")

    try:
        cars = getCars(srcFileName)
        writeCars(cars, outDir)
        print("Done.")
    except:
        print("Something went wrong while writing the data. Try again tomorrow.")


if __name__ == "__main__":
    main()
