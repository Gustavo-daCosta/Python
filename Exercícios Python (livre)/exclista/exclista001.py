num = []
for c in range(1, 6):
    num.append(int(input(f'Digite o {c}° valor: ')))
print('=-='*15)
for c in range(1, 6):
    print(f'O {c}° valor digitado foi: {num[c]}')