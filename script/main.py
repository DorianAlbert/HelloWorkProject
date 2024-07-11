from BDD import create_database

def display_main_menu():
    print("\n=== Menu Principal ===")
    print("1. Rechercher les offres d'emploi")
    print("2. Statistique")
    print("3. Rechercher une offre")
    print("4. Quitter")

def search_job_offers():
    while True:
        print("\n=== Rechercher les offres d'emploi ===")
        print("Ici, vous pouvez implémenter la logique de recherche des offres d'emploi.")
        print("0. Retour au menu principal")
        choice = input("Veuillez sélectionner une option: ")
        if choice == '0':
            break

def show_statistics():
    while True:
        print("\n=== Statistiques ===")
        print("Ici, vous pouvez afficher les statistiques.")
        print("0. Retour au menu principal")
        choice = input("Veuillez sélectionner une option: ")
        if choice == '0':
            break

def search_offer():
    while True:
        print("\n=== Rechercher une offre ===")
        print("Ici, vous pouvez implémenter la logique de recherche d'une offre spécifique.")
        print("0. Retour au menu principal")
        choice = input("Veuillez sélectionner une option: ")
        if choice == '0':
            break

def main():
    while True:
        display_main_menu()
        choice = input("Veuillez sélectionner une option (1-4): ")

        if choice == '1':
            search_job_offers()
            result = create_database()
            print(result)  # Afficher le résultat de la création de la base de données
        elif choice == '2':
            show_statistics()
        elif choice == '3':
            search_offer()
        elif choice == '4':
            print("Au revoir!")
            break
        else:
            print("Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
