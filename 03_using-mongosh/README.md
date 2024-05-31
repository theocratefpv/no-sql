## Partie 1: Exploration des Bases de Données et Collections
Lister les Bases de Données :

Utilisez la commande show dbs pour afficher toutes les bases de données existantes.

```show dbs```  

Sélectionner une Base de Données :

Utilisez la commande use suivie du nom d'une base de données existante ou d'une nouvelle pour la sélectionner.   
Par exemple, pour sélectionner ou créer testDB :

```use testDB```

Créer une Collection :

Créez une nouvelle collection nommée testCollection.

```db.createCollection("testCollection")```

Afficher les Collections :

Utilisez la commande ```show collections``` pour lister toutes les collections de la base de données actuelle.

## Partie 2: Manipulation des Données
Insertion de Données :

```db.testCollection.insertOne({name: "test", value: 1})```

Lecture de Données :

Utilisez ```db.testCollection.find()``` pour afficher tous les documents dans testCollection.

```db.testCollection.find()```
Mise à Jour de Données :

Mettez à jour le document précédemment inséré en augmentant value de 1.

```db.testCollection.updateOne({name: "test"}, {$inc: {value: 1}})```

Suppression de Données :

Supprimez le document avec name: "test".

```db.testCollection.deleteOne({name: "test"})```

## Partie 3: Nettoyage
Suppression de Collection :

```db.testCollection.drop()```

Suppression de Base de Données :

Supprimez la base de données testDB (assurez-vous d'avoir sélectionné testDB).

```db.dropDatabase()```

Validation
Pour vérifier que vos actions ont été correctement exécutées, utilisez les commandes appropriées à chaque étape. Par exemple :

Après avoir inséré des données, utilisez ```db.testCollection.find()``` pour vérifier l'insertion.

Après avoir mis à jour des données, utilisez à nouveau ```b.testCollection.find()``` pour vérifier la mise à jour.  

Après avoir supprimé des données, utilisez ```db.testCollection.find()``` pour confirmer la suppression.

Utilisez show dbs et show collections pour vérifier les modifications apportées aux bases de données et aux collections.

En suivant ces étapes, vous serez en mesure de manipuler des bases de données et des collections dans MongoDB en utilisant mongosh.






