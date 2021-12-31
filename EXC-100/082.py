soma = media = acimaMedia = maior = nota = 0
notas, maiorNota = list(), list()

for c in range(1, 11):
    print(f'{c}° ALUNO'.center(50, '-'))
    while True:
        try:
            nota = str(input(f'Digite a nota do {c}° aluno: '))
        except:
            print('ERRO! Valor inválido digitado. Digite um valor inteiro.')
        if isinstance(nota, int or float) == True:
            break
    notas.append(nota)
    soma += nota
    if c == 1:
        maior == nota
    else:
        if nota > maior:
            maior = nota
media = soma/10
for c in range(0, 10):
    if notas[c] > media:
        acimaMedia += 1
    if notas[c] == maior:
        maiorNota.append(c)
print('RESULTADOS'.center(50, '-'))
print(f'''Média da turma: {media:.1f}
Total de alunos acima da média: {acimaMedia} alunos
Maior nota registrada: {maior}
Posições em que a maior nota aparece: {maiorNota}''')