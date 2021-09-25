data, par, impar = [], [], []
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
par.sort()
impar.sort()
data.append(par)
data.append(impar)
print('=-='*25)
print(f'Os valores pares digitados foram: {data[0]}')
print(f'Os valores ímpares digitados foram: {data[1]}')