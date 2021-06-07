estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
# dict.COPY = Serve para copiar um dicionário, é uma forma de fatiar dicionários
for e in brasil:
    for k, v in e.items():
        print(v, end='-')
    print()

total = sum(brasil)
# Se todos os valores forem numéricos, soma todos os valores da lista e retorna o resultado