data, media, total, aprovados = [], 0, 0, 0
for c in range(1, 11):
    print(f'=-=-= ALUNO {c} =-=-=')
    for x in range(1, 5):
        nota = float(input(f'Digite a {x}° nota: '))
        total += nota
    media = total/4
    data.append(media)
for c in range(0, 10):
    if data[c] >= 7.0:
        aprovados += 1
print(f'Total de alunos aprovados (média maior ou igual a 7.0): {aprovados}')