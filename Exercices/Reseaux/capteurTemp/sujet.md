# Exercice : Transmission de données de température via TCP et sockets en Python

## Objectif

Créer une application client-serveur en Python utilisant les sockets TCP pour transmettre des données de température au format JSON. Le serveur devra sauvegarder les données reçues soit dans un fichier, soit dans une base de données (au choix).

---

## Consignes

### 1. Côté Client

- Écrire un script Python qui :
    - Se connecte à un serveur via TCP (adresse et port à définir).
    - Génère ou saisit une température (par exemple, un nombre flottant).
    - Prépare un message JSON contenant la température et un identifiant de capteur.
    - Envoie ce message au serveur.

### 2. Côté Serveur

- Écrire un script Python qui :
    - Écoute sur un port TCP.
    - Accepte les connexions entrantes.
    - Reçoit les messages JSON envoyés par les clients.
    - Parse les données JSON pour extraire la température et l’identifiant.
    - Sauvegarde chaque donnée reçue :
        - soit dans un fichier texte (par exemple, `donnees.txt`), chaque ligne correspondant à une mesure,
        - soit dans une base de données SQLite (table avec au moins les colonnes : identifiant, température, timestamp).

---



## Exemple de message JSON

```json
{
    "capteur_id": "capteur_1",
    "temperature": 23.5
}
```

---

## Livrables

- `client.py`
- `serveur.py`
- Fichier de sauvegarde ou base de données
