def metade(n=0):
    return n/2

def dobro(n=0):
    return n*2


def aumentar(n=0, porc=0):
    dif = n * (porc/100)
    return n+dif


def diminuir(n=0, porc=0):
    dif = n * (porc/100)
    return n-dif

def moeda(preco=0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')