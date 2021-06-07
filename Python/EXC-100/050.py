from random import randint

acima5 = div3 = 0
print('Números sorteados:', end=' ')
for c in range(1, 11):
    num = randint(1, 10)
    print(num, end='')
    if c < 10:
        print(',', end=' ')
    if num > 5:
        acima5 += 1
    if num % 3 == 0:
        div3 += 1
print()
print(f'Total de números maiores que 5: {acima5}')
print(f'Total de números divisíveis por 3: {div3}')