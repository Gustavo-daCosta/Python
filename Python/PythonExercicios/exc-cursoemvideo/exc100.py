from random import randint

lista = list()

def sorteio(lista):
    for c in range(0, 5):
        lista.append(randint(1, 10))
    print('Sorteando 5 valores da lista:', end=' ')
    for c in range(0, 5):
        print(f'{lista[c]}', end=' ')
    print('PRONTO!')

def pares(a):
    par = 0
    print(f'Somando os valores pares de {a}', end='')
    for c in range(0, len(a)):
        if a[c] % 2 == 0:
            par += a[c]
    print(f', temos {par}')

sorteio(lista)
pares(lista)