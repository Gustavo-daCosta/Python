anterior = sucessor = 0
vetor = list()

for c in range(0, 17):
    if sucessor != 0:
        vetor.append(sucessor)
    sucessor = sucessor + anterior
    anterior = sucessor - anterior
    if sucessor == 0:
        sucessor += 1
print(vetor)