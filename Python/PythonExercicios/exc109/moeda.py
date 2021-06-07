def metade(n=0, form=False):
    resp = n/2
    return resp if not form else moeda(resp)

def dobro(n=0, form=False):
    resp = n*2
    return resp if not form else moeda(resp)

def aumentar(n=0, porc=0, form=False):
    resp = n +(n * (porc/100))
    return resp

def diminuir(n=0, porc=0, form=False):
    resp = n -(n * (porc/100))
    return resp

def moeda(preco=0, moeda = 'R$', form=False):
    return f'{moeda}{preco:.2f}'.replace('.', ',')