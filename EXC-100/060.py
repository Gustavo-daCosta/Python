maior = Fmenor = velha = Fnova = media = M30 = F18 = cont = 0
opcao = 'S'
while True:
    cont += 1
    print(f'CADASTRO N°{cont}'.center(40,'-'))
    nome = str(input('Nome: ')).capitalize()
    genero = str(input('Gênero: [M/F]: ')).upper()
    idade = int(input('Idade: '))
    media += idade
    if cont == 1:
        velha = idade
        maior = nome
        if genero == 'F':
            Fnova = idade
            Fmenor = nome
    else:
        if genero == 'F':
            Fnova = idade
            Fmenor = nome
        if idade > velha:
            velha = idade
            maior = nome
        if genero == 'F' and idade < Fmenor:
            Fmenor = idade
    if genero == 'M' and idade > 30:
        M30 += 1
    if genero == 'F' and idade < 18:
        F18 += 1
    while True:
        opcao = str(input('Deseja continuar? [S/N]: ')).lower()
        if opcao in 'sn':
            break
        else:
            print('ERRO! Digite uma opção válida.')
    if opcao in 'n':
        break
print('-'*40)
print(f'''Nome da pessoa mais velha: {maior}
Nome da mulher mais jovem: {Fmenor}
Média de idade do grupo: {media/cont:.2f} anos
Quantidade de homens com mais de 30 anos: {M30} homens
Quantidade de mulheres com menos de 18 anos: {F18} mulheres''')