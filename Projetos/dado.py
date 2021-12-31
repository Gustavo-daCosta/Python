from random import randint
from time import sleep

while True:
    print('-'*50)
    print('SIMULADOR DE DADO'.center(50))
    print('-'*50)
    while True:
        opcao = str(input('Você deseja jogar o dado? [S/N]: '))
        if opcao in ('NnSs'):
            break
        else:
            print(f'ERRO! Digite S ou N para continuar.')
    if opcao in 'Nn':
        break
    print(f'Valor sorteado: {randint(1, 6)}')
print('Finalizando', end='', flush=True)
for c in range(0, 3):
    sleep(0.3)
    print('.', end='', flush=True)