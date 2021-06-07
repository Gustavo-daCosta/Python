from random import randint
print('=-='*20)
print('          PAR OU ÍMPAR')
random = randint(1, 10)
n, par_impar, vitorias = 0, ' ', 0
while True:
    print('=-='*20)
    n = int(input('Digite um número entre 1 e 10: '))
    par_impar = str(input('Par ou Ímpar? [P/I]: '))
    print('-'*60)
    if par_impar == 'P':
        if (n + random) % 2 == 0:
            vitorias += 1
            print(f'Você jogou {n} e o computador jogou {random}. Total: {n+random}')
            print('RESULTADO: PAR       Parabéns! Você venceu, vamos jogar novamente.')
        else:
            print(f'Você jogou {n} e o computador jogou {random}. Total:{n+random}')
            print('RESULTADO: ÍMPAR     Infelizmente você perdeu :(')
            print(f'Total de vitórias: {vitorias}')
            break
    else:
        if (n + random) % 2 != 0:
            vitorias += 1
            print(f'Você jogou {n} e o computador jogou {random}. Total:{n+random}')
            print('RESULTADO: ÍMPAR     Parabéns! Você venceu, vamos jogar novamente.')
        else:
            print(f'Você jogou {n} e o computador jogou {random}. Total: {n+random}')
            print('RESULTADO: PAR       Infelizmente você perdeu :(')
            print(f'Total de vitórias: {vitorias}')
            break