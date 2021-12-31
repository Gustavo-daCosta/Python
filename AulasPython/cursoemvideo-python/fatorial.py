import functions

num = int(input('Digite um valor: '))
fat = functions.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {functions.dobro(num)}')
print(f'O triplo de {num} é {functions.triplo(num)}')