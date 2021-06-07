num = []
for c in range(0, 10):
    num.append(float(input(f'Digite o {c+1}° valor: ')))
print('=-='*15)
print('Os valores digitados em ordem inversa são:')
num.sort(reverse=True)
for c in range(0, 10):
    print(f'O {c+1}° valor digitado foi: {num[c]}')