from pymongo import MongoClient
from prettytable import PrettyTable
from FetchData import get_data_INSEE_code
import json

# Connexion à la base de données
def connect_to_mongo():
    try:
        client = MongoClient('mongodb://root:root@localhost:27017')
        return client
    except Exception as e:
        print(f"Erreur lors de la connexion à MongoDB : {e}")
        return None

# Création de la base de données ainsi que la collection
def create_database_and_collection(client):
    db = client.HelloWork
    collection_name = "travail"

    if collection_name not in db.list_collection_names():
        db.create_collection(collection_name)
        print(f"Collection '{collection_name}' créée dans la base de données 'HelloWork'.")
    else:
        print(f"Collection '{collection_name}' déjà existante dans la base de données 'HelloWork'.")

# Insertion des données fetch de FetchData.py dans la collection Travail
def store_data_in_mongo(client, data, city):
    db = client.HelloWork
    collection = db.travail

    if 'resultats' not in data:
        print(f"Aucune offre d'emploi trouvée pour la ville de {city}")
        return

    offers = data['resultats']
    existing_offers = {offer['reference_annonce']: offer for offer in collection.find({"ville": city})}

    # Insertion ou mise à jour des offres
    for offer in offers:
        reference_annonce = offer.get("id", "")
        if reference_annonce in existing_offers:
            print(f"Offre déjà présente pour {city} : {reference_annonce}")
            # Vous pouvez mettre à jour l'offre existante si nécessaire
        else:
            offer_data = {
                "titre": offer.get("intitule", ""),
                "description": offer.get("description", ""),
                "url_postulation": offer.get("contact", {}).get("urlPostulation", ""),
                "salaire": offer.get("salaire", {}).get("libelle", ""),
                "reference_annonce": reference_annonce,
                "ville": city,
                "type_contrat": offer.get("typeContrat", ""),
                "entreprise_nom": offer.get("entreprise", {}).get("nom", "")
            }
            try:
                collection.insert_one(offer_data)
                print(f"Document inséré pour {city} : {offer_data}")
            except Exception as e:
                print(f"Erreur lors de l'insertion du document pour {city} : {e}")

    # Suppression des offres qui ne sont plus présentes
    current_references = {offer.get("id", "") for offer in offers}
    for ref_annonce, existing_offer in existing_offers.items():
        if ref_annonce not in current_references:
            try:
                collection.delete_one({"reference_annonce": ref_annonce})
                print(f"Document supprimé pour {city} : {ref_annonce}")
            except Exception as e:
                print(f"Erreur lors de la suppression du document pour {city} : {e}")

# Permet la récupération des données de FetchData et insert dans la base pour les 3 villes
def search_job_offers():
    client = connect_to_mongo()
    if client:
        insee_codes = {"Bordeaux": "33063", "Paris": "75056", "Rennes": "35238"}

        for city, code in insee_codes.items():
            print(f"Récupération des données pour {city} (INSEE: {code})")
            data = get_data_INSEE_code(code)
            if data:
                store_data_in_mongo(client, data, city)
            else:
                print(f"Pas de données récupérées pour {city}")

    print("\n=== Rechercher les offres d'emploi ===")
    print("Collecte des offres d'emploi terminée.")

# Récupération des offres stockées dans la base en fonction de la ville choisie
def search_offers_by_city(client, city):
    db = client.HelloWork
    collection = db.travail

    try:
        results = collection.find({"ville": city})
        offers = list(results)

        if offers:
            table = PrettyTable()
            table.field_names = ["Référence", "Titre", "Salaire", "Entreprise", "Type Contrat"]

            for index, offer in enumerate(offers, start=1):
                table.add_row([offer.get("reference_annonce"), offer.get("titre"), offer.get("salaire"), offer.get("entreprise_nom"), offer.get("type_contrat")])

            print(table)
        else:
            print(f"Aucune offre trouvée pour la ville '{city}'.")

        return offers
    except Exception as e:
        print(f"Erreur lors de la recherche des offres pour la ville '{city}' : {e}")
        return []

# Récupération de l'offre stockée dans la base en fonction de sa référence
def get_offer_by_reference(client, reference):
    db = client.HelloWork
    collection = db.travail

    try:
        offer = collection.find_one({"reference_annonce": reference})
        if offer:
            for key, value in offer.items():
                print(f"{key}: {value}")
        else:
            print(f"Aucune offre trouvée pour la référence '{reference}'.")

        return offer
    except Exception as e:
        print(f"Erreur lors de la recherche de l'offre pour la référence '{reference}' : {e}")
        return None

# Compte le nombre d'offres par ville
def count_offers_by_city(client):
    db = client.HelloWork
    collection = db.travail

    try:
        cities = ["Bordeaux", "Paris", "Rennes"]
        counts = {}
        for city in cities:
            count = collection.count_documents({"ville": city})
            counts[city] = count

        return counts
    except Exception as e:
        print(f"Erreur lors du comptage des offres par ville : {e}")
        return {}

# Compte le nombre d'entreprises récupérées
def count_companies(client):
    db = client.HelloWork
    collection = db.travail

    try:
        companies = collection.distinct("entreprise_nom")
        return len(companies)
    except Exception as e:
        print(f"Erreur lors du comptage des entreprises : {e}")
        return 0

# Répartition par type de contrat
def contract_distribution(client):
    db = client.HelloWork
    collection = db.travail

    try:
        pipeline = [
            {"$group": {"_id": "$type_contrat", "count": {"$sum": 1}}}
        ]
        distribution = collection.aggregate(pipeline)
        return {doc['_id']: doc['count'] for doc in distribution}
    except Exception as e:
        print(f"Erreur lors de la répartition par type de contrat : {e}")
        return {}

def show_statistics(client):
    while True:
        print("\n=== Statistiques ===")
        counts = count_offers_by_city(client)
        for city, count in counts.items():
            print(f"{city}: {count} offres disponibles")

        num_companies = count_companies(client)
        print(f"Nombre d'entreprises récupérées: {num_companies}")

        distribution = contract_distribution(client)
        print("Répartition par type de contrat:")
        for contract_type, count in distribution.items():
            print(f"{contract_type}: {count}")

        print("0. Retour au menu principal")
        choice = input("Veuillez sélectionner une option: ")
        if choice == '0':
            break
