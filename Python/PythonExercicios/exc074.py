from random import randint
num = (randint(1, 1000), randint(1, 1000), randint(1, 1000), randint(1, 1000), randint(1, 1000))
menor, maior = num[1], num[1]
cont, n = 0, 0
while cont != 5:
    if num[cont] > maior:
        maior = num[cont]
    if num[cont] < menor:
        menor = num[cont]
    cont += 1
print('Os números sorteados foram: ', end='')
cont = 0
while cont != 5:
    print(num[cont], end=' ')
    cont += 1
print('')
print(f'O menor valor sorteado foi: {menor}')
print(f'O maior valor digitado foi: {maior}')