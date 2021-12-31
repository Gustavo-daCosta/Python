from random import randint
random = randint(0,10)
opcao = 11
tentativas = 1
while opcao != random:
    opcao = int(input('Digite um número entre 0 e 10: '))
    if opcao == random:
        print('Parabéns! Você acertou.')
        print(f'Quantidade de tentativas: {tentativas}')
    else:
        print('Você errou! Tente novamente.')
        tentativas += 1