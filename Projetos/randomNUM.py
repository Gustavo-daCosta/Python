from random import randint

aleat = randint(1, 10)
print('-'*50)
print('ADIVINHE O NÚMERO'.center(50))
print('-'*50)
while True:
    num = int(input('Digite um número entre 1 e 10: '))
    if num == aleat:
        print('Parábens, você acertou o número sorteado!')
        break
    else:
        print('Errou! Tente novamente.')