import http.client
import urllib.parse
import json

# Configuration
client_id = "PAR_testhellowork_7214b995c311b0f844f41203d71fadf0116afb0b222dc9c295a400348e431d7d"
client_secret = "5ea1869205294eb3ab195d0ad219ea8dbf4ea35c7e42c134a65faab3f26a6bc4"
scope = "o2dsoffre api_offresdemploiv2"

def get_access_token():
    conn = http.client.HTTPSConnection("entreprise.francetravail.fr")

    payload = urllib.parse.urlencode({
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
        "scope": scope
    })

    headers = {
        'Content-Type': "application/x-www-form-urlencoded"
    }

    conn.request("POST", "/connexion/oauth2/access_token?realm=%2Fpartenaire", payload, headers)
    res = conn.getresponse()
    data = res.read()

    if res.status == 200:
        token_response = json.loads(data.decode("utf-8"))
        return token_response["access_token"]
    else:
        print(f"Erreur {res.status} lors de la récupération du token : {data.decode('utf-8')}")
        return None

if __name__ == "__main__":
    token = get_access_token()
    if token:
        print(f"Access Token: {token}")
    else:
        print("Échec de l'obtention de l'access token")
