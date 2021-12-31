cont = 0
n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))
n4 = int(input('Digite o 4° número: '))
num = (n1, n2, n3, n4)
if (num.count(9)) >= 1:
    print(f'O número 9 aparace {num.count(9)} vez na lista.')
else:
    print('O número 9 não aparece na lista.')
if (num.count(3)) > 1:
    print(f'A primeira ocorrência do número 3 está na posição {num.index(3)} da lista.')
elif (num.count(3)) == 0:
    print('O número 3 não aparece na lista.')
else:
    print(f'O número 3 aparece unicamente na posição {num.index(3)} da lista.')
print('Os números pares digitados foram:', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')