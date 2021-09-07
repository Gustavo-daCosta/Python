primeiro = int(input('Primeiro elemento: '))
razao = int(input('Razão: '))
ultimo = primeiro + (10-1)*razao
ultimo += 1

for c in range (primeiro, ultimo, razao):
    print(c, end=', ')
print('Fim')