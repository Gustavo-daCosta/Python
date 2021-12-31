titulo = 'ANÁLISE DE MÉDIAS'
print('-'*40)
print(f'{titulo:^40}')
print('-'*40)
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
media = (nota1 + nota2) / 2
if media < 5:
    situacao = 'Reprovado'
elif media >= 5 and media < 7:
    situacao = 'Recuperação'
else:
    situacao = 'Aprovado'
print(f'Média do aluno: {media:.1f}')
print(f'Situação do aluno: {situacao}')