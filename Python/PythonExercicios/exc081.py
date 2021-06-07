lista = []
opcao = 'S'
while opcao != 'N':
    print('=-='*20)
    n = (int(input('Digite um valor: ')))
    lista.append(n)
    if n == 5:
        tem5 = 'O valor 5 está na lista.'
    opcao = str(input('Você deseja continuar? [S/N]: ').upper())
print('=-='*20)
print(f'Total de valores digitados: {len(lista)}')
print(f'Lista de valores em ordem decrescente: {sorted(lista, reverse=True)}')
print(tem5)