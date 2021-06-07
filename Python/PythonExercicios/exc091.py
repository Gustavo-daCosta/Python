from random import randint
from time import sleep
from operator import itemgetter

cont = 0
data = dict()

print('Valores sorteados:')
for c in range(1, 5):
    random = randint(1, 6)
    data[f'jogador{c}'] = random
    print(f'        O jogador{c} tirou {random} no dado')
    sleep(0.5)
ranking = dict()
print('Ranking dos jogadores:')
ranking = sorted(data.items(), key=itemgetter(1), reverse=True)
for k, v in enumerate(ranking):
    print(f'    {k+1}° lugar: {v[0]} com {v[1]}')