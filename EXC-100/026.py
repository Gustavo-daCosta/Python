n1 = int(input('1° número: '))
n2 = int(input('2° número: '))
if n1 > n2:
    print(f'O 1° valor ({n1}) é maior que o 2° valor ({n2})')
elif n1 < n2:
    print(f'O 2° valor ({n2}) é maior que o 1° valor ({n1})')
else:
    print(f'Não existe valor maior, o 1° e o 2° valor são iguais.')