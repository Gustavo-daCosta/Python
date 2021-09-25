def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

def soma(* valores):
    s = 0
    for num in valores:
        s += num

soma(5, 2)
soma(2, 9, 4)
print(soma)

def :
    global variavel
# global - Faz uma variável local se transformar em uma variável global