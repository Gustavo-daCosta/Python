par = impar = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}° número: '))
    if num % 2 == 0:
        par += 1
    else:
        impar += 1
print(f'Total de números pares: {par}')
print(f'Total de números ímpares: {impar}')