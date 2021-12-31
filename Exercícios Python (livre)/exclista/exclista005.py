valores, num, par, impar = [], 0, [], []
for c in range(1, 21):
    num = (int(input(f'Digite o {c}° valor: ')))
    valores.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print('=-='*15)
print(f'Valores digitados: {valores}')
print(f'Valores PARES digitados: {par}')
print(f'Valores ÍMPARES digitados: {impar}')