vetor = list()

for c in range(0, 7):
    vetor.append(str(input(f'Digite o {c+1}° nome: ')))
print('-'*40)
print(vetor[::-1])