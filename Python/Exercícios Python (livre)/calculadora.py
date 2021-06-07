n1, n2, opcao, titulo, operacao, resultado, txt = 0, 0, 'S', 'CALCULADORA', 0, 0, ' '
while True:
    print('=-='*20)
    print(titulo.center(60))
    print('=-='*20)
    n1 = float(input('Digite o 1° número: '))
    print('[ 1 ] ADIÇÃO')
    print('[ 2 ] SUBTRAÇÃO')
    print('[ 3 ] MULTIPLICAÇÃO')
    print('[ 4 ] DIVISÃO')
    operacao = int(input('Digite o número da operação: '))
    n2 = float(input('Digite o 2° número: '))
    if operacao == 1:
        resultado = n1 + n2
        txt = f'A soma entre {n1} e {n2} é igual a {resultado}'
    elif operacao == 2:
        resultado = n1 - n2
        txt = f'A subtração entre {n1} e {n2} é igual a {resultado}'
    elif operacao == 3:
        resultado = n1*n2
        txt = f'A multiplicação entre {n1} e {n2} é igual a {resultado}'
    elif operacao == 4:
        resultado = n1/n2
        txt = f'A divisão de {n1} por {n2} é igual a {resultado}'
    else:
        print('OPERAÇÃO INVÁLIDA!')
        break
    print('=-='*30)
    print(txt)
    opcao = str(input('Você deseja continuar? [S/N]: ').upper)
    if opcao == 'N':
        break