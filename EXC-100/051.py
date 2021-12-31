for c in range(1, 9):
    valor = float(input(f'Digite o valor do {c}° produto: R$'))
    if c == 1:
        maior = valor
        menor = valor
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
print(f'Maior valor: R${maior:.2f}')
print(f'Menor valor: R${menor:.2f}')