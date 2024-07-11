from BDD import connect_to_mongo, create_database_and_collection, search_job_offers, search_offers_by_city, get_offer_by_reference, count_offers_by_city, count_companies, contract_distribution

def display_main_menu():
    print("\n=== Menu Principal ===")
    print("1. Rechercher les offres d'emploi")
    print("2. Statistiques")
    print("3. Rechercher une offre")
    print("4. Quitter")

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

def search_offer():
    client = connect_to_mongo()

    while True:
        print("\n=== Rechercher une offre ===")
        reference = input("Veuillez entrer la référence de l'offre (ou '0' pour retourner au menu principal): ")
        if reference == '0':
            break
        else:
            get_offer_by_reference(client, reference)

def choose_city(client):
    while True:
        print("\n=== Choisissez une ville ===")
        print("1. Bordeaux")
        print("2. Paris")
        print("3. Rennes")
        print("0. Retour au menu principal")
        choice = input("Veuillez sélectionner une option: ")

        if choice == '1':
            print("Vous avez choisi Bordeaux")
            offers = search_offers_by_city(client, "Bordeaux")
            if not offers:
                print("Aucune offre disponible pour Bordeaux. Veuillez choisir une autre ville.")
                continue
            search_offer()
            break
        elif choice == '2':
            print("Vous avez choisi Paris")
            offers = search_offers_by_city(client, "Paris")
            if not offers:
                print("Aucune offre disponible pour Paris. Veuillez choisir une autre ville.")
                continue
            search_offer()
            break
        elif choice == '3':
            print("Vous avez choisi Rennes")
            offers = search_offers_by_city(client, "Rennes")
            if not offers:
                print("Aucune offre disponible pour Rennes. Veuillez choisir une autre ville.")
                continue
            search_offer()
            break
        elif choice == '0':
            break
        else:
            print("Option invalide, veuillez réessayer.")

def main():
    client = connect_to_mongo()
    if client:
        create_database_and_collection(client)

    while True:
        display_main_menu()
        choice = input("Veuillez sélectionner une option (1-4): ")

        if choice == '1':
            search_job_offers()
            choose_city(client)  # Demander à l'utilisateur de choisir une ville après la collecte des offres d'emploi
        elif choice == '2':
            show_statistics(client)
        elif choice == '3':
            search_offer()
        elif choice == '4':
            print("Au revoir!")
            break
        else:
            print("Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
