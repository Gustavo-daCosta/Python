parent1 = parent2 = expressao = resultado = r =0
r = str(input('Digite a expressão: '))
expressao = list(r)
for i, cont in enumerate(expressao):
    if '(' in expressao:
        parent1 += 1
        expressao.remove('(')
    if ')' in expressao:
        parent2 += 1
        expressao.remove(')')
if parent1 == parent2:
    print('Sua expressão é válida!')
else:
    print('Sua expressão está errada!')