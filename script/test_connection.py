from pymongo import MongoClient

def test_connection():
    admin_username = "HelloWorks"
    admin_password = "HelloWorks"
    connection_url = f"mongodb://{admin_username}:{admin_password}@mongo:27017/"


    try:
        client = MongoClient(connection_url)
        # Essayer de lister les bases de données pour vérifier la connexion
        databases = client.list_database_names()
        print("Connexion réussie à MongoDB")
        print("Bases de données existantes : ", databases)
    except Exception as e:
        print("Erreur lors de la connexion à MongoDB : ", e)

if __name__ == "__main__":
    test_connection()
