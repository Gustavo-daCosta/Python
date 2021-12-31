maior = Mjovem = homens = MediaH = cont = 0
opcao = 'S'
while True:
    cont += 1
    print(f'CADASTRO N°{cont}'.center(40, '-'))
    genero = str(input('Gênero: [M/F]: ')).strip()
    idade = int(input('Idade: '))
    if cont == 1:
        maior = idade
        if genero == 'F':
            Mjovem = idade
    if idade > maior:
        idade = maior
    if genero == 'F' and idade < Mjovem:
        Mjovem = idade
    if genero == 'M':
        homens += 1
        MediaH += idade
    if genero == 'F' and cont == 1:
        Mjovem == idade
    elif genero == 'F':
        if idade < Mjovem:
            Mjovem = idade
    while True:
        opcao = str(input('Deseja continuar? [S/N]: ')).upper()
        if opcao in 'SN':
            break
        else:
            print('ERRO! Digite uma opção válida.')
    if opcao == 'N':
        print('Finalizando...')
        break
print('-'*40)
print(f'''Maior idade lida: {maior} anos
Total de homens cadastrados: {homens} homens
Idade da mulher mais jovem: {Mjovem} anos
Média de idade dos homens: {MediaH/homens:.1f} anos''')