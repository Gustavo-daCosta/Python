import random
al1 = input('Digite o nome do primeiro aluno: ')
al2 = input('Digite o nome do segundo aluno: ')
al3 = input('Digite o nome do terceiro aluno: ')
al4 = input('Digite o nome do quarto aluno: ')
alunos = (al1, al2, al3, al4)
print (f'O aluno sorteado foi {random.choice(alunos)}')