def fatorial(num=1, show=False):
    """[Calcula o fatorial de um número]

    Args:
        num (int): [O número a ser calculado]. Defaults to 1.
        show (bool, optional): [Mostrar ou não a conta]. Defaults to False.

    Returns:
        [int]: [O valor do fatorial de um número n]
    """
    f = 1
    if show == True:
        for c in range(num, 0, -1):
            f *= c
            print(c, end=' x ')
        return (f'= {f}')
    else:
        for c in range(num, 0, -1):
            f *= c
        return f'{f}'

print('-'*30)
print(fatorial(5, show=True))
print(fatorial(3, show=False))
print(fatorial(9))
print(fatorial(8, show=True))
help(fatorial)