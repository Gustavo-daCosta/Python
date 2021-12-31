cont, opcao, titulo, num = 0, 'S', 0, 0
valor = []
while opcao != 'N':
    titulo = f' VALOR {cont} '
    print(f'{titulo:-^50}')
    num = (int(input('Digite um valor numérico: ')))
    if num not in valor:
        valor.append(int(num))
        print('Valor adicionado com sucesso!')
        cont += 1
    else:
        print('Este valor já foi adicionado anteriormente! Tente novamente.')
    print('-'*50)
    opcao = str(input('Você deseja continuar? [S/N]: ').upper())
print('='*50)
final = valor.sort()
print(f'Os valores digitados em ordem crescente são: {sorted(valor)}')