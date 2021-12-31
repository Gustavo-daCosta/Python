import json

jogador_j = '{"nome": "Bruno", "time": "aviadores", "vivo": "True", "energia": 100, "mochila":["pederneira", "corda", "linha", "arame"], "aeronaves":[{"tipo": "transporte", "habilidade": 80}, {"tipo":"ataque", habilidade": 100}, {"tipo": "reconhecimento", "habilidade": 50}]}'

jogador = json.loads(jogador_j)

print(jogador)