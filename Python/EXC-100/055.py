from random import randint

sort = randint(1, 10)
print(sort)
for c in range(3, -1, -1):
    num = int(input('Digite um número entre 1 e 10: '))
    if num == sort:
        print('Parábens! Você acertou o número sorteado.')
        break
    else:
        print(f'Você errou, restam {c} tentativas.')
    if c == 0:
        print('Acabaram as tentativas! Boa sorte na próxima.')
        break