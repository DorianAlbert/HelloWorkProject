import http.client
    #Call API
def get_data_INSEE_code(codeInsee):
    try:
        conn = http.client.HTTPSConnection("api.francetravail.io")

        headers = {
            'Authorization': "Bearer kQlloCw8Pi12LK2doh9VBKTvBxM",
            'Accept': "application/json"
        }

        conn.request("GET", "/partenaire/offresdemploi/v2/offres/search?commune=" + codeInsee, headers=headers)

        res = conn.getresponse()
        data = res.read()
        decoded_data = data.decode("utf-8")

        if not decoded_data:
            print(f"Aucune donnée reçue pour le code INSEE {codeInsee}")
            return None

        return decoded_data

    except ValueError as e:
        print(f"Oops, erreur lors de la récupération des données : {e}. Veuillez réessayer.")
        return None
    except Exception as e:
        print(f"Erreur inattendue : {e}")
        return None