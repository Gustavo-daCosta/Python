import json

carros = {
    "marca": "honda",
    "modelo": "HRV",
    "cor": "prata"
}

# Converte o dicionário para JSON
carros_json = json.dumps(carros)

print(carros_json)