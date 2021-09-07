num = int(input('Digite um número: '))
print(f'TABUADA DO NÚMERO {num}'.center(30, '-'))
for c in range(1, 11):
    print(f'\t{num} x {c} = {num*c}')