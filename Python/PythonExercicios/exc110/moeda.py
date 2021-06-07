def metade(n=0, form=False):
    resp = n/2
    return resp if not form else moeda(resp)

def dobro(n=0, form=False):
    resp = n*2
    return resp if not form else moeda(resp)

def aumentar(n=0, porc=0, form=False):
    resp = n +(n * (porc/100))
    return resp if not form else moeda(resp)

def diminuir(n=0, porc=0, form=False):
    resp = n -(n * (porc/100))
    return resp if not form else moeda(resp)

def moeda(preco=0, moeda = 'R$', form=False):
    return f'{moeda}{preco:.2f}'.replace('.', ',')

def resumo(preco=0, taxaa=0, taxar=0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'Com {taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'Com {taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('-'*30)