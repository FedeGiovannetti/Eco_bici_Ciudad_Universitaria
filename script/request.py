import requests
import os
import pandas

credenciales = {
    "client_id": os.getenv("CLIENT_ID"),
    "client_secret": os.getenv("CLIENT_SECRET")
}

link_api = 'https://apitransporte.buenosaires.gob.ar/ecobici/gbfs/stationStatus?'

response = requests.get(link_api, params=credenciales)

print(f"Status code: {response.status_code}")
print(response.text)

estaciones_status = response.json()

estaciones_status_df = pd.DataFrame(estaciones_status["data"])
estaciones_status_df = pd.json_normalize(estaciones_status_df['stations'])
estaciones_status_df

estaciones_status_df["station_id"] = estaciones_status_df["station_id"].astype(int) 


datos_filtrados = estaciones_status_df[(estaciones_status_df["station_id"] == 420) | (estaciones_status_df["station_id"] == 464)]

datos_filtrados.to_csv('data/stations.csv', index=False)
