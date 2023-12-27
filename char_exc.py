# pede os valores ao usuário
vetor1Length = int(input())
vetor1 = str(input())
vetor2Length = int(input())
vetor2 = str(input())

# transforma as strings em listas
vetor1 = vetor1.strip().split(" ")
vetor2 = vetor2.strip().split(" ")

# Verifica se o vetor 1 é maior que o vetor 2
# além de definir qual lista é maior e qual é menor
if vetor1Length >= vetor2Length:
    higherList = vetor1
    minorList = vetor2
else:
    higherList = vetor2
    minorList = vetor1

result = list()
for item in higherList:
    if item not in minorList:
        result.append(item)

print(*result, sep=" ")