soma = 0
for c in range(1,501):
    if c % 2 != 0:
        if c % 3 == 0:
            print(f'O número {c} é ímpar e é multíplo de 3.')
            soma += c
print(f'A soma de todos os valores é: {soma}')