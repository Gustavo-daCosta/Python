lista, opcao, cont, escolha = dict(), 'S', 0, '0'

def mostrarLista():
    print('-'*40)
    print('NÚMERO\tITEM\tQUANTIDADE')
    for u in (lista.keys):
        for n in lista.values:
            print(f'{u}\t{n[0]}\t{n[1]}')
    print('-'*40)

while True:
    cont += 1
    print(f'ITEM {cont}'.center(40, '-'))
    item = str(input('Nome do item: '))
    quantidade = int(input('Quantidade do item: '))
    lista[cont] = item, quantidade
    print('Item adicionado a lista!')
    print('-'*40)
    while True:
        opcao = str(input('Deseja continuar? [S/N]: ')).upper()
        if opcao in 'SN':
            break
        else:
            print('ERRO! Digite uma opção válida.')
    if opcao in 'N':
        mostrarLista()
        while True:
            print('''       OPÇÕES
[ 1 ] Adicionar um novo item a lista.
[ 2 ] Excluir um item da lista.
[ 3 ] Ver a lista.
[ 4 ] Encerrar o programa''')
            escolha = str(input('Escolha uma opção: '))
            if (escolha == 1) or (escolha == 2) or (escolha == 3) or (escolha == 4):
                break
            else:
                print('ERRO! Valor inválido digitado.')
        if escolha == 2:
            while True:
                item = str(input('Nome do item que será excluido: '))
                if item not in lista:
                    print('ERRO! Esse item não existe na lista.')
                else:
                    del lista(item)
                    break
        elif escolha == 3:
            mostrarLista()
        else:
            break
    if escolha == 4:
        break