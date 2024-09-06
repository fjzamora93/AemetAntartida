
from dotenv import load_dotenv

import requests
import json
import os
load_dotenv()

API_KEY = os.getenv("API_KEY")

# ARCHIVO DE SALIDA
estacion_nombre = "jci"

for i in range (2024, 2025):
    año = str(i)
    print(f"\n\n\n ______________________ \nDescargando datos de {año}...")
    for i in range(1, 13):
        if i < 10:
            mes = f"0{i}"
        else:
            mes = str(i)
        
        # Fechas de inicio y fin de la solicitud
        ini = f"{año}-{mes}-01"
        fin = f"{año}-{mes}-31"

        print(f"Descargando datos de {ini} a {fin}...")
        
        estacion = 89064  # gabriel de castilla ///// 89064 # juan carlos I
        
        # URL de la solicitud inicial a la API
        url = f"https://opendata.aemet.es/opendata/api/antartida/datos/fechaini/{ini}T00%3A00%3A00UTC/fechafin/{fin}T00%3A00%3A00UTC/estacion/{estacion}"
        api_key = API_KEY  #deberia ir entre comillas?
        params = {
            "api_key": api_key
        }
        
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if 'datos' in data:
                url_datos = data['datos']
                response_datos = requests.get(url_datos)
                
                if response_datos.status_code == 200:
                    datos_reales = response_datos.json()
                    archivo = f"{estacion_nombre}_{año}.json"
                    
                    if os.path.exists(archivo):
                        with open(archivo, "r", encoding="utf-8") as json_file:
                            datos_existentes = json.load(json_file)
                        
                        if isinstance(datos_existentes, list) and isinstance(datos_reales, list):
                            datos_existentes.extend(datos_reales)
                            print(f"Número de registros del mes {mes}: ", len(datos_existentes))
                        else:
                            datos_existentes = datos_existentes + datos_reales
                            
                        
                        with open(archivo, "w", encoding="utf-8") as json_file:
                            json.dump(datos_existentes, json_file, ensure_ascii=False, indent=4)
                    else:
                        with open(archivo, "w", encoding="utf-8") as json_file:
                            json.dump(datos_reales, json_file, ensure_ascii=False, indent=4)
                    
                    print("Datos descargados y guardados con éxito.")
                else:
                    print(f"Error al obtener los datos: {response_datos.status_code}")
            else:
                print("La respuesta no contiene una URL de datos.")
        else:
            print(f"Error en la solicitud inicial: {response.status_code}")
        