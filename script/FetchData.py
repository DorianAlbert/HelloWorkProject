import http.client
import json
from auth import get_access_token

def get_data_INSEE_code(codeInsee):
    access_token = get_access_token()  # Obtenez l'access token
    if not access_token:
        print("Échec de l'obtention de l'access token")
        return None

    try:
        conn = http.client.HTTPSConnection("api.francetravail.io")

        headers = {
            'Authorization': f"Bearer {access_token}",
            'Accept': "application/json"
        }

        conn.request("GET", f"/partenaire/offresdemploi/v2/offres/search?commune={codeInsee}", headers=headers)

        res = conn.getresponse()
        data = res.read()
        decoded_data = data.decode("utf-8")

        if not decoded_data:
            print(f"Aucune donnée reçue pour le code INSEE {codeInsee}")
            return None

        return json.loads(decoded_data)

    except ValueError as e:
        print(f"Oops, erreur lors de la récupération des données : {e}. Veuillez réessayer.")
        return None
    except Exception as e:
        print(f"Erreur inattendue : {e}")
        return None

if __name__ == "__main__":
    codeInsee = "33063"  # Exemple pour Bordeaux
    data = get_data_INSEE_code(codeInsee)
    if data:
        print(json.dumps(data, indent=4, ensure_ascii=False))
    else:
        print("Pas de données récupérées.")
