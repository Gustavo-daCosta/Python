lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print(len(lanche))
for cont in range(0, (len(lanche))):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')
for cont in lanche:
    print(f'Eu vou comer {cont}')
print('Comi pra caramba!')
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print('Comi pra caramba!')

print(sorted(lanche))
# SORTED = Transfoma a Tupla em uma Lista e a mostra em ordem alfabética