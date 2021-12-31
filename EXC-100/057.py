salarioHomens, salarioMulheres, cont, opcao = 0, 0, 0, 'S'
while True:
    cont += 1
    print(f'{cont}° CADASTRO'.center(40, '-'))
    salario = float(input('Salário: R$'))
    genero = str(input('Gênero: [M/F]: ')).upper()
    if genero == 'M':
        salarioHomens += salario
    else:
        salarioMulheres += salario
    while True:
        opcao = str(input('Deseja continuar? [S/N]: ')).lower()
        if opcao in 'sn':
            break
        else:
            print('ERRO! Digite uma opção válida.')
    if opcao == 'n':
        print('Encerrando...')
        break
print('-'*40)
print(f'Total de salário pago: R${salarioHomens+salarioMulheres:.2f}')
print(f'Salário total pago aos homens: R${salarioHomens:.2f}')
print(f'Salário total pago as mulheres: R${salarioMulheres:.2f}')