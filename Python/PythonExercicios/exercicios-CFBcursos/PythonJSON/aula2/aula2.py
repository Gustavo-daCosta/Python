import json

carros_dictionary = {
    "marca": "honda",
    "modelo": "HRV",
    "cor": "prata"
}
# dictionary -> objeto JSON
carros_list = ['honda', 'volkswagen', 'ford', 'fiat', 'chevrolet']
# list -> objeto JSON
carros_tupla = ('honda', 'volkswagen', 'ford', 'fiat', 'chevrolet')
# tuple -> objeto JSON

# Converte o dicionário para JSON
carros_j = json.dumps(carros_dictionary, indent=4, separators=(': ', '='), sort_keys=True)

print(carros_j)