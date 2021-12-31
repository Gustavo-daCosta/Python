def area(a, b):
    result = a*b
    print(f'A área de um terreno {a:.1f}x{b:.1f} é de {result:.1f}m²')

print('Controle de Terrenos')
print('--------------------')
area(a = float(input('LARGURA (m): ')),
b = float(input('COMPRIMENTO (m): ')))