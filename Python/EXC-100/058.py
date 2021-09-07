soma, total = 0, 1
while True:
    print(f'{total}° ALUNO'.center(40, '-'))
    idade = int(input('Idade do aluno: '))
    if idade == 999:
        print('Finalizando...')
        break
    else:
        total += 1
        soma += idade
print('-'*40)
print(f'Total de alunos na turma: {total-1} alunos')
print(f'Média de idade da turma: {soma/(total-1):.1f} anos')