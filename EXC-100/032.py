from random import randint

random = randint(1, 5)
print('-'*40)
num = int(input('Digite um número inteiro entre 1 e 5: '))
print('-'*40)
if random == num:
    msg = 'Parábens! Você acertou o número sorteado.'
else:
    msg = 'Infelizmente você errou o número sorteado.'
print(f'Número sorteado: {random}       Número digitado: {num}')
print(msg)