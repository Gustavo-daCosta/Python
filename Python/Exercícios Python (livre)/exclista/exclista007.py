data, num, soma, multi = [], 0, 0, 0
for c in range(1, 6):
    num = int(input(f'Digite o {c}° valor: '))
    data.append(num)
    soma += num
    multi = multi*num
print('=-='*20)
print(f'Valores digitados: {data}')
print(f'Soma dos valores digitados: {soma}')
print(f'Multiplicação dos valores digitados: {multi}')