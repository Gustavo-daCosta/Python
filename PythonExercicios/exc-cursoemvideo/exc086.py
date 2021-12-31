matriz = [[], [], []]

for c in range(0, 3):
    for x in range(0, 3):
        matriz[c].append(input(f'Digite um valor para [{c}, {x}]: '))
for c in range(0, 3):
    for x in range(0, 3):
        print(f'[ {matriz[c][x]} ]', end='')
    print()