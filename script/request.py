import requests
import os

credenciales = {
    "client_id": os.getenv("CLIENT_ID"),
    "client_secret": os.getenv("CLIENT_SECRET")
}

link_api = 'https://apitransporte.buenosaires.gob.ar/ecobici/gbfs/stationStatus?'

response = requests.get(link_api, params=credenciales)

print(f"Status code: {response.status_code}")
print(response.text)
