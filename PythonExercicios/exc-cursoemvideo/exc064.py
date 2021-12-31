soma = 0
digitados = 0
n = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        soma += n
    digitados += 1
print('Programa finalizado.')
print(f'Total de números digitados: {digitados}')
print(f'Soma entre os números digitados: {soma}')