media = 0
menos20 = 0
velhonome = ' '
menos20 = 0
for c in range(1, 5):
    print(f'-----  {c}° PESSOA  -----')
    nome = str(input(f'Nome: ')).strip()
    idade = int(input(f'Idade: '))
    genero = str(input(f'Gênero [M/F]: ')).strip()
    media += idade
    if c == 1 and genero == 'M':
        velhoidade = idade
        velhonome = nome
    if genero == 'M' and idade > velhoidade:
        velhonome = nome
    if genero == 'F' and idade < 20:
        menos20 += 1
print(f'Média de idade do grupo: {media/4}')
print(f'Nome do homem mais velho do grupo: {velhonome}')
print(f'Mulheres com menos de 20 anos do grupo: {menos20}')