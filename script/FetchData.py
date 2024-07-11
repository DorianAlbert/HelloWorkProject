import http.client

####
## function to get data by Insee code
###
def get_data_INSEE_code(codeInsee):
    try:
        conn = http.client.HTTPSConnection("api.francetravail.io")

        headers = {
            'Authorization': "Bearer n0ffcjcekOdgONiGOk42euKu3YU",
            'Accept': "application/json"
        }

        conn.request("GET", "/partenaire/offresdemploi/v2/offres/search?commune="+codeInsee+"", headers=headers)

        res = conn.getresponse()
        data = res.read()

        return(data.decode("utf-8"))

    except ValueError:
        print("Oops, Error to fetch data ! Please retry.")