import requests
import os
import pandas as pd
from datetime import datetime
import pytz

# Define your timezone
timezone = pytz.timezone('America/Argentina/Buenos_Aires')
now = datetime.now(timezone)

## Seteo el path

data_dir = os.path.join(os.getcwd(), 'data')  # Absolute path to 'data' folder
os.makedirs(data_dir, exist_ok=True)

# Credenciales BA que estan en secrets

credenciales = {
    "client_id": os.getenv("CLIENT_ID"),
    "client_secret": os.getenv("CLIENT_SECRET")
}


# Hago el request

link_api = 'https://apitransporte.buenosaires.gob.ar/ecobici/gbfs/stationStatus?'

response = requests.get(link_api, params=credenciales)

print(f"Status code: {response.status_code}")
print(response.text)

# Armo el dataset con los nuevos datos

estaciones_status = response.json()

estaciones_status_df = pd.DataFrame(estaciones_status["data"])
estaciones_status_df = pd.json_normalize(estaciones_status_df['stations'])
estaciones_status_df

estaciones_status_df["station_id"] = estaciones_status_df["station_id"].astype(int) 


datos_filtrados = estaciones_status_df[(estaciones_status_df["station_id"] == 420) | (estaciones_status_df["station_id"] == 464)]


# Le agrego la fecha

hoy = now.strftime('%Y-%m-%d')
ahora = now.strftime('%H:%M:%S')
dia = now().now.strftime('%A')

datos_filtrados["Date"] = hoy
datos_filtrados["hora"] = ahora
datos_filtrados["dia"] = dia


# Cargo datos anteriores

csv_file_path = os.path.join(data_dir, 'full_data.csv')

full_data = pd.read_csv(csv_file_path)

full_data = pd.concat([full_data, datos_filtrados], ignore_index=True)

full_data.to_csv(csv_file_path, index=False)

print(f"CSV saved to {csv_file_path}")
