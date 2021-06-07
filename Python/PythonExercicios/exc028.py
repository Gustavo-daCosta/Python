import random
n = random.randint(0, 5)
resp = int(input('Digite um número entre 0 e 5: '))
if n == resp:
    print('Parabéns! Você acertou.')
else:
    print('Você errou :(')