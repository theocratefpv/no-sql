# MongoDB podman Setup Guide 📘

This guide provides detailed instructions for setting up a MongoDB database using podman. It covers everything from pulling the MongoDB podman image to creating databases and collections, as well as managing backup, restoration, and access control.

## Prerequisites 📋

- podman installed on your machine.
- Basic familiarity with terminal or command line operations.

## Step 1: Setup MongoDB Container 📦

### Create Data Directory

From your terminal, create a new directory to store MongoDB data:

    mkdir -p ~/mongodb/data

### Pull MongoDB podman Image

Pull the latest MongoDB image from podman Hub:

    podman pull mongo

### Run MongoDB Container

Run the MongoDB container, mapping the local data directory to the container's data directory:

    podman run --name mongodb_container -v ~/mongodb/data:/data/db -p 27017:27017 -d mongo

### Verify Container is Running

Check if the MongoDB container is running:

    podman ps

## Step 2: Connect to MongoDB Container 🔗

Connect to your MongoDB Atlas cluster from the container. Replace `<container_id>`, `<dbname>`, `<username>`, and `<password>` with your specific details:

    podman exec -it mongodb_container mongo "mongodb+srv://cluster0.7zv8v.mongodb.net/<dbname>" --username <username> --password <password>

## Step 3: Database and Collection Operations 🗄️

### Create Database and Collections

In the MongoDB shell:

    use Galaxies
    db.createCollection("Stars")
    db.createCollection("Planets")

### Insert Documents

Insert documents into the `Stars` and `Planets` collections:

    db.Stars.insertMany([
      { Name: "Sun", Type: "G-Type", Age: "4.6 Billion Years", DistanceFromEarth: "N/A" },
      // Add more stars
    ])
    db.Planets.insertMany([
      { Name: "Earth", Type: "Terrestrial", NumberOfMoons: 1, DistanceFromSun: "1 AU" },
      // Add more planets
    ])

### Create Indexes

Create indexes on the `Name` field for both collections:

    db.Stars.createIndex({ Name: 1 })
    db.Planets.createIndex({ Name: 1 })

## Step 4: Backup and Restore Data 💾

### Create Backup

    podman exec mongodb_container mongodump --archive=/data/db/GalaxiesBackup.gz --db Galaxies

### Delete Database

    db.dropDatabase()

### Restore Database

    podman exec mongodb_container mongorestore --archive=/data/db/GalaxiesBackup.gz --nsFrom='Galaxies.*' --nsTo='Galaxies_Restored.*'

## Step 5: Configure Role-Based Access Control 🔐

### Create New User

In the MongoDB shell connected to `Galaxies_Restored`:

    db.createUser({
      user: "newuser",
      pwd: "password",
      roles: [{ role: "readWrite", db: "Galaxies_Restored" }]
    })

### Verify Operations as New User

Connect with the new user credentials and test operations:

    mongo "mongodb://localhost:27017/Galaxies_Restored" --username newuser --password password

## Step 6: podman Compose and Automation Script 📜

### podman Compose File

Create a file named `podman-compose.yml`:

    version: '3.8'
    services:
      mongodb:
        image: mongo
        container_name: mongodb_container
        ports:
          - "27017:27017"
        volumes:
          - ./data:/data/db

### Shell Script

Create a shell script `setup.sh`:

    #!/bin/bash

    # Commands from Steps 1 to 3, add the missing commands from above here

Make the script executable and run it:

    chmod +x setup.sh
    ./setup.sh
