import json

with open('aula4/jogador.json') as f:
    jogador = json.load(f)

def linha():
    print('-----------------------------')

for c in jogador:
    print(c)
linha()

for i in jogador.items():
    print(i)
linha()

for v in jogador.values():
    print(v)
linha()

# Nome do jogador
print(jogador["time"])
linha()
# itens da mochila
for im in jogador["mochila"]:
    print(im)
linha()
for a in jogador["aeronaves"]:
    print(f'{a["tipo"]} - {a["habilidade"]}')
linha()