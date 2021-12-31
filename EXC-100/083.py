from random import randint

def mostrarValores():
    print(f'Posição\t\tValor')
    for c in range(0, 20):
        numeros.append(randint(0, 99))
        print(f' {c}\t\t {numeros[c]}')

numeros = list()

mostrarValores()
numeros.sort()
print('NÚMEROS ORDENADOS'.center(50, '-'))
mostrarValores()