lista, pessoa = list(), list()

for c in range(0, 9):
    print(f'{c+1}° CADASTRO'.center(50, '-'))
    while True:
        nome = str(input('Nome: '))
        try:
            nome = int(nome)
            print('ERRO! Digite um nome válido')
        except:
            pass
        try:
            nome = float(nome)
            print('ERRO! Digite um nome válido.')
        except:
            pass
        if isinstance(nome, str) is True:
            break
    while True:
        try:
            idade = int(input('Idade: '))
        except:
            print('ERRO! Idade inválida.')
        if isinstance(idade, int) is True:
            break
    if idade < 18:
        pessoa = [nome, idade]
        lista.append(pessoa)
        pessoa.clear
print('LISTAGEM DE MENORES DE IDADE'.center(50, '-'))
print(f'NOME\tIDADE')
for c in range(0, len(lista)):
    if lista[c][1] < 18:
        print(f'{lista[c][0]}\t{lista[c][1]}')