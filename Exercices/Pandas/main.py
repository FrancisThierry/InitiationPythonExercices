import pandas as pd
import openpyxl
houses = pd.read_csv('./data/Californiahousing.csv')
allHouses = pd.read_csv('./data/Californiahousing.csv')

houses = houses.dropna()
print(houses.info())
print('afficher les 100 premières lignes')
print(houses.head(100))
print('afficher les 100 dernières lignes')
print(houses.tail(100))
print('afficher les valeurs uniques de la colonne population')
print(houses['population'].unique())

print('afficher population, households, total_rooms')
print(houses[['population', 'households', 'total_rooms']].head(100))

print('afficher le max de la colonne population, de households, total_rooms avec l\'entête indiquant max')
print(houses[['population', 'households', 'total_rooms']].max())

print('afficher le min de la colonne population, de households, total_rooms avec l\'entête indiquant min')
print(houses[['population', 'households', 'total_rooms']].min())

print('afficher la valeur moyenne de la colonne population, de households, total_rooms avec l\'entête indiquant max')
print(houses[['population', 'households', 'total_rooms']].mean())


print('afficher les population')
print(houses['population'].head(100))

print('afficher les population', 'households', 'total_rooms pour les populations entre 400000 et 600000')
print(houses[(houses['population'] > 400) & (houses['population'] < 600)][['population', 'households', 'total_rooms']].head(100))


print('afficher la première valeur de la colonne population')
print(houses['population'].iloc[0])

