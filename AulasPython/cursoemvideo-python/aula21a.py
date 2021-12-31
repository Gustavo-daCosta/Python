def somar(a, b, c):
    s = a + b + c
    """
    [Faz a soma de três valores e mostra o resultado na tela.]
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    """
    return s
# return - Serve para retornar um valor da função
s = somar(3, 2, 5)
print(f'A soma vale {s}')

def mult(a=0, b=0, c=0):
    m = a*b*c
    return m
# Quando o parâmetro tiver um valor anexado a ele, ele vira um parâmetro opcional em que o usuário não
# é obrigado a dar um valor ao parâmetro, por exemplo "a=0"