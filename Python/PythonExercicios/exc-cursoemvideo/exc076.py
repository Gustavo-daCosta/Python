produtos = ("Saco de Arroz", 15, 'Feijão', 8.50, 'Café', 10, 'Bolo', 20.50, 'Açúcar', 6, 'Suco', 5, 'Frango', 18)
titulo, cont = 'SUPERMERCADO VAREJO', 0
print('=-=-='*11)
print(titulo.center(55))
print('=-=-='*11)
while cont != 12:
    nome, preço = produtos[cont], produtos[cont+1]
    preço1 = f'{preço:.2f}'
    print(nome.ljust(44, '.'), 'R$', f'{preço1:>6}')
    cont += 2