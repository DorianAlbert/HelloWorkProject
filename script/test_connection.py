from pymongo import MongoClient
#test de connection à la base de donnée
def connect_to_mongo():
    try:
        # Connexion à la base de données MongoDB
        client = MongoClient('mongodb://root:root@localhost:27017')

        # Vérification de la connexion
        db = client.admin
        server_status = db.command("serverStatus")
        print("Connexion réussie !")
        print("Version de MongoDB:", server_status["version"])

        # Accéder à la base de données 'HelloWork' et à la collection 'travail'
        hello_work_db = client.HelloWork
        travail_collection = hello_work_db.travail

        # Insérer un document exemple
        travail_collection.insert_one({"message": "Hello, MongoDB!"})
        print("Document inséré avec succès !")

        # Récupérer et afficher les documents de la collection
        for doc in travail_collection.find():
            print(doc)

    except Exception as e:
        print(f"Erreur lors de la connexion à MongoDB : {e}")

if __name__ == "__main__":
    connect_to_mongo()
