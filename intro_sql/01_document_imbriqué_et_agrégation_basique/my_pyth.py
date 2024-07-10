from pymongo import MongoClient
import random
client = MongoClient('mongodb://localhost:27017/')
db = client.pokemonDB
collection = db.pokemonGO

for pokemon in collection.find():
    attack = random.randint(1, 100)
    defense = random.randint(1, 100)
    collection.update_one(
        {'_id': pokemon['_id']},
        {'$set': {'stats': {'attack': attack, 'defense': defense}}}
    )

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

highest_hp_pokemon = collection.find().sort('hp', -1).limit(1)[0]
highest_cp_pokemon = collection.find().sort('cp', -1).limit(1)[0]
print("Pokemon with highest HP:", highest_hp_pokemon['name'], highest_hp_pokemon['hp'])
print("Pokemon with highest CP:", highest_cp_pokemon['name'], highest_cp_pokemon['cp'])

pokemon_with_high_attack = collection.find({'stats.attack': {'$gt': 50}})
for pokemon in pokemon_with_high_attack:
    print(pokemon['name'], pokemon['stats']['attack'])

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

pokemon_above_avg_cp = collection.find({'cp': {'$gt': average_cp}})
for pokemon in pokemon_above_avg_cp:
    print(pokemon['name'], pokemon['cp'])

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


