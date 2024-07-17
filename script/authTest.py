from auth import get_access_token

def test_get_access_token():
    token = get_access_token()
    if token:
        print(f"Access Token: {token}")
    else:
        print("Échec de l'obtention de l'access token")

if __name__ == "__main__":
    test_get_access_token()
