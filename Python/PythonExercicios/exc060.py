n = int(input('Digite o número que você deseja saber o fatorial: '))
fatorial = 1
while n-1 != 0:
    fatorial *= n
    print(fatorial)
    n -= 1
print(f'O fatorial do número {n} é {fatorial}')