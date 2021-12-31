mulheres = h100 = medF = maiorH = 0

for c in range(1, 9):
    print(f'CADASTRO {c}'.center(50, '-'))
    genero = str(input('Gênero: [M/F]: ')).upper()
    peso = int(input('Peso: '))
    if genero == 'F':
        mulheres += 1
        medF += peso
    if genero == 'M':
        if c == 1:
            maiorH = peso
        else:
            if peso > maiorH:
                maiorH = peso
        if peso > 100:
            h100 += 1
print('-'*50)
print(f'''Total de mulheres cadastradas: {mulheres} mulheres
Homens com mais de 100Kg: {h100} homens
Média de peso entre as mulheres: {medF/8:.1f}Kg
Maior peso entre os homens: {maiorH}Kg''')