ficha = list()
opcao, opc = 'S', 0
while True:
    print('=-='*8)
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    opcao = str(input('Quer continuar? [S/N]: ').upper())
    if opcao == 'N':
        break
print('=-='*8)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('=-='*8)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while opc != 999:
    print('=-='*8)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc <= len(ficha):
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<<<< VOLTE SEMPRE >>>>>')