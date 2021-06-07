from random import randint
rand = randint(1, 3)
print('=-='*20)
print('                           JOKENPÔ')
print('=-='*20)
print('''OPÇÕES
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
opcao = int(input('Digite sua opção: '))
if opcao==rand:
    if opcao==1:
        print('Ambos jogaram PEDRA!')
    elif opcao==2:
        print('Ambos jogaram PAPEL!')
    elif opcao==3:
        print('Ambos jogaram TESOURA!')
    print('HOUVE EMPATE')
elif opcao==1 and rand==3:
    print('''Sua jogada: Pedra
Jogada do computador: Tesoura 
Parábens! Você venceu.''')
elif opcao==1 and rand==2:
    print('''Sua jogada: Pedra
Jogada do computador: Papel
Você perdeu! Tente novamente :(''')
elif opcao==2 and rand==3:
    print('''Sua jogada: Papel
Jogada do computador: Tesoura
Você perdeu! Tente novamente :(''')
elif opcao==2 and rand==1:
    print('''Sua jogada: Papel
Jogada do computador: Pedra
Parabéns! Você venceu.''')
elif opcao==3 and rand==1:
    print('''Sua jogada: Tesoura
Jogada do computador: Pedra
Você perdeu! Tente novamente :(''')
elif opcao==3 and rand==2:
    print('''Sua jogada: Tesoura
Jogada do computador: Papel
Parabéns! Você venceu.''')
else:
    print('OPÇÃO INVÁLIDA. Tente novamente.')