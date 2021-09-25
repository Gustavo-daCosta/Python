from random import randint
from time import sleep

titulo, random, jogos, lista, cont = 'MEGA SENA', 0, 0, [], 0

print('-'*60)
print(f'{titulo:^60}')
print('-'*60)
jogos = int(input('Quantos jogos você quer sortear? '))
print(f'---------< SORTEANDO {jogos} JOGOS >---------')
for c in range(0, jogos):
    lista.append(0)
    while random in lista:
        random = randint(1, 61)
        lista.append(random)
        cont += 1
        if cont == 6:
            break
    random = cont = 0
    lista.remove(0)
    print(f'Jogo {c+1}: {lista}')
    lista.clear()
    sleep(0.3)
print(f'--------------< BOA SORTE! >--------------')