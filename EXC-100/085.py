nome, genero, salario = list(), list(), list()
varnome = vargenero = varsalario = 0

for c in range(0, 5):
    print(f'{c+1}° CADASTRO'.center(60, '-'))

    # VERIFICAR NOME
    while True:
        varnome = str(input('Nome: '))
        try:
            varnome = int(varnome)
            print('ERRO! Digite um nome válido.')
        except:
            pass
        try:
            if isinstance(varnome, int) is False:
                varnome = float(varnome)
                print('ERRO! Digite um nome válido.')
            else:
                pass
        except:
            pass
        if isinstance(varnome, str) is True:
            break
    
    # VERIFICAR GÊNERO
    while True:
        vargenero = str(input('Digite o seu gênero [M/F]: '))
        try:
            vargenero = int(vargenero)
            print('ERRO! Digite um gênero válido.')
        except:
            pass
        try:
            if isinstance(vargenero, int) is False:
                vargenero = float(vargenero)
                print('ERRO! Digite um gênero válido.')
            else:
                pass
        except:
            pass