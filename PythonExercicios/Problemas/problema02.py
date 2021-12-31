# Problema #2 - Chute o número
# Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e permite que o usuário chute um número até que o valor aleatório gerado no início do programa seja chutado corretamente.
# O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início do programa.

from random import randint

randomNUM = randint(1, 10)
jogador = ''

while True:
    while True:
        try:
            jogador = int(input('Digite um número entre 1 e 10: '))
        except:
            print('ERRO! Digite um valor válido.')
        finally:
            if isinstance(jogador, int) is True:
                if jogador >= 1 and jogador <= 10:
                    break
                elif (isinstance(jogador, str) is False):
                    print('ERRO! Digite um valor entre 1 e 10')
    if jogador > randomNUM:
        print('O número inserido é MAIOR que o número sorteado, tente novamente.')
    elif jogador < randomNUM:
        print('o número inserido é MENOR que o número sorteado, tente novamente.')
    else:
        print('Parábens! Você adivinhou o número sorteado.')
        break