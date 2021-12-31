valor = lata1 = lata2 = lata3 = 0

print('=-='*15)
print('LOJA DE TINTAS'.center(45))
print('=-='*15)
quant = int(input('Quantas latas de tinta você deseja comprar? '))
for c in range(0, quant):
    print('LATA DE TINTA'.center(45, '-'))
    print('''[ 1 ] TINTA AZUL: \tR$80,00
    [ 2 ] TINTA BRANCA: \tR$60,00
    [ 3 ] TINTA VERMELHA: \tR$100,00
    Obs: Todas as latas de tinta tem 18 litros.''')
    while True:
        tinta = int(input('Escolha uma opção: '))
        if tinta == 1 or tinta == 2 or tinta == 3:
            break
        else:
            print('\033[0;031mERRO! Valor inválido digitado, tente novamente.\033[m')
    if tinta == 1:
        valor += 80
        lata1 += 1
    if tinta == 2:
        valor += 60
        lata2 += 1
    if tinta == 3:
        valor += 100
        lata3 += 1
print('=-='*15)