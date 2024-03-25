import requests

def fetch_birds_data():
    url = "https://aves.ninjas.cl/api/birds"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error al obtener los datos de la API.")
        return None


birds_data = fetch_birds_data()
if birds_data:
    for bird in birds_data:
        print("Nombre en español:", bird["name"]["spanish"])
        print("Nombre en inglés:", bird["name"]["english"])
        print("Nombre en latín:", bird["name"]["latin"])
        print("URL de la imagen principal:", bird["images"]["main"])
        print()