matriz = [[], [], []]
valor = pares = soma = maior = 0

for c in range(0, 3):
    for x in range(0, 3):
        valor = int(input(f'Digite um valor para [{c}, {x}]: '))
        if valor % 2 == 0:
            pares += valor
        matriz[c].append(valor)
        if x == 2:
            soma += valor
        if c == 1:
            maior = valor
            if valor > maior:
                maior = valor
print('=-='*25)
for c in range(0, 3):
    for x in range(0, 3):
        print(f'[ {matriz[c][x]} ]', end='')
    print()
print('=-='*25)
print(f'A soma dos valores pares é: {pares}')
print(f'A soma dos valores da terceira coluna é: {soma}')
print(f'O maior valor da segunda linha é: {maior}')