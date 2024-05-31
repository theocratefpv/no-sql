# Introduction aux bases des données de type No-Sql (MongoDB)
**Sommaire :**

[TOC]

## Exercice 1 : Création d'une Base de Données et d'une Collection
Lancez **mongosh** pour démarrer le shell MongoDB.

```mongosh```

Créez une base de données nommée **PokemonDB**.  

```use PokemonDB```

Dans **PokemonDB**, créez une collection nommée **Pokemons**.

```db.createCollection("Pokemons")```

## Exercice 2 : Insertion de Données

### a - Consigne 📖
Préparez le fichier pokemonGO.csv pour l'importation. Vous pouvez utiliser l'outil mongoimport fourni avec MongoDB pour importer des fichiers CSV directement dans MongoDB.

### b - Execution 🚀

```
mongoimport --db PokemonDB --collection Pokemons --type csv --headerline --file pokemonGO.csv
--db PokemonDB # Nom de la base
--collection   #Pokemons spécifie la collection dans laquelle vous souhaitez importer les données.
--type csv     # indique que le fichier source est un CSV.
--headerline   # utilise la première ligne du CSV comme noms des champs.
```
**retour de la commande:**

```
[dionys@localhost 01_basic-queries]$ mongoimport --db PokemonDB --collection Pokemons --type csv --headerline --file /home/dionys/no-sql/01_basic-queries/pokemonGO.csv
2024-05-31T11:36:55.134+0200    connected to: mongodb://localhost/
2024-05-31T11:36:55.146+0200    151 document(s) imported successfully. 0 document(s) failed to import.
```

### c - Vérification ✅

Sélectionnez la base de données PokemonDB.

```use PokemonDB```  

Vérifiez les documents dans la collection Pokemons.

```db.Pokemons.find().pretty()```

**Retour de la commande (extrait) :**

```
PokemonDB> db.Pokemons.find().pretty()
[
  {
    _id: ObjectId('66599a37c718c0361e29b45d'),
    PokemonNo: 1,
    Name: 'Bulbasaur',
    Type1: 'Grass',
    Type2: 'Poison',
    MaxCP: 1079,
    MaxHP: 83,
    ImageURL: 'http://cdn.bulbagarden.net/upload/thumb/2/21/001Bulbasaur.png/250px-001Bulbasaur.png'
  },
  {
    _id: ObjectId('66599a37c718c0361e29b45e'),
    PokemonNo: 4,
    Name: 'Charmander',
    Type1: 'Fire',
    Type2: '',
    MaxCP: 962,
    MaxHP: 73,
    ImageURL: 'http://cdn.bulbagarden.net/upload/thumb/7/73/004Charmander.png/250px-004Charmander.png'
  }
]
```
## Exercice 3 : Lecture de Données
### a - Consigne 📖
Trouvez tous les Pokémon de type **Feu**.
Récupérez les informations du Pokémon nommé "Pikachu".
Commandes

### b - Execution 🚀

**Trouver tous les Pokémon de type Feu :**

```db.Pokemons.find({ Type: /Feu/ }).pretty()```

**Récupérer les informations du Pokémon nommé Pikachu**

```db.Pokemons.findOne({ Name: "Pikachu" })```

## Exercice 4 : Mise à Jour de Données
### a - Consigne :
Mettez à jour les points de combat de **Pikachu** pour qu'ils soient de 900.

### b - Execution 🚀

```
db.Pokemons.updateOne(
  { Name: "Pikachu" },
  { $set: { CP: 900 } }
)
```

## Exercice 5 : Suppression d'Éléments
### a - Consigne 📖

Supprimez le Pokémon **Bulbasaur** de la collection Pokemons.

### b - Execution 🚀
```db.Pokemons.deleteOne({ Name: "Bulbasaur" })```

### c - Vérification ✅
Après avoir complété chaque exercice, utilisez les commandes appropriées pour vérifier que vos opérations ont été réalisées correctement.

**Vérifier que les Pokémon de type Feu ont été trouvés**
```db.Pokemons.find({ Type: /Feu/ }).pretty()```

**Vérifier les informations de Pikachu**
```db.Pokemons.findOne({ Name: "Pikachu" })```

**Vérifier que les points de combat de Pikachu sont mis à jour**
```db.Pokemons.findOne({ Name: "Pikachu" })```

**Vérifier que "Bulbasaur" a été supprimé**

```db.Pokemons.findOne({ Name: "Bulbasaur" })```
