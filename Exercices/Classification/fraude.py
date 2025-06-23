import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

df = pd.read_excel('data/fraude_file.xlsx')
df.dropna(inplace=True)
# on étudie le datafrrame
df.info()
df.describe()
print(df.head(5))

# on prépare le modele
# Séparer les caractéristiques (X) de la variable cible (y)
X = df[['Montant', 'Nb_Transactions_24h']]
y = df['Frauduleux']

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialiser le modèle de régression logistique
model = LogisticRegression()

# Entraîner le modèle sur l'ensemble d'entraînement
model.fit(X_train, y_train)



# Obtenir les coefficients du modèle
coef = model.coef_[0]
intercept = model.intercept_

# Faire des prédictions sur l'ensemble de test
y_pred = model.predict(X_test)

# Calculer le R2 score
# r2 = r2_score(y_test, y_pred)

# print(f"R2 score: {r2}")

# Créer un diagramme de dispersion
plt.figure(figsize=(10, 6))

# Afficher les points de ceux qui ont Non frauduleux
plt.scatter(X_test[y_test == 1]['Montant'], X_test[y_test == 1]['Nb_Transactions_24h'], color='red', label='frauduleux')

# Afficher les points de ceux qui ont Frauduleux
plt.scatter(X_test[y_test == 0]['Montant'], X_test[y_test == 0]['Nb_Transactions_24h'], color='green', label='Non Frauduleux')

# Ajouter une légende et des titres
plt.legend()
plt.title('Diagramme de Dispersion - Classification Binaire')
plt.xlabel('Montant de la Transaction')
plt.ylabel('NB de Transactions 24h')
plt.show()

