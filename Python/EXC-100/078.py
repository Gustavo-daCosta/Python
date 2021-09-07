vetor = list()

for c in range(0, 15):
    vetor.append(int(input(f'Digite o {c+1}° valor: ')))
print(vetor)
print('-'*40)
for c in range(0, len(vetor)):
    if vetor[c] % 10 == 0:
        print(f'O número {vetor[c]} na posição {c+1} é múltiplo de 10')