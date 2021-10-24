import json

jogador_j = '{"nome": "Bruno", "time": "aviadores", "vivo": "True", "energia": 100, "mochila":["pederneira", "corda", "linha", "arame"], "aeronaves":[{"tipo": "transporte", "habilidade": 80}, {"tipo":"ataque", "habilidade": 100}, {"tipo": "reconhecimento", "habilidade": 50}]}'

jogador = json.loads(jogador_j)

for chave in jogador:
    print(chave)

# Items
for item in jogador.items():
    print(item)

# Valores
for valor in jogador.values():
    print(valor)

# Nome do jogador
print(jogador["time"])

# itens da mochila
for im in jogador["mochila"]:
    print(im)

for a in jogador["aeronaves"]:
    print(f'{a["tipo"]} - {a["habilidade"]}')