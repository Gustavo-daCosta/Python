from random import randint

titulo, msg = 'PEDRA-PAPEL-TESOURA', ''
while True:
    print('-'*40)
    print(f'{titulo:^40}')
    print('-'*40)
    print('''PEDRA   [ 1 ]
PAPEL   [ 2 ]
TESOURA [ 3 ]''')
    opcao = int(input('Escolha uma opção: '))
    print('-'*40)
    comput = randint(1, 3)
    print(comput)
    
    if opcao == 1:
        opcao = 'PEDRA'
    if opcao == 2:
        opcao = 'PAPEL'
    if opcao == 3:
        opcao = 'TESOURA'
    if comput == 1:
        comput = 'PEDRA'
    if comput == 2:
        comput = 'PAPEL'
    if comput == 3:
        comput = 'TESOURA'
    #-------------------------
    if (opcao == 'PEDRA' and comput == 'TESOURA') or (opcao == 'PAPEL' and comput == 'PEDRA') or (opcao == 'TESOURA' and comput == 'PAPEL'):
        msg = 'Parábens! Você venceu! (:'  
    if (comput == 'PEDRA' and opcao == 'TESOURA') or (comput == 'PAPEL' and opcao == 'PEDRA') or (comput == 'TESOURA' and opcao == 'PAPEL'):
        msg = 'Infelizmente você perdeu ):'
    if opcao == comput:
        msg = 'Empate! Ambos fizeram a mesma jogada.'
    
    print(f'Sua jogada: {opcao}      Jogada do computador: {comput}')
    print(msg)
    print('-'*40)
    while True:
        opcao = str(input('Deseja continuar? [S/N]: '))
        if opcao in 'SsNn':
            break
    if opcao in 'Nn':
        break
print('Obrigado por jogar!')