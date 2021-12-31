homens = mulheres = soma = medhomem = mulheres20 = 0

for c in range(1, 6):
    print(f'{c}° PESSOA'.center(40, '-'))
    while True:
        genero = str(input('Gênero: [M/F] ')).lower()
        if genero not in 'MFmf':
            print('ERRO! Digite uma opção válida.')
        else:
            break
    idade = int(input('Idade: '))
    if genero in 'Mm':
        homens += 1
        medhomem += idade
    else:
        mulheres += 1
    soma += idade
    if c == 1:
        maior = idade
    if idade > maior:
        maior = idade
    if genero == 'f' and idade > 20:
        mulheres20 += 1
print('-'*40)
print(f'''Total de homens cadastrados: {homens} homens
Total de mulheres cadastradas: {mulheres} mulheres
Média de idade do grupo: {soma/5:.1f} anos
Média de idade dos homens: {medhomem/homens:.1f} anos
Mulheres com mais de 20 anos: {mulheres20} mulheres''')