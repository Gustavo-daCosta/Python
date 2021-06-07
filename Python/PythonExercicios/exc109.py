from exc109 import moeda

p = float(input('Digite o preço: R$'))
print(f'A Metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'Aumentando 10% de {moeda.moeda(p)} temos {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo 13% de {moeda.moeda(p)} temos {moeda.aumentar(p, 13, True)}')