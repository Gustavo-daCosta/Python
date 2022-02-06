dadosListados = list()

for c in range(0, 5):
    while True:
        print(f'\n{f"FUNCIONÁRIO {c+1}":^50}')
        try:
            nome = str(input('Nome: '))
            genero = str(input('Genêro [M/F]: '))
            salario = float(input('Salário: R$'))
            if genero.upper() not in 'MF':
                raise ValueError
            break
        except:
            print('ERRO! Tente novamente.')
    if genero == 'F' and salario > 5000:
        dadosListados.append(nome)
    
print('Funcionárias do genêro feminino que ganham mais de R$5 mil:')
for nome in dadosListados:
    print(f'{(dadosListados.index(nome)) + 1} - {nome}')
    del(dadosListados[dadosListados.index(nome)])