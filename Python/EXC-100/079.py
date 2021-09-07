vetor = list()

for c in range(0, 10):
    vetor.append(int(input(f'Digite o {c+1}° valor: ')))
print('-'*40)
print(vetor)
print('-'*40)
for c in range(0, 10):
    if vetor[c] % 2 == 0:
        print(f'O valor {vetor[c]} na posição {c+1} é par.')