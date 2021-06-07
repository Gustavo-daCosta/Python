n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1>n2:
    print(f'O 1° valor({n1}) é maior que o 2° valor({n2})')
elif n1<n2:
    print(f'O 2° valor({n2}) é maior que o 1° valor({n1})')
else:
    print(f'Os dois valores são iguais ({n1})')