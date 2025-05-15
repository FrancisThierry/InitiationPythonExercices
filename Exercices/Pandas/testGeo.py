import sys
import os

# Ajoute le dossier racine du projet au sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from Exercices.Pandas.BusinessLogic.Geo import Geo
from Exercices.Pandas.BusinessLogic.Position import Position


myGeo = Geo()

start = Position(48.8566, 2.3522)  # Paris
end = Position(51.5074, -0.1278)  # London
distance = myGeo.distanceBetweenPositions(start, end)

print(f"Distance between Paris and London: {distance} km")
# The distance between Paris and London is approximately 343 kilometers (213 miles) as the crow flies.