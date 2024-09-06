import json

# Abre el archivo json y lee los datos
with open('jci_1994.json', 'r') as f:
    data = json.load(f)

# Ahora 'data' es un diccionario de Python que contiene los datos del archivo json
print(len(data))