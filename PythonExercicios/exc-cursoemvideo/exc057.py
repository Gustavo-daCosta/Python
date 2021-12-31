genero = ' '
while genero == ' ':
    genero = str(input('Digite o seu genêro [M/F]: ')).upper()
    if genero == 'M' or genero == 'F':
        print('Cadastro concluído.')
    else:
        print('Opcão Inválida.')
        genero = ' '