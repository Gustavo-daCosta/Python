quadradoMagico = list()
proporcaoQuadrado = int(input())
for c in range(0, proporcaoQuadrado):
    linha = str(input())
    quadradoMagico.append([int(numero) for numero in linha.split(" ")])

tamanhoLinha = len(quadradoMagico[1])
total = 0
for lista in range(0, tamanhoLinha):
    soma = 0
    for valor in range(0, tamanhoLinha):
        soma += quadradoMagico[lista][valor]
    total += soma

if soma == total/tamanhoLinha:
    print(f"\n{soma}")
else:
    print("-1")