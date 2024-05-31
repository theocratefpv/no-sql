# Exercices Avancés MongoDB avec la Base de Données Titanic
**Sommaire :**

[TOC]

## Exercice 1: Importation et Création de la Collection ⚗️


**Utilisez la commande suivante pour importer les données dans MongoDB :**

```mongoimport --db TitanicDB --collection Passengers --type csv --headerline --file /home/dionys/no-sql/02_advanced-queries.md/tested.csv```

## Exercice 2: Analyse des Données 📈

**Compter le nombre total de passagers :**
```
use TitanicDB;
db.Passengers.countDocuments({});
```
Réponse ➡️ 418
**Trouver combien de passagers ont survécu :**
```db.Passengers.countDocuments({ Survived: 1 });```
Réponse ➡️ 152

**Trouver le nombre de passagers femmes :**
```db.Passengers.countDocuments({ Sex: "female" });```
Réponse ➡️ 152
**Trouver le nombre de passagers avec au moins 3 enfants :**
```db.Passengers.countDocuments({ SibSp: { $gte: 3 } });```
Réponse ➡️ 11
## Exercice 3: Mise à Jour de Données ⤴️
Mettre à jour les documents où le port d'embarquement est manquant :
```
db.Passengers.updateMany(
  { Embarked: { $in: ["", null] } },
  { $set: { Embarked: "S" } }
);
```

**Ajouter un champ rescued pour les passagers ayant survécu :**
```
db.Passengers.updateMany(
  { Survived: 1 },
  { $set: { rescued: true } }
);
```

## Exercice 4: Requêtes Complexes 🧬
Sélectionner les noms des 10 passagers les plus jeunes :

```db.Passengers.find({}, { Name: 1, Age: 1 }).sort({ Age: 1 }).limit(10);```
  
  
<details>
  <summary>Réponse ➡️</summary>

```
[
  {
    _id: ObjectId('6659b9c314b64764f32a1625'),
    Name: 'Dean, Miss. Elizabeth Gladys Millvina""',
    Age: 0.17
  },
  {
    _id: ObjectId('6659b9c314b64764f32a158c'),
    Name: 'Danbom, Master. Gilbert Sigvard Emanuel',
    Age: 0.33
  },
  {
    _id: ObjectId('6659b9c314b64764f32a15dc'),
    Name: 'Peacock, Master. Alfred Edward',
    Age: 0.75
  },
  {
    _id: ObjectId('6659b9c314b64764f32a1611'),
    Name: 'Aks, Master. Philip Frank',
    Age: 0.83
  },
  {
    _id: ObjectId('6659b9c314b64764f32a15bd'),
    Name: 'West, Miss. Barbara J',
    Age: 0.92
  },
  {
    _id: ObjectId('6659b9c314b64764f32a15f4'),
    Name: 'Laroche, Miss. Louise',
    Age: 1
  },
  {
    _id: ObjectId('6659b9c314b64764f32a15d3'),
    Name: 'Klasen, Miss. Gertrud Emilia',
    Age: 1
  },
  {
    _id: ObjectId('6659b9c314b64764f32a1553'),
    Name: 'Sandstrom, Miss. Beatrice Irene',
    Age: 1
  },
  {
    _id: ObjectId('6659b9c314b64764f32a151c'),
    Name: 'Wells, Master. Ralph Lester',
    Age: 2
  },
  {
    _id: ObjectId('6659b9c314b64764f32a15df'),
    Name: 'Rosblom, Miss. Salli Helena',
    Age: 2
  }
]
```

</details>
    
  
  
Identifier les passagers qui n'ont pas survécu et qui étaient dans la 2e classe :

```
db.Passengers.find(
  { Survived: 0, Pclass: 2 },
  { Name: 1, Pclass: 1, Survived: 1 }
);
```

<details>
  <summary>Réponse ➡️</summary>

```
[
  {
    _id: ObjectId('6659b9c314b64764f32a14ce'),
    Survived: 0,
    Pclass: 2,
    Name: 'Myles, Mr. Thomas Francis'
  },
  {
    _id: ObjectId('6659b9c314b64764f32a14d3'),
    Survived: 0,
    Pclass: 2,
    Name: 'Caldwell, Mr. Albert Francis'
  },
  {
    _id: ObjectId('6659b9c314b64764f32a14d9'),
    Survived: 0,
    Pclass: 2,
    Name: 'Howard, Mr. Benjamin'
  },
  {
    _id: ObjectId('6659b9c314b64764f32a14dc'),
    Survived: 0,
    Pclass: 2,
    Name: 'Keane, Mr. Daniel'
  },
  {
    _id: ObjectId('6659b9c314b64764f32a14ea'),
    Survived: 0,
    Pclass: 2,
    Name: 'Louch, Mr. Charles Alexander'
  },
  {
    _id: ObjectId('6659b9c314b64764f32a14eb'),
    Survived: 0,
    Pclass: 2,
    Name: 'Jefferys, Mr. Clifford Thomas'
  },
  {
    _id: ObjectId('6659b9c314b64764f32a14f6'),
    Survived: 0,
    Pclass: 2,
    Name: 'Pulbaum, Mr. Franz'
  },
  {
    _id: ObjectId('6659b9c314b64764f32a14f9'),
    Survived: 0,
    Pclass: 2,
    Name: 'Mangiavacchi, Mr. Serafino Emilio'
  },
  {
    _id: ObjectId('6659b9c314b64764f32a1500'),
    Survived: 0,
    Pclass: 2,
    Name: 'McCrae, Mr. Arthur Gordon'
  },
  {
    _id: ObjectId('6659b9c314b64764f32a151c'),
    Survived: 0,
    Pclass: 2,
    Name: 'Wells, Master. Ralph Lester'
  },
  {
    _id: ObjectId('6659b9c314b64764f32a1528'),
    Survived: 0,
    Pclass: 2,
    Name: 'Weisz, Mr. Leopold'
  },
  {
    _id: ObjectId('6659b9c314b64764f32a152c'),
    Survived: 0,
    Pclass: 2,
    Name: 'Aldworth, Mr. Charles Augustus'
  },
  {
    _id: ObjectId('6659b9c314b64764f32a1532'),
    Survived: 0,
    Pclass: 2,
    Name: 'Lamb, Mr. John Joseph'
  },
  {
    _id: ObjectId('6659b9c314b64764f32a1539'),
    Survived: 0,
    Pclass: 2,
    Name: 'Swane, Mr. George'
  },
  {
    _id: ObjectId('6659b9c314b64764f32a153a'),
    Survived: 0,
    Pclass: 2,
    Name: 'Stanton, Mr. Samuel Ward'
  },
  {
    _id: ObjectId('6659b9c314b64764f32a1543'),
    Survived: 0,
    Pclass: 2,
    Name: 'Bowenur, Mr. Solomon'
  },
  {
    _id: ObjectId('6659b9c314b64764f32a154c'),
    Survived: 0,
    Pclass: 2,
    Name: 'Schmidt, Mr. August'
  },
  {
    _id: ObjectId('6659b9c314b64764f32a155b'),
    Survived: 0,
    Pclass: 2,
    Name: 'Beauchamp, Mr. Henry James'
  },
  {
    _id: ObjectId('6659b9c314b64764f32a1561'),
    Survived: 0,
    Pclass: 2,
    Name: 'Lahtinen, Rev. William'
  },
  {
    _id: ObjectId('6659b9c314b64764f32a1567'),
    Survived: 0,
    Pclass: 2,
    Name: 'Peruschitz, Rev. Joseph Maria'
  }
]
```

</details>

## Exercice 5: Suppression de Données 🗑️

Supprimer les enregistrements des passagers qui n'ont pas survécu et dont l'âge est inconnu :

```db.Passengers.deleteMany({ Survived: 0, Age: { $in: ["", null] } });```
## Exercice 6: Mise à Jour en Masse 🔄

Augmenter l'âge de tous les passagers de 1 an :
```
# Idée de base mais incorrect ❌
db.Passengers.updateMany(
  { Age: { $ne: null } },
  { $inc: { Age: 1 } }
);

# Convertir en int des str ✅
db.Passengers.aggregate([
  {
    $project: {
      Age: {
        $convert: {
          input: "$Age",
          to: "double",
          onError: null,  // Si la conversion échoue, mettez à null
          onNull: null   // Si la valeur est null, restez null
        }
      }
    }
  },
  {
    $merge: {
      into: "Passengers",
      whenMatched: "merge",
      whenNotMatched: "discard"
    }
  }
]);
```
## Exercice 7: Suppression Conditionnelle ♻️

Supprimer les documents où le champ Ticket est absent ou vide :

```db.Passengers.deleteMany({ $or: [{ Ticket: "" }, { Ticket: { $exists: false } }] });```

Bonus: Utiliser les REGEX

**Utiliser une regex pour trouver tous les passagers portant le titre de Dr :**

```
db.Passengers.find(
  { Name: { $regex: "Dr\\.", $options: "i" } },
  { Name: 1 }
);
```

Réponse ➡️
```
[
  {
    _id: ObjectId('6659b9c314b64764f32a15f1'),
    Name: 'Dodge, Dr. Washington'
  }
]
```