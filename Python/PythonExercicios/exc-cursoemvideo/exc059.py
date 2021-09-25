resultado = 0
opcao = 0
while opcao != 7:
    v1 = int(input('Digite o 1° valor: '))
    v2 = int(input('Digite o 2° valor: '))
    print('[ 1 ] SOMAR')
    print('[ 2 ] SUBTRAIR')
    print('[ 3 ] MULTIPLICAR')
    print('[ 4 ] DIVIDIR')
    print('[ 5 ] MAIOR VALOR')
    print('[ 6 ] NOVOS VALORES')
    print('[ 7 ] ENCERRAR PROGRAMA')
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        resultado = v1+v2
    elif opcao == 2:
        resultado = v1-v2
    elif opcao == 3:
        resultado = v1*v2
    elif opcao == 4:
        resultado = (v1/v2)
    elif opcao == 5:
        if v1 > v2:
            resultado = v1
        else:
            resultado = v2
    elif opcao == 6:
        print('Digite os novos números: ')
    print(f'Resultado: {resultado}')