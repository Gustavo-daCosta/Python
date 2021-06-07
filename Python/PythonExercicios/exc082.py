lista, par, impar = [], [], []
opcao = 'S'
while opcao != 'N':
    print('=-='*20)
    n = (int(input('Digite um valor: ')))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    opcao = str(input('Você deseja continuar? [S/N]: ').upper())
print('=-='*20)
print(f'Lista com todos os valores: {lista}')
print(f'Lista com valores PARES: {par}')
print(f'Lista com valores ÍMPARES: {impar}')