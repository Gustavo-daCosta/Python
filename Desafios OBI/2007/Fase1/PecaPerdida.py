# Status do exercício: Completo e funcionando

linha1 = int(input())
linha2 = str(input())
listaNumeros = [int(number) for number in linha2.split(" ")]

for numero in listaNumeros:
    antecessor = numero - 1
    if antecessor > 0 and antecessor not in listaNumeros:
        falta = antecessor
        print(falta)