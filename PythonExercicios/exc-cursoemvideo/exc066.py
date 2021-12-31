n, valores, soma = 0, 0, 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    valores += 1
    soma += n
print(f'A soma dos {valores} valores foi {soma}')