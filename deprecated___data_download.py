
#! DEPRECATED USAR EL OTRO ARCHIVO

import requests
import json
import os

#TODO: EMPEZAR EN EL 89? - Hasta 2024
#TODO: PROBAR SACAR DATOS DE FORMA SIMULTANEA
#TODO CONVERTIR LOS DATOS A CSV

# URL del archivo JSON y donde se guardará
url = "https://opendata.aemet.es/opendata/sh/86e6314f_202409052226_json"
archivo_json = "archivo_aemet_2008.json"

with open(archivo_json, "r", encoding="utf-8") as json_file:
    existing_data = json.load(json_file)

# Realizar la solicitud HTTP GET
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    existing_data.extend(data)  
    
    # Guardar los datos actualizados en el archivo
    with open(archivo_json, "w", encoding="utf-8") as json_file:
        json.dump(existing_data, json_file, ensure_ascii=False, indent=4)
    
    print("Archivo JSON actualizado con éxito.")
else:
    print(f"Error al descargar el archivo: {response.status_code}")
