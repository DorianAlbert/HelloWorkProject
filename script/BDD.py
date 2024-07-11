from pymongo import MongoClient

def create_database():
    # Connection Data
    admin_username = "HelloWorks"
    admin_password = "HelloWorks"
    database_name = "HelloWork"

    # Auth URL connection
    connection_url = f"mongodb://{admin_username}:{admin_password}@mongo:27017/"

    # Client
    client = MongoClient(connection_url)

    # create database
    db = client[database_name]

    # Collection
    collection_name = "work"
    try:
        db.create_collection(collection_name)
        return f"La base de données '{database_name}' a été créée avec la collection '{collection_name}'."
    except Exception as e:
        return f"Erreur lors de la création de la base de données : {e}"
