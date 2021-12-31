cont, soma, p21, opcao = 0, 0, 0, 'S'

while opcao != 'N':
    cont += 1
    print(f'{cont}° CADASTRO'.center(40, '='))
    idade = int(input('Idade: '))
    soma += idade
    if idade >= 21:
        p21 += 1
    opcao = str(input('Deseja continuar? [S/N]: '))
print('RESULTADOS'.center(40, '='))
print(f'Foram digitadas {cont} idades ao todo.')
print(f'Média entre as idades digitadas: {soma/cont:.1f} anos')
print(f'Quantidade de pessoas com 21 anos ou mais: {p21} pessoas')