lista = []
total = 0
nome = str(input('Digite o nome do aluno: '))
for c in range(0, 4):
    nota = float(input(f'Digite a {c+1}° nota do aluno: '))
    lista.append(nota)
    total += nota
media = total/4
print(f'As 4 notas de {nome} são: ', end='')
for c in range(0, 4):
    print({lista[c]}, end=' → ')
print('FIM')
print(f'A média de {nome} é: {media:.1f}')