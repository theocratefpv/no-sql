# Étape 1: Ajout de Statistiques Aléatoires

```
from pymongo import MongoClient
import random
```
# Connexion à MongoDB
```
client = MongoClient('mongodb://localhost:27017/')
db = client.pokemonDB
collection = db.pokemonGO
```

# Mise à jour des documents avec des statistiques aléatoires
```
for pokemon in collection.find():
    attack = random.randint(1, 100)
    defense = random.randint(1, 100)
    collection.update_one(
        {'_id': pokemon['_id']},
        {'$set': {'stats': {'attack': attack, 'defense': defense}}}
    )
```
## Étape 2: Agrégation des Statistiques HP et CP
### a - Calcul de la moyenne des HP et des CP pour l'ensemble des Pokémon
```
pipeline = [
    {
        '$group': {
            '_id': None,
            'averageHP': {'$avg': '$hp'},
            'averageCP': {'$avg': '$cp'}
        }
    }
]
result = list(collection.aggregate(pipeline))
print("Average HP:", result[0]['averageHP'])
print("Average CP:", result[0]['averageCP'])
```
### b - Calcul de la moyenne des HP et des CP par type
```
pipeline = [
    {'$unwind': '$type'},
    {
        '$group': {
            '_id': '$type',
            'averageHP': {'$avg': '$hp'},
            'averageCP': {'$avg': '$cp'}
        }
    }
]
result = list(collection.aggregate(pipeline))
for doc in result:
    print(f"Type: {doc['_id']}, Average HP: {doc['averageHP']}, Average CP: {doc['averageCP']}")
```
### c - Détermination du Pokémon ayant les HP et les CP les plus élevés
```
highest_hp_pokemon = collection.find().sort('hp', -1).limit(1)[0]
highest_cp_pokemon = collection.find().sort('cp', -1).limit(1)[0]
print("Pokemon with highest HP:", highest_hp_pokemon['name'], highest_hp_pokemon['hp'])
print("Pokemon with highest CP:", highest_cp_pokemon['name'], highest_cp_pokemon['cp'])
```
## Étape 3: Lecture de Données sur les Documents
### a - Identifier tous les Pokémon avec plus de 50 d'attaque
```
pokemon_with_high_attack = collection.find({'stats.attack': {'$gt': 50}})
for pokemon in pokemon_with_high_attack:
    print(pokemon['name'], pokemon['stats']['attack'])
```
### b - Sélectionner les Pokémon avec un CP supérieur à la moyenne des CP


**Calcul de la moyenne des CP**
```
pipeline = [
    {
        '$group': {
            '_id': None,
            'averageCP': {'$avg': '$cp'}
        }
    }
]
result = list(collection.aggregate(pipeline))
average_cp = result[0]['averageCP']
```
# Sélection des Pokémon avec CP supérieur à la moyenne
```
pokemon_above_avg_cp = collection.find({'cp': {'$gt': average_cp}})
for pokemon in pokemon_above_avg_cp:
    print(pokemon['name'], pokemon['cp'])
```
## Étape 4: Agrégation des Statistiques par Type
### a - Calcul de la moyenne des statistiques d'attaque et de défense pour chaque Pokémon
```
pipeline = [
    {
        '$project': {
            'name': 1,
            'averageAttack': {'$avg': '$stats.attack'},
            'averageDefense': {'$avg': '$stats.defense'}
        }
    }
]
result = list(collection.aggregate(pipeline))
for doc in result:
    print(f"Pokemon: {doc['name']}, Average Attack: {doc['averageAttack']}, Average Defense: {doc['averageDefense']}")
```
### b - Comparaison des statistiques moyennes d'attaque et de défense de chaque Pokémon groupé par type
```
pipeline = [
    {'$unwind': '$type'},
    {
        '$group': {
            '_id': '$type',
            'averageAttack': {'$avg': '$stats.attack'},
            'averageDefense': {'$avg': '$stats.defense'}
        }
    }
]
result = list(collection.aggregate(pipeline))
for doc in result:
    print(f"Type: {doc['_id']}, Average Attack: {doc['averageAttack']}, Average Defense: {doc['averageDefense']}")
```