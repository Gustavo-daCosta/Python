idade,cont, genero, opcao, maior, homens, mulheres20, pessoa = 0, 0, ' ', 'S', 0, 0, 0, ' '
while True:
    cont += 1
    pessoa = (f'{cont}° PESSOA')
    print(f'{pessoa:-^50}')
    idade = int(input(f'Digite a idade da {cont}° pessoa: '))
    genero = str(input(f'Digite o gênero da {cont}° pessoa [M/F]: ')).upper()
    if idade >= 18:
        maior += 1
    if genero == 'M':
        homens += 1
    if genero == 'F' and idade < 20:
        mulheres20 += 1
    print('-'*44)
    opcao = str(input('Você deseja continuar? [S/N]: ')).upper()
    if opcao == 'N':
        break
        print('======= PROGRAMA ENCERRADO =======')
print(f'Total de pessoas cadastradas: {cont} pessoas')
print(f'Total de pessoas maiores de idade: {maior} pessoas')
print(f'Total de homens cadastrados: {homens} pessoas')
print(f'Total de mulheres com menos de 20 anos cadastradas: {mulheres20}')